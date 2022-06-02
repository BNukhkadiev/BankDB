from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bank.db"
app.config["SECRET_KEY"] = "d7c615534bbcde839281364b"
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
from bank import routes
