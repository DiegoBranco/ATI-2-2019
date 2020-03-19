
from flask import render_template, flash, redirect, url_for, request, jsonify, session
from app import app, mongo
from app.forms import CertificateForm, QuestionCreateForm
from flask_babel import _
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mongoengine.wtf import model_form
from functools import wraps

from .user import (
    User, GetSignInForm, GetSignUpForm, 
    Certificate, GetCertificateForm,
    Test,
    Question
)
import datetime

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session['userId'] is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/perfil/<string:userID>')
def perfil(userID):
    user = User.objects.get_or_404(id=userID)
    certificates=[]
    return render_template('perfil.html', user=user, certificate=certificates)


@app.route('/')
def index():
    cursos = Certificate.objects[:5]
    clientes=['Google', 'Platzi', 'Yahoo', 'Bing']
    return render_template('index.html', title="ATI te educamos", cursos=cursos, clientes=clientes)

@app.route('/details/<string:courseId>', methods=['GET'])
def course_details(courseId):
    course = Certificate.objects.get_or_404(id= courseId)
    return render_template('details.html', title='Details', course=course)

@app.route('/editor/<string:courseId>', methods=['GET', 'POST'])
def course_editor(courseId):
    form = GetCertificateForm(request.form)

    course = Certificate.objects.get_or_404(id=courseId)

    if form.validate_on_submit():
        course.title = form.title.data
        course.description = form.description.data
        course.numQuestions = form.numQuestions.data
        course.timeForTest = form.timeForTest.data
        course.scoreForTrueFalse = form.scoreForTrueFalse.data
        course.scoreForSimpleSelection = form.scoreForSimpleSelection.data
        course.save()
        print("saved the course")
    else:
        print(form.errors)

    return render_template('editor.html', title='Editor', course=course, form=form)


@app.route('/block/<string:userId>')
def toggleBlock(userId):
    user = User.objects.get_or_404(id=userId)

    if user['blocked']:
        user.blocked = False
    else:
        user.blocked = True

    user.save()
    return redirect(url_for('perfil', userID = userId))


@app.route('/sign-out')
def signOut():
    session.clear()
    return redirect(url_for('index'))

@app.route('/sign-in', methods=['GET', 'POST'])
def signInGet():
    form = GetSignInForm(request.form)

    if form.username.validate(form) and form.password.validate(form):

        user = User.objects(username__exact=form.username.data)[0]
        
        if check_password_hash(user.password, form.password.data ):
            session['user'] = user
            session['userId'] = str(user.id)
            return redirect(url_for('home'))   
        else:
            flash("Couldn't log you in")

            
    else:
        print(form.errors)



    return render_template('sign-in.html', title='Sign In', form=form, message= _("hi"))

@app.route('/sign-up', methods=['GET', 'POST'])
def signUp():
    form = GetSignUpForm(request.form)

    if form.validate_on_submit():
        user = User(
            listTest= [],
            listCert= [],
            name= form.name.data,
            lastName= form.lastName.data,
            email= form.email.data,
            username= form.username.data,
            password= generate_password_hash(form.password.data),
            profileImageUrl= 'https://www.pondokindahmall.co.id/assets//img/default.png',
            # birthDate= fromtimestamp(form.birthDate.data),
            gender= form.gender.data,
            university= form.university.data,
            location= form.location.data
        )
        user.save()
        
        flash('Signup requested for user {}'.format(
            form.username.data))
        print("done inserting")
        return redirect(url_for('index'))

    else:


        print(form.errors)
    # users = mongo.db.user.find({})

    return render_template('sign-up.html', form=form, message= _("hi"))

@app.route('/home')
def home():
    user = session.get('user')
    print(user)
    post = {
        'cursos':{
        'ultimo':{
            'cert':'HTML',
            'description':'Curso introductorio de HTML5'
        },
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
        ]
    }}

    post['cursos']['disponibles']= Certificate.objects[:5]

    return render_template('home.html', title='Home', user=user, post=post)

@app.route('/create-test/<string:courseId>')
@login_required
def create_test(courseId):

    cert = Certificate.objects.get_or_404(id=courseId)
    test = Test()
    test.userId = session['userId']
    test.certificateId = session['courseId']
    test.scoreForSimpleSelection = cert.scoreForSimpleSelection
    test.scoreForTrueFalse = cert.scoreForTrueFalse
    test.approvalScore = cert.approvalScore



    redirect(url_for('test', testId= test.id))
    pass

@app.route('/test/<string:courseId>', methods=['GET', 'POST'])
@login_required
def test(courseId):
    user = {'username':'Miguel'}
    test = {
        'title':'Ruby',
        'time':'20:00',
        'preguntas':[{
            'tipo':'seleccion',
            'codigo':True,
            'pregunta':'Cual es el output del siguiente fragmento de codigo?',
            'opciones':['Hello World!', 'Puts "Hello World!" ','Error','P (World!)'],
            'correcta':'Hello World!',
            'name':'pregunta1'
        },{
        'tipo':'trueFalse',
        'codigo':False,
        'pregunta':'Ruby es un lenguaje fuertemente tipado?',
        'opciones':['Si', 'No'],
        'correcta' : 'Si',
        'name':'pregunta2'
        }]
    }

    return render_template('test.html', title='Certificacion', user=user, test=test)




@app.route('/create-certificate')
def create_certificate():
    cert = Certificate()
    cert.title = _("My awesome certificate title")
    cert.description = _("My awesome certificate description")
    cert.imgUrl = "https://maltawinds.com/wp-content/uploads/2018/10/education-640x360.jpg"

    cert.scoreForTrueFalse = 1
    cert.scoreForSimpleSelection = 2
    cert.numQuestions = 10
    cert.timeForTest = 140

    cert.save()

    return redirect(url_for("course_editor", courseId=cert.id))


@app.errorhandler(404) 
def not_found(error):
    return render_template('404.html')

@app.route('/certificates')
def certs():
    cursos = Certificate.objects[:5]

    return render_template('certs.html', title='Lista de cursos', cursos=cursos)


@app.route('/controlpanel', methods=['GET', 'POST'])
def controlpanel():
    certs = Certificate.objects

    return render_template('controlpanel.html', title='Lista de cursos', certs=certs)


@app.route('/create_question')
def create_question():
    question = Question()
    question.question = _("My awesome question")
    question.qtype = _("My question type")
    question.answer = _("Correct answer")
    question.opcion2 = _("opcion2")
    question.opcion3 = _("opcion3")
    question.opcion4 = _("opcion4")

    question.save()
    return redirect(url_for("questionCreator", questionId=question.id))

@app.route('/questionCreator/<string:questionId>', methods=['GET', 'POST'])
def questionCreator(questionId):
    form = QuestionCreateForm(request.form)

    if form.validate_on_submit():

        if form.typeQuestion.data == "TrueFalse":
            Question.replaceone(
                {_id: questionId},
                {id:questionId,
                question: form.question.data,
                opcionCorrect: form.opcionCorrect.data,
                opcion2: form.opcion2.data}
            )
        else:
            Question.replaceone(
                {_id: questionId},
                {id:questionId,
                question: form.question.data,
                opcionCorrect: form.opcionCorrect.data,
                opcion2: form.opcion2.data,
                opcion3: form.opcion3.data,
                opcion4: form.opcion4.data}
            )
        return redirect(url_for("home"))
    
    return render_template('questionCreator.html', form=form, message= _("hi"))

# @app.route('/static/styles/<path:path>')
# def send_js(path):
#     return send_from_directory('js', path)
