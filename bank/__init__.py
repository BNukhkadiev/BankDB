from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bank.db"
app.config["SECRET_KEY"] = "d7c615534bbcde839281364b"
db = SQLAlchemy(app)

from bank import routes
