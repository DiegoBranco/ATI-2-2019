from flask import render_template, flash, redirect, url_for
from app import app, mongo
from app.forms import SignInForm, SignUpForm, CertificateForm
from flask_babel import _


# Como recibir parametros de url 
# https://stackoverflow.com/questions/7478366/create-dynamic-urls-in-flask-with-url-for

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

@app.route('/perfil')
def perfil():
    user = { 
        'name': 'Fulano',
        'lastname': 'de Tal'
    }
    certificate = [
            {
                'imgUrl': '/static/image/HTML.png',
                'title': 'HTML'
            },
            
            {
                'imgUrl': '/static/image/C++.png',
                'title': 'C++'
            },
            {
                'imgUrl': '/static/image/Python.png',
                'title': 'Python'
            },
            {
                'imgUrl': '/static/image/Ruby.png',
                'title': 'Ruby'
            },
    ]

    return render_template('perfil.html', user=user, certificate=certificate)

@app.route('/')
def index():
    cursos=[
    {
        'cert':'Marketing digital',
        '_id': 'Marketing digital',
        'description':'Descripcion de curso pendiente',
    },
    {
        'cert':'Javascript',
        '_id': 'Javascript',
        'description':'Descripcion de curso pendiente',
    },
    {
        'cert':'ReactJS',
        '_id': 'ReactJS',
        'description':'Descripcion de curso pendiente',
    },
    {
        'cert':'Angular',
        '_id': 'Angular',
        'description':'Descripcion de curso pendiente',
    },
    {
        'cert':'Rails',
        '_id': 'Rails',
        'description':'Descripcion de curso pendiente',
    },
    {
        'cert':'Python',
        '_id': 'Python',
        'description':'Descripcion de curso pendiente',
    }
    ]
    clientes=['Google', 'Platzi', 'Yahoo', 'Bing']
    return render_template('index.html', title="ATI te educamos", cursos=cursos, clientes=clientes)



@app.route('/details/<string:courseId>', methods=['GET'])
def course_details(courseId):
    course = {
        '_id': courseId,
        'dateCreated':'1/Mar/2020',
        'title': 'Principios Basicos de HTML5',
        'description': 'Esta certificacion es sobre la estructura basica para realizar una pagina sencilla en html.',
        'numQuestions': '15 preguntas.',
        'scoreForTrueFalse':'1 punto cada una.',
        'scoreForSimpleSelection':'2 puntos cada una.',
        'timeForTest':'20min.',
        'imgUrl': '/static/image/HTML.png'
    }
    form = CertificateForm()
    return render_template('details.html', title='Details', course=course, form=form)

@app.route('/editor/<string:courseId>', methods=['GET'])
def course_editor(courseId):
    course = {
        '_id': courseId,
        'dateCreated':'1/Mar/2020',
        'title': 'Principios Basicos de HTML5',
        'description': 'Esta certificacion es sobre la estructura basica para realizar una pagina sencilla en html.',
        'numQuestions': '15 preguntas.',
        'scoreForTrueFalse':'1 punto cada una.',
        'scoreForSimpleSelection':'2 puntos cada una.',
        'timeForTest':'20min.',
        'imgUrl': '/static/image/HTML.png'    }
    form = CertificateForm()
    return render_template('editor.html', title='Editor', course=course, form=form)

@app.route('/sign-in', methods=['GET', 'POST'])
def signIn():
    form = SignInForm()
    if form.validate_on_submit():
        # mongo.db.user.insert_one({'username': form.username.data})
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('land'))

    # users = mongo.db.user.find({})

    return render_template('sign-in.html', title='Sign In', form=form, message= _("hi"))


@app.route('/sign-up', methods=['GET', 'POST'])
def signUp():
    form = SignUpForm()
    if form.validate_on_submit():
        mongo.db.user.insert_one({'username': form.username.data})
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('land'))

    users = mongo.db.user.find({})

    return render_template('sign-up.html', form=form, message= _("hi"))

