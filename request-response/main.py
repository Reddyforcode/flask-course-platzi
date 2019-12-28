from flask import request, make_response, redirect, render_template, session, url_for, flash
from app import create_app
from app.forms import LoginForm
#test
import unittest
todos = ['comprar cafe', 'enviar solicitud de compra', 'TODO 3', 'TODO 4', 'TODO 5']
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

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    #user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form,
        'username': username
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        flash('Nombre de usuario registrado con exito')
        return redirect(url_for('index'))
        # dete ta cuando se manda un post y valida una forma
    #return 'Hello World from {} ip'.format(user_ip)
    return render_template( 'hello.html', **context) 