import random
import re

from flask import request, abort, redirect, render_template, session

from app import app

user_list = [{'id': 1, 'name': 'Eugen'}, {'id': 2, 'name': 'Max'}, {'id': 3, 'name': 'David'},
             {'id': 4, 'name': 'Fox'}, ]
book_list = [{'id': 1, 'title': 'Duna'}, {'id': 2, 'title': 'Inferno'}, {'id': 3, 'title': 'Royal Assassin'},
             {'id': 4, 'title': 'Royal Assassin 2'}]


@app.get('/users')
def users_list():
    email = session.get('email')
    if session_username(email):
        count = request.args.get('count')
        if count:
            count_int = int(count)
        else:
            count_int = random.randint(1, 50)

        user_lst = []
        for i in range(count_int):
            random_item = random.choice(user_list)
            random_name = random_item['name']
            user_lst.append(random_name)
        users_lst = [user for user in user_lst]

        user_name = print_username()
        context = {
            'username': user_name,
            'title': 'Users list',
            'users': users_lst,
        }
        return render_template('main/users.html', **context), 200
    else:
        return redirect('/login')


@app.get('/books')
def books_list():
    email = session.get('email')
    if session_username(email):

        count = request.args.get('count')
        if count:
            count_int = int(count)
        else:
            count_int = random.randint(1, 50)
        book_lst = []
        for i in range(count_int):
            random_item = random.choice(book_list)
            random_title = random_item['title']
            book_lst.append(random_title)
        books_lst = [book for book in book_lst]

        context = {
            'title': 'Book list',
            'books': books_lst,
            'username': print_username(),
        }
        return render_template('main/books.html', **context), 200
    else:
        return redirect('/login')


@app.get('/users/<user_id>')
def user_detail(user_id):
    email = session.get('email')
    if session_username(email):
        try:
            user_id_int = int(user_id)
        except ValueError:
            abort(400, 'Invalid task id')

        user = None
        if not user_id_int % 2:
            for item in user_list:
                if user_id_int == item['id']:
                    user = item
                    break

        if not user:
            abort(404, 'User not found')

        context = {
            'user': user,
            'title': 'User detail',
            'username': print_username(),
        }
        return render_template('main/user_detail.html', **context), 200
    else:
        return redirect('/login')


@app.get('/books/<title>')
def book_title(title):
    email = session.get('email')
    if session_username(email):
        new_title = title.capitalize()

        context = {
            'book_title': new_title,
            'title': 'Book detail',
            'username': print_username(),
        }
        return render_template('main/book_title.html', **context), 200
    else:
        return redirect('/login')



@app.get('/params')
def params():
    email = session.get('email')
    if session_username(email):
        name = request.args.get('name')
        age = request.args.get('age')

        context = {
            'name': name,
            'age': age,
            'title': 'Parameters',
            'username': print_username(),
        }

        return render_template('main/params.html', **context), 200
    else:
        return redirect('/login')


def password_valid(password):
    pattern = r'^(?=.*\d)(?=.*[A-Z]).{8,}$'
    if re.match(pattern, password):
        return True
    else:
        return False


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


@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/login')


def session_username(email):
    if session.get('email') is None:
        return False
    elif session.get('email') == email:
        return True
    else:
        return False


def print_username():
    username = session.get('email')
    return username


@app.errorhandler(404)
def not_found_error(error):
    requests = f'''
    <p1>The page you are looking for does not exist</p1>
    '''
    return requests, 404


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
