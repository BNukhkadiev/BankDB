from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bank.db"
db = SQLAlchemy(app)


class Client(db.Model):
    """
    Класс таблицы содержащей данные о клиентах банка
    """
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=225), nullable=False)
    gender = db.Column(db.Boolean(), nullable=False)
    passport_number = db.Column(db.String(length=10), nullable=False, unique=True)
    snils = db.Column(db.String(length=11))
    birth_date = db.Column(db.Date())
    address = db.Column(db.String(length=200))


class Account(db.Model):
    """
    Класс таблицы содержащей данные о счетах клиентов
    """
    id = db.Column(db.Integer(), primary_key=True)
    balance = db.Column(db.Float(), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey(Client.id))
    currency = db.String(db.String(length=15))


class Transfer(db.Model):
    """
    Класс таблицы содержащей данные о переводах
    """
    id = db.Column(db.Integer(), primary_key=True)
    receiver_account_id = db.Column(db.Integer, db.ForeignKey(Account.id))
    sender_account_id = db.Column(db.Integer, db.ForeignKey(Account.id))
    transfer_amount = db.Column(db.Float, nullable=False)


class Employee(db.Model):
    """
    Класс таблицы содержащей данные о сотрудниках банка
    """

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(225), nullable=False)


# Добавить эти таблицы (У них не работает Foreign KEy посмотри как это пофиксить в репозитории heelo flask
class Credit(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey(Employee.id))
    client_id = db.Column(db.Integer, db.ForeignKey(Client.id))
    percentage = db.Column(db.Float(), nullable=False)
    credit_amount = db.Column(db.Float(), nullable=False)
    last_payment_date = db.Column(db.Date(), nullable=False)


class Service(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    service_name = db.Column(db.String(225), nullable=False)


class Payment(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    payment_amount = db.Column(db.Float(), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey(Employee.id))
    account_id = db.Column(db.Integer, db.ForeignKey(Account.id))


@app.route('/')
@app.route('/home')
def home_page():
    name = request.args.get('name', 'world')
    return render_template('index.html', name=name)


@app.route("/accounts")
def accounts_page():
    accounts = [
        {'id': 1, 'name': 'Pavel', 'balance': 100},
        {'id': 2, 'name': 'Ivan', 'balance': 200},
        {'id': 3, 'name': 'Brian', 'balance': 5523},
        {'id': 4, 'name': 'Kornelius', 'balance': 3123}
    ]
    return render_template('accounts.html', accounts=accounts)


# @app.route("/register", methods=["POST"])
# def register():
#     name = request.args.get("name")
#     dorm = request.args.get("dorm")
#


if __name__ == "__main__":
    app.run(debug=True)
