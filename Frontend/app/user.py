from flask_mongoengine.wtf import model_form
from wtforms import SubmitField

from wtforms.validators import DataRequired
from app import mongo
from flask_babel import _
from mongoengine.fields import DateTimeField, IntField, StringField, URLField, ListField, ReferenceField, EmailField, BooleanField

class Media():
    mtype = StringField()
    content = StringField()
    pass

class Question():
    question = StringField()
    qtype =  StringField()
    pass

class Certificate(mongo.Document):
    # dateCreated
    title = StringField()
    description = StringField()
    # pdf url / firm
    pass


class Admin(mongo.Document):
    pass

class User(mongo.Document):
    __name__ = "user"
    username = StringField(validators=[DataRequired(),], verbose_name=_("Username"))
    password = StringField(validators=[DataRequired(),])
    listTest = ListField(ReferenceField(Certificate))

    listCert = ListField(ReferenceField(Certificate))

    name = StringField(verbose_name='Name', validators=[DataRequired()])

    lastName = StringField(verbose_name='Last name', validators=[DataRequired()])

    email = EmailField(verbose_name="Email", validators=[DataRequired()])

    profileImageUrl = URLField()

    # birthDate = DateTimeField(verbose_name='Birth Date', validators=[DataRequired()], )

    gender = StringField(verbose_name='Gender', choices=[('Male','Male'),('Female','Female')])

    university = StringField(verbose_name='University/Institution')

    location = StringField(verbose_name='location')    

    remember_me = BooleanField()

    admin = ReferenceField(Admin)

    # submit = SubmitField('Sign Up')

    birthDate = DateTimeField()

    pass

class Test(mongo.Document):
    idUser = ReferenceField(User)
    idCertificate = ReferenceField(Certificate)
    pass


UserFormSignUp = model_form(User, field_args={'password':{'password': True}, "gender":{"radio" : True}})
UserFormSignIn = model_form(User, field_args={'password':{'password': True}})

def GetSignUpForm(form):
    return UserFormSignUp(form)
    pass

def GetSignInForm(form):
    return UserFormSignIn(form)
    pass