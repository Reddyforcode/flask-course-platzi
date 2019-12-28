from flask import request, make_response, redirect, render_template, session, url_for, flash
from app import create_app
from app.forms import LoginForm
from app.firestore_service import get_users, get_todos
#test
import unittest

app = create_app()

@app.cli.command()
def test():
    test = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(test)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def not_found500(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    #response.set_cookie('user_ip', user_ip)
    session['user_ip']=user_ip
    return response

@app.route('/hello', methods=['GET'])
def hello():
    user_ip = session.get('user_ip')
    username = session.get('username')
    todos = [ todo.to_dict()['description'] for todo in get_todos(username)]
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'username': username
    }
    users = get_users()
    for user in users:
        #users is a snapshot
        print(user.id)
        print(user.to_dict())
    return render_template( 'hello.html', **context) 