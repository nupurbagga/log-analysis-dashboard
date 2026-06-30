from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,PasswordField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                        validators = [DataRequired(), Length(min=3,max=20)])
    email = StringField("Email address",
                        validators= [DataRequired(),Email()])
    password = PasswordField("Enter Password",
                        validators = [DataRequired()])
    confirm_password = PasswordField("Confirm Password",
                        validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField("Email address",
                        validators= [DataRequired(),Email()])
    password = PasswordField("Enter Password",
                        validators = [DataRequired()])
    remember = BooleanField("Remember Me")
    submitpass = SubmitField("Login")


class UploadForm(FlaskForm):
    file = FileField('Upload Log File',
                        validators=[FileRequired(), FileAllowed(["log", "txt"], "Only .log and .txt files are allowed")])
    filetype = SelectField('Log Type',
                        choices=[("apache", "Apache access logs")])
    submitfile = SubmitField('Analyze Log')