from flask import Flask, request, make_response, redirect, render_template

todos = ['TODO 1', 'TODO 2', 'TODO 3', 'TODO 4', 'TODO 5']
app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos': todos
    }
    #return 'Hello World from {} ip'.format(user_ip)
    return render_template( 'hello.html', **context) 



