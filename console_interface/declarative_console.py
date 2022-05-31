from sqlalchemy import create_engine, inspect
from sqlalchemy import select, delete
from sqlalchemy import Column, Integer, Float, ForeignKey, String, Date, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

from prettytable import PrettyTable

engine = create_engine("sqlite:///tryout.db")
Base = declarative_base()
Session = sessionmaker(engine)
inspector = inspect(engine)


class Account(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True)
    balance = Column(Float, nullable=False)
    client_id = Column(ForeignKey("client.id"))
    email = Column(String)
    password = Column(String)

    def __repr__(self):
        return f"<Account> {self.email}"


class Credit(Base):
    __tablename__ = "credit"
    id = Column(Integer, primary_key=True)
    employee_id = Column(ForeignKey("employee.id"))
    client_id = Column(ForeignKey("client.id"))
    percentage = Column(Float)
    credit_amount = Column(Float)
    last_payment_date = Column(Date)


class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)


class Transfer(Base):
    __tablename__ = "transfer"
    transfer_id = Column(Integer, primary_key=True)
    account_id = Column(ForeignKey("account.id"))
    reciever_account_id = Column(ForeignKey("account.id"))
    transfer_amount = Column(Float)


class Client(Base):
    __tablename__ = "client"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    gender = Column(Boolean)
    birth_date = Column(Date)
    passport_number = Column(String)
    address = Column(String)


Base.metadata.create_all(engine)


def add_values(id, balance, client_id, email, password):
    with Session.begin() as session:
        account_record = Account(
            id=id,
            balance=balance,
            client_id=client_id,
            email=email,
            password=password
        )
        session.add(account_record)


def get_values():
    with Session.begin() as session:
        select_statement = select(Account).where(Account.email.in_(["patrick@mail", "spongy@mail"]))
        result = session.execute(select_statement)

        x = PrettyTable()
        x.field_names = ["id", "balance", "client_id", "email", "password"]
        for row in result.scalars():
            x.add_row([row.id, row.balance, row.client_id, row.email, row.password])
        print(x)


def delete_values(key, value):
    with Session.begin() as session:
        delete_statement = delete(Account).where(Account.email == value)
        result = session.execute(delete_statement)


def search_values(*values):
    with Session.begin() as session:
        select_statement = select(Account).where(Account.email.in_(values))
        result = session.execute(select_statement)
        x = PrettyTable()
        x.field_names = ["id", "balance", "client_id", "email", "password"]
        for row in result.scalars():
            x.add_row([row.id, row.balance, row.client_id, row.email, row.password])
        print(x)


def print_table_names():
    print("Available tables:", "; ".join(inspector.get_table_names()))


add_values(1, 0, 1, "spongy@mail", "123")
# add_values(2, 0, 2, "sandy@mail", "321")
# add_values(3, 0, 2, "patrick@mail", "321")
# add_values(4, 0, 2, "krabs@mail", "321")
# add_values(5, 0, 2, "squidward@mail", "321")

get_values()

delete_values("email", "spongy@mail")

get_values()

search_values("patrick@mail", "krabs@mail")
# get_values()
