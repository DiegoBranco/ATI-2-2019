from flask_mongoengine.wtf import model_form
from wtforms import validators, SubmitField
from app import mongo
from flask_babel import _


class Media():
    mtype = mongo.StringField()
    content = mongo.StringField()
    pass

class Question():
    question = mongo.StringField()
    qtype =  mongo.StringField()
    pass

class Certificate(mongo.Document):
    # dateCreated
    title = mongo.StringField()
    description = mongo.StringField()
    # pdf url / firm
    pass


class Admin(mongo.Document):
    pass

class User(mongo.Document):
    __name__ = "user"
    username = mongo.StringField(validators=[validators.DataRequired(),], verbose_name=_("Username"))
    password = mongo.StringField(validators=[validators.DataRequired(),])
    listTest = mongo.ListField(mongo.ReferenceField(Certificate))

    # listCert = mongo.ListField(mongo.ReferenceField(Certificate))

    name = mongo.StringField(verbose_name='Name', validators=[validators.DataRequired()])

    lastName = mongo.StringField(verbose_name='Last name', validators=[validators.DataRequired()])

    email = mongo.EmailField("Email", validators=[validators.DataRequired()])

    profileImageUrl = mongo.URLField('https=//www.pondokindahmall.co.id/assets//img/default.png')

    birthDate = mongo.DateField(verbose_name='Birth Date', validators=[validators.DataRequired()])

    gender = mongo.StringField(verbose_name='Gender', choices=[('Male','Male'),('Female','Female')])

    university = mongo.StringField(verbose_name='University/Institution')

    location = mongo.StringField(verbose_name='location')    

    remember_me = mongo.BooleanField()

    admin = mongo.ReferenceField(Admin)

    # submit = SubmitField('Sign Up')

    birthDate = mongo.DateTimeField()

    pass

class Test(mongo.Document):
    idUser = mongo.ReferenceField(User)
    idCertificate = mongo.ReferenceField(Certificate)
    pass


UserFormSignUp = model_form(User, field_args={'password':{'password': True}, "gender":{"radio" : True}})
UserFormSignIn = model_form(User, field_args={'password':{'password': True}})

def GetSignUpForm(form):
    return UserFormSignUp(form)
    pass

def GetSignInForm(form):
    return UserFormSignIn(form)
    pass