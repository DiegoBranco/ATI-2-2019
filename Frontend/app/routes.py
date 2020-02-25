from flask import render_template, flash, redirect, url_for
from app import app, mongo
from app.forms import LoginForm
from flask_babel import _

@app.route('/ejemplo')
def ejemplo():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('ejemplo.html', title='Home', user=user, posts=posts)

@app.route('/')
def index():
    cursos=[
    {'cert':'Marketing digital',
    'description':'Descripcion de curso pendiente'},
    {'cert':'Javascript',
    'description':'Descripcion de curso pendiente'},
    {'cert':'ReactJS',
    'description':'Descripcion de curso pendiente'},
    {'cert':'Angular',
    'description':'Descripcion de curso pendiente'},
    {'cert':'Rails',
    'description':'Descripcion de curso pendiente'},
    {'cert':'Python',
    'description':'Descripcion de curso pendiente'}
    ]
    clientes=['Google', 'Platzi', 'Yahoo', 'Bing']
    return render_template('index.html', title="ATI te educamos", cursos=cursos, clientes=clientes)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        mongo.db.user.insert_one({'username': form.username.data})
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('home'))

    users = mongo.db.user.find({})

    print(users)
    return render_template('login.html', title='Sign In', form=form, users = users, message= _("hi"))

@app.route('/home')
def home():
    user = {'username':'Miguel'}
    post = {
        'cursos':{
        'ultimo':{
        'cert':'HTML',
        'description':'Curso introductorio de HTML5'},
        'terminados':[
    {'cert':'Marketing digital',
    'description':'Descripcion de curso pendiente'},
    {'cert':'Javascript',
    'description':'Descripcion de curso pendiente'},
    {'cert':'ReactJS',
    'description':'Descripcion de curso pendiente'},
    {'cert':'Angular',
    'description':'Descripcion de curso pendiente'},
    {'cert':'Rails',
    'description':'Descripcion de curso pendiente'},
    {'cert':'Python',
    'description':'Descripcion de curso pendiente'}
    ],
    'disponibles':[
    {'cert':'Ruby',
    'description':'Descripcion de curso pendiente'},
    {'cert':'C++',
    'description':'Descripcion de curso pendiente'},
    {'cert':'CSS',
    'description':'Descripcion de curso pendiente'}
    ]}}
    return render_template('home.html', title='Home', user=user, post=post)


@app.errorhandler(404) 
def not_found():
    return("not found")



# @app.route('/static/styles/<path:path>')
# def send_js(path):
#     return send_from_directory('js', path)