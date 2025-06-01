# Forms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[Length(min=2, max=20)])
    userType = [{"Student", "S"}, ("Faculty", "F")]
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    register = SubmitField("Register Account")

    pass

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[Length(min=2, max=20)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    login = SubmitField("Login")

    pass