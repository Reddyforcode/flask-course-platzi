from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap
todos = ['comprar cafe', 'enviar solicitud de compra', 'TODO 3', 'TODO 4', 'TODO 5']
app = Flask(__name__)
bootstrap = Bootstrap(app) 

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