@app.route('/home')
def home():
    user = {'username':'Miguel'}
    post = {
        'cursos':{
        'ultimo':{
        'cert':'HTML',
        'description':'Curso introductorio de HTML5'},
        'terminados':[
            {
                'cert':'Marketing digital',
                'description':'Descripcion de curso pendiente',
                '_id': 'Marketing digital',
            },
            {
                'cert':'Javascript',
                'description':'Descripcion de curso pendiente',
                '_id': 'Javascript',
            },
            {
                'cert':'ReactJS',
                'description':'Descripcion de curso pendiente',
                '_id': 'ReactJS',
            },
            {
                'cert':'Angular',
                'description':'Descripcion de curso pendiente',
                '_id': 'Angular',
            },
            {
                'cert':'Rails',
                'description':'Descripcion de curso pendiente',
                '_id': 'Rails',
            },
            {
                'cert':'Python',
                'description':'Descripcion de curso pendiente',
                '_id': 'Python',
            }
        ],
        'disponibles':[
            {
                'cert':'Ruby',
                'description':'Descripcion de curso pendiente',
                '_id': 'Ruby',
            },
            {
                'cert':'C++',
                'description':'Descripcion de curso pendiente',
                '_id': 'C++',
            },
            {
                'cert':'CSS',
                'description':'Descripcion de curso pendiente',
                '_id': 'CSS',
            }
        ]
    }}
    return render_template('home.html', title='Home', user=user, post=post)

@app.route('/test/<string:courseId>', methods=['GET', 'POST'])
def test(courseId):
    user = {'username':'Miguel'}
    test = {
        'title':'Ruby',
        'time':'20:00',
        'preguntas':[{
        'tipo':'seleccion',
        'codigo':True,
        'pregunta':'¿Cúal es el output del siguiente fragmento de código?',
        'opciones':['Hello World!', 'Puts "Hello World!" ','Error','P (World!)'],
        'correcta':'Hello World!',
        'name':'pregunta1'
    },{
        'tipo':'trueFalse',
        'codigo':False,
        'pregunta':'¿Ruby es un lenguaje fuertemente tipado?',
        'opciones':['Si', 'No'],
        'correcta' : 'Si',
        'name':'pregunta2'
    }]
    }

    return render_template('test.html', title='Certificacion', user=user, test=test)

@app.route('/certs')
def certs():
    cursos=[
    {
        'cert':'Marketing digital',
        '_id': 'Marketing digital',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Javascript',
        '_id': 'Javascript',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'ReactJS',
        '_id': 'ReactJS',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Angular',
        '_id': 'Angular',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Rails',
        '_id': 'Rails',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Python',
        '_id': 'Python',
        'description':'Descripcion de curso pendiente'
    },{
        'cert':'Marketing digital',
        '_id': 'Marketing digital',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Javascript',
        '_id': 'Javascript',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'ReactJS',
        '_id': 'ReactJS',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Angular',
        '_id': 'Angular',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Rails',
        '_id': 'Rails',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Python',
        '_id': 'Python',
        'description':'Descripcion de curso pendiente'
    },{
        'cert':'Marketing digital',
        '_id': 'Marketing digital',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Javascript',
        '_id': 'Javascript',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'ReactJS',
        '_id': 'ReactJS',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Angular',
        '_id': 'Angular',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Rails',
        '_id': 'Rails',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Python',
        '_id': 'Python',
        'description':'Descripcion de curso pendiente'
    },{
        'cert':'Marketing digital',
        '_id': 'Marketing digital',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Javascript',
        '_id': 'Javascript',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'ReactJS',
        '_id': 'ReactJS',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Angular',
        '_id': 'Angular',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Rails',
        '_id': 'Rails',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Python',
        '_id': 'Python',
        'description':'Descripcion de curso pendiente'
    },{
        'cert':'Marketing digital',
        '_id': 'Marketing digital',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Javascript',
        '_id': 'Javascript',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'ReactJS',
        '_id': 'ReactJS',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Angular',
        '_id': 'Angular',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Rails',
        '_id': 'Rails',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Python',
        '_id': 'Python',
        'description':'Descripcion de curso pendiente'
    },{
        'cert':'Marketing digital',
        '_id': 'Marketing digital',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Javascript',
        '_id': 'Javascript',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'ReactJS',
        '_id': 'ReactJS',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Angular',
        '_id': 'Angular',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Rails',
        '_id': 'Rails',
        'description':'Descripcion de curso pendiente'
    },
    {
        'cert':'Python',
        '_id': 'Python',
        'description':'Descripcion de curso pendiente'
    }
    ]
    return render_template('certs.html', title='Lista de cursos', cursos=cursos)

@app.errorhandler(404) 
def not_found():
    return("not found")



# @app.route('/static/styles/<path:path>')
# def send_js(path):
#     return send_from_directory('js', path)