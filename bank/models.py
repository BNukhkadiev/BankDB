from bank import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """
    Класс Пользователя приложения. Является родителем Client и Employee.
    """
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String)

    def check_password_correction(self, attempted_password):
        if self.password == attempted_password:
            return True


class Client(db.Model):
    """
    Класс таблицы содержащей данные о клиентах банка
    """
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    gender = db.Column(db.Boolean())
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    passport_id = db.Column(db.String())
    birth_date = db.Column(db.Date())
    address = db.Column(db.String())


class BankAccount(db.Model):
    """
    Класс таблицы содержащей данные о счетах клиентов
    """
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    balance = db.Column(db.Float())
    client_id = db.Column(db.Integer, db.ForeignKey(Client.id))


class Transfer(db.Model):
    """
    Класс таблицы содержащей данные о переводах
    """
    id = db.Column(db.Integer(), primary_key=True)
    amount = db.Column(db.Float)
    receiver_id = db.Column(db.Integer, db.ForeignKey(BankAccount.id))
    sender_id = db.Column(db.Integer, db.ForeignKey(BankAccount.id))


class Employee(db.Model):
    """
    Класс таблицы содержащей данные о сотрудниках банка
    """
    id = db.Column(db.Integer(), primary_key=True)
    position = db.Column(db.String(60), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

    def __repr__(self):
        return f"Employee {self.name} {self.position}"


class Credit(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    percentage = db.Column(db.Float(), nullable=False)
    credit_amount = db.Column(db.Float(), nullable=False)
    last_payment_date = db.Column(db.Date(), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey(Employee.id))
    client_id = db.Column(db.Integer, db.ForeignKey(Client.id))


class Journal(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    operation_datetime = db.Column(db.Date())
    table_name = db.Column(db.String())
    operation_id = db.Column(db.ForeignKey(BankAccount.id))
