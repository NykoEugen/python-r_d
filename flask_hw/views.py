import random
import re

from flask import request, abort, redirect

from app import app

user_list = [{'id': 1, 'name': 'Eugen'}, {'id': 2, 'name': 'Max'}, {'id': 3, 'name': 'David'},
             {'id': 4, 'name': 'Fox'}, ]
book_list = [{'id': 1, 'title': 'Duna'}, {'id': 2, 'title': 'Inferno'}, {'id': 3, 'title': 'Royal Assassin'},
             {'id': 4, 'title': 'Royal Assassin 2'}]


@app.get('/users')
def users_list():
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
    users_html = ''.join(f'<li>{user}</li>'
                         for user in user_lst)

    response = f'''
    <h1>Users List</h1>
    <ul>
        {users_html}
    </ul>
    '''
    return response, 200


@app.get('/books')
def books_list():
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
    books_html = ''.join(f'<li>{book}</li>'
                         for book in book_lst)

    response = f'''
        <h1>Users List</h1>
        <ul>
            {books_html}
        </ul>
        '''
    return response, 200


@app.get('/users/<user_id>')
def user_detail(user_id):
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

    response = f'''
    <h1>{user['name']}</h1>'''
    return response, 200


@app.get('/books/<title>')
def book_title(title):
    new_title = title.capitalize()

    response = f'''
    <h1>{new_title}</h1>'''
    return response, 200


@app.get('/params')
def params():
    name = request.args.get('name')
    age = request.args.get('age')

    requests = f'''
    <table>
        <tr>
            <th>parameter</th>
            <th>|</th>
            <th>value</th>
        </tr>
        <tr>
            <td>name</td>
            <td>|</td>
            <td>{name}</td>
        </tr>
        <tr>
            <td>age</td>
            <td>|</td>
            <td>{age}</td>
        </tr>
    </table>
    '''

    return requests, 200


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
                return redirect('/users')
            else:
                abort(400, 'Invalid password')
        else:
            abort(400, 'Invalid data')

    else:
        return f'''
            <form method="POST" action="/login">
                <label for="email">Email:</label>
                <input type="email" name="email" id="email"><br><br>
                <label for="password">Password:</label>
                <input type="password" name="password" id="password"><br><br>
                <input type="submit" value="Submit">
            </form>
            '''


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


@app.get('/links')
def links_list():
    requests = f'''
    <table>
        <tr><td><a href=127.0.0.1:5000/login">login</a></td></tr>
        <tr><td><a href=127.0.0.1:5000/users">users</a></td></tr>
        <tr><td><a href=127.0.0.1:5000/books">books</a></td></tr>
        <tr><td><a href=127.0.0.1:5000/params">params</a></td></tr>
    </table>
    '''
    return requests, 200
