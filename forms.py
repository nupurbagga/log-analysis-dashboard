from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email
class UploadForm(FlaskForm):
    file = FileField('Upload Log File',
                        validators=[FileRequired(), FileAllowed(["log", "txt"], "Only .log and .txt files are allowed")])
    filetype = SelectField('Log Type',
                        choices=[("apache", "Apache access logs")])
    submitfile = SubmitField('Analyze Log')