from flask import render_template, flash, redirect, url_for
from app import app, mongo
from app.forms import LoginForm
from flask_babel import _

@app.route('/')
def index():
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
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        mongo.db.user.insert_one({'username': form.username.data})
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))

    users = mongo.db.user.find({})

    print(users)
    return render_template('login.html', title='Sign In', form=form, users = users, message= _("hi"))

@app.errorhandler(404) 
def not_found():
    return("not found")



# @app.route('/static/styles/<path:path>')
# def send_js(path):
#     return send_from_directory('js', path)