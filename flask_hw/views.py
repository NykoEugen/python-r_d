import json
import random
import re
from functools import wraps

from flask import request, abort, redirect, render_template, session, jsonify

from app import app, db
from models import *

user_list = [{'id': 1, 'name': 'Eugen'}, {'id': 2, 'name': 'Max'}, {'id': 3, 'name': 'David'},
             {'id': 4, 'name': 'Fox'}, ]
book_list = [{'id': 1, 'title': 'Duna'}, {'id': 2, 'title': 'Inferno'}, {'id': 3, 'title': 'Royal Assassin'},
             {'id': 4, 'title': 'Royal Assassin 2'}]


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            email = request.form['email']
            password = request.form['password']
        except KeyError:
            abort(400, 'Invalid data')

        if len(email) >= 5:
            validator = password_valid(password)
            if validator:
                session['email'] = email
                return redirect('/users')
            else:
                abort(400, 'Invalid password')
        else:
            abort(400, 'Invalid data')

    else:
        return render_template('main/login.html'), 200


def session_username(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('email') is None:
            return redirect('/login')
        return func(*args, **kwargs)

    return wrapper


def int_validator(param_num):
    if param_num:
        try:
            param_int = int(param_num)
        except ValueError:
            return 'Invalid parameter size', 400
    else:
        param_int = None
    return param_int


@app.get('/users')
@session_username
def users_list():
    response_param = request.args.get('format')
    size = request.args.get('size')
    user_name = print_username()

    size_int = int_validator(size)
    query = db.session.query(Users)
    if size_int is not None:
        query = query.limit(size_int)
        users = db.session.execute(query).scalars()
    else:
        query = db.select(Users)
        users = db.session.execute(query).scalars()

    if response_param == 'json':
        req = [{'id': user.id, 'first_name': user.first_name,
                'last name': user.last_name, }
               for user in users]
        return req

    context = {
        'username': user_name,
        'title': 'Users list',
        'users': users,
    }

    return render_template('main/users.html', **context), 200


@app.get('/books')
@session_username
def books_list():
    response_param = request.args.get('format')
    size = request.args.get('size')

    size_int = int_validator(size)
    query = db.session.query(Books)
    if size_int is not None:
        query = query.limit(size_int)
        books = db.session.execute(query).scalars()
    else:
        query = db.select(Books)
        books = db.session.execute(query).scalars()

    if response_param == 'json':
        req = [{'id': book.id, 'title': book.title,
                'author': book.author, 'price': book.price, }
               for book in books]
        return req

    context = {
        'title': 'Book list',
        'books': books,
        'username': print_username(),
    }
    return render_template('main/books.html', **context), 200


@app.get('/users/<user_id>')
@session_username
def user_detail(user_id):
    try:
        user_id_int = int(user_id)
    except ValueError:
        abort(400, 'Invalid user id')

    query_count = db.session.query(Users).count()
    if user_id_int > query_count:
        abort(404, 'User not found')

    query = db.select(Users).where(Users.id == user_id_int)
    user = db.session.execute(query).scalars().first()

    context = {
        'user': user,
        'title': 'User detail',
        'username': print_username(),
    }
    return render_template('main/user_detail.html', **context), 200


@app.get('/books/<book_id>')
@session_username
def book_title(book_id):
    try:
        book_id_int = int(book_id)
    except ValueError:
        abort(400, 'Invalid user id')

    query_count = db.session.query(Books).count()
    if book_id_int > query_count:
        abort(404, 'Book not found')

    query = db.select(Books).where(Books.id == book_id_int)
    book = db.session.execute(query).scalars().first()

    context = {
        'book': book,
        'title': 'Book detail',
        'username': print_username(),
    }
    return render_template('main/book_title.html', **context), 200


@app.get('/purchases')
@session_username
def purchases():
    response_param = request.args.get('format')
    size = request.args.get('size')
    size_int = int_validator(size)

    query = db.session.query(Users.id, Users.first_name, Users.last_name,
                             Books.title, Books.author, ) \
        .join(Purchase, Users.id == Purchase.user_id) \
        .join(Books, Purchase.book_id == Books.id) \
        .order_by(Users.id)

    if size_int is not None:
        query = query.limit(size_int)

    result = query.all()

    if response_param == 'json':
        req = [{'id': item.id, 'first_name': item.first_name,
                'last name': item.last_name, 'title': item.title,
                'author': item.author, }
               for item in result]
        return req

    context = {
        'purchases': result,
        'title': 'Purchase cart',
        'username': print_username(),
    }
    return render_template('main/purchases.html', **context), 200


@app.get('/purchases/<purchase_id>')
@session_username
def purchase_detail(purchase_id):
    try:
        purchase_id_int = int(purchase_id)
    except ValueError:
        abort(400, 'Invalid user id')

    query_count = db.session.query(Purchase).count()
    if purchase_id_int > query_count:
        abort(404, 'Purchase number not found')

    query = db.session.query(Users.id, Users.first_name, Users.last_name,
                             Books.title, Books.author) \
        .join(Purchase, Users.id == Purchase.user_id) \
        .join(Books, Purchase.book_id == Books.id) \
        .filter(Purchase.id == purchase_id_int)
    result = query.all()
    context = {
        'purchases': result,
        'title': 'Purchase cart',
        'username': print_username(),
    }
    return render_template('main/purchase_detail.html', **context), 200


@app.get('/params')
@session_username
def params():
    name = request.args.get('name')
    age = request.args.get('age')

    context = {
        'name': name,
        'age': age,
        'title': 'Parameters',
        'username': print_username(),
    }

    return render_template('main/params.html', **context), 200


def password_valid(password):
    pattern = r'^(?=.*\d)(?=.*[A-Z]).{8,}$'
    if re.match(pattern, password):
        return True
    else:
        return False


@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/login')


def print_username():
    username = session.get('email')
    return username


# @app.errorhandler(404)
# def not_found_error(error):
#     requests = f'''
#     <p1>The page you are looking for does not exist</p1>
#     '''
#     return requests, 404


@app.errorhandler(500)
def not_found_error(error):
    requests = f'''
    <p1>Something bad happened</p1>
    '''
    return requests, 500


@app.get('/')
def link_list():
    login = '/login'
    logout = '/logout'
    users = '/users'
    books = '/books'
    params = '/params'
    context = {
        'title': 'Book store',
        'login': login,
        'logout': logout,
        'users': users,
        'books': books,
        'params': params,
    }

    return render_template('base.html', **context), 200
