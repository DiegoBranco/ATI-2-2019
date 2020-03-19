from flask_mongoengine.wtf import model_form
from wtforms import SubmitField

from wtforms.validators import DataRequired, NumberRange
from app import mongo
from flask_babel import _
from mongoengine.fields import DateTimeField, IntField, StringField, URLField, ListField, ReferenceField, EmailField, BooleanField
import datetime


class Answer(mongo.Document):

    pass


class Media(mongo.Document):
    __name__ = "media"
    mtype = StringField()
    content = StringField()
    pass

class Question(mongo.Document):
    __name__ = "question"
    question = StringField()
    qtype =  StringField()
    answer = StringField()
    opcion2 = StringField()
    opcion3 = StringField()
    opcion4 = StringField()
    pass

class Certificate(mongo.Document):
    __name__ = "certificate"
    imgUrl = URLField()
    title = StringField(max_length = 30, verbose_name= "Title", validators=[DataRequired()])
    description = StringField(verbose_name= "Description", validators=[DataRequired()])
    scoreForTrueFalse = IntField(verbose_name= "Score For True False", validators=[DataRequired(), NumberRange(min=0)] )   
    scoreForSimpleSelection = IntField(verbose_name= "Score For Simple Selection", validators=[DataRequired(), NumberRange(min=0)] )  
    numQuestions = IntField(verbose_name= "numQuestions", validators=[DataRequired(), NumberRange(min=0)] )  
    timeForTest = IntField(verbose_name= "timeForTest", validators=[DataRequired(), NumberRange(min=0)] )  
    submit = SubmitField(verbose_name= 'Save Changes')
    dateCreated = DateTimeField(default= datetime.datetime.utcnow)
    listQuestion = ListField(ReferenceField(Question))
    listQuestionActive = ListField(ReferenceField(Question))
    approvalScore = IntField()

    def clean(self):
        print(self.scoreForSimpleSelection)
        # self.scoreForTrueFalse = int(self.scoreForTrueFalse.data)
        # self.scoreForSimpleSelection = int(self.scoreForSimpleSelection.data)
        # self.numQuestions = int(self.numQuestions.data)
        # self.timeForTest = int(self.timeForTest.data)

    # users = []
    # pdf url / firm
    pass






class Admin(mongo.Document):
    __name__ = "admin"
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
    blocked = BooleanField(default = False)

    admin = ReferenceField(Admin)

    # submit = SubmitField('Sign Up')

    birthDate = DateTimeField()

    pass

class Test(mongo.Document):
    __name__ = "test"
    userId = ReferenceField(User)
    certificateId = ReferenceField(Certificate)
    listQuestion = ListField(ReferenceField(Question))
    timeCreated = DateTimeField(default= datetime.datetime.utcnow)
    timeUserEnds = DateTimeField()
    scoreForSimpleSelection = IntField()
    scoreForTrueFalse = IntField()
    # timeForTest =
    # timeEnd = 
    approvalScore = IntField()
    answers = ListField(ReferenceField(Question))
    pass


UserFormSignUp = model_form(User, field_args={'password':{'password': True}, "gender":{"radio" : True}})
UserFormSignIn = model_form(User, field_args={'password':{'password': True}})

CertificateForm = model_form(Certificate)

def GetSignUpForm(form):
    return UserFormSignUp(form)

def GetSignInForm(form):
    return UserFormSignIn(form)

def GetCertificateForm(form):
    return CertificateForm(form)
