from bank import db


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

    def __repr__(self):
        return f"Employee {self.name}"


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
