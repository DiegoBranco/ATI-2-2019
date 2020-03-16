from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField, RadioField
from wtforms.fields import TextAreaField
from wtforms.validators import DataRequired, NumberRange
from wtforms.fields.html5 import EmailField, DateField

class SignInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    lastName = StringField('Last name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    birthDate = DateField('Birth Date', validators=[DataRequired()])
    mail = EmailField("Email", validators=[DataRequired()])
    gender = RadioField('Gender', choices=[('Male','Male'),('Female','Female')])
    university = StringField('University/Institution')
    location = StringField('location')    
    submit = SubmitField('Sign Up')



class CertificateForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    scoreForTrueFalse = IntegerField("Score For True False", validators=[DataRequired(), NumberRange(min=0)] ) 
    scoreForSimpleSelection = IntegerField("Score For Simple Selection", validators=[DataRequired(), NumberRange(min=0)] )
    numQuestions = IntegerField("numQuestions", validators=[DataRequired(), NumberRange(min=0)] )
    timeForTest = StringField("timeForTest", validators=[DataRequired(), NumberRange(min=0)] )
    submit = SubmitField('Save Changes')
    

class QuestionTFForm(FlaskForm):

    description = TextAreaField("Description", validators=[DataRequired()])

    submit = SubmitField('Save Changes')



# class Question4