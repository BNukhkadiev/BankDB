from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FloatField, BooleanField, DateField
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


class TransferForm(FlaskForm):
    sender_id = IntegerField(label="Sender ID", validators=[DataRequired()])
    receiver_id = IntegerField(label="Receiver ID: ", validators=[DataRequired()])
    amount = FloatField(label="Amount: ", validators=[DataRequired()])
    submit = SubmitField(label="Transfer Money")


class UserToDelete(FlaskForm):
    email = StringField(label="Email Address:", validators=[DataRequired()])
    submit = SubmitField(label="Delete User")


class NewClient(FlaskForm):
    gender = BooleanField(label="Gender:", validators=[DataRequired()])
    user_id = IntegerField(label="User ID:", validators=[DataRequired()])
    birthday = DateField(label="Birthday:", validators=[DataRequired()])
    address = StringField(label="Address:", validators=[DataRequired()])
    submit = SubmitField(label="Create Client")
