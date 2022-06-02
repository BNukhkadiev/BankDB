from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired


class RegisterForm(FlaskForm):
    username = StringField(label="User Name:", validators=[Length(min=1, max=30), DataRequired()])
    email_address = StringField(label="Email Address:", validators=[Email(), DataRequired()])
    password1 = PasswordField(label="Password:")
    password2 = PasswordField(label="Confirm Password:", validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label="Create Account")


class LoginForm(FlaskForm):
    username = StringField(label="User Name", validators=[DataRequired()])
    password = StringField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Sign in")
