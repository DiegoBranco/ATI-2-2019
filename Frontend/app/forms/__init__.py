from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField
from wtforms.fields import TextAreaField
from wtforms.validators import DataRequired, NumberRange

class SignInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')



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