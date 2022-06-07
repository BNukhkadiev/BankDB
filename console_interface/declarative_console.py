from sqlalchemy import create_engine, inspect
from sqlalchemy import select, delete
from sqlalchemy import Column, Integer, Float, ForeignKey, String, Date, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

from prettytable import PrettyTable

engine = create_engine("sqlite:///../bank/bank.db")
Base = declarative_base()
Session = sessionmaker(engine)
inspector = inspect(engine)


class Journal(Base):
    __tablename__ = "journal_account"
    id = Column(Integer, primary_key=True, autoincrement=True)
    operation_datetime = Column(Date)
    table_name = Column(String)
    operation_id = Column(ForeignKey("bank_account.id"))


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)


class BankAccount(Base):
    __tablename__ = "bank_account"
    id = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Float, nullable=False)
    client_id = Column(ForeignKey("client.id"))

    def __repr__(self):
        return f"<Bank Account> {self.email}"


class Credit(Base):
    __tablename__ = "credit"
    id = Column(Integer, primary_key=True, autoincrement=True)
    percentage = Column(Float)
    credit_amount = Column(Float)
    last_payment_date = Column(Date)
    employee_id = Column(ForeignKey("employee.id"))
    client_id = Column(ForeignKey("client.id"))


class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True, autoincrement=True)
    position = Column(String)
    user_id = Column(ForeignKey("user.id"))


class Transfer(Base):
    __tablename__ = "transfer"
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    sender_id = Column(ForeignKey("bank_account.id"))
    receiver_id = Column(ForeignKey("bank_account.id"))


class Client(Base):
    __tablename__ = "client"
    id = Column(Integer, primary_key=True, autoincrement=True)
    gender = Column(Boolean)
    user_id = Column(ForeignKey("user.id"))
    passport_id = Column(String)
    birth_date = Column(Date)
    address = Column(String)


# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


def add_values(id, name, email, password):
    with Session.begin() as session:
        user_record = User(
            id=id,
            name=name,
            email=email,
            password=password
        )
        session.add(user_record)


def get_values():
    with Session.begin() as session:
        select_statement = select(User)
        result = session.execute(select_statement)

        x = PrettyTable()
        x.field_names = ["id", "balance", "email", "password"]
        for row in result.scalars():
            x.add_row([row.id, row.name, row.email, row.password])
        print(x)


def delete_values(value):
    with Session.begin() as session:
        delete_statement = delete(User).where(User.email == value)
        result = session.execute(delete_statement)


def search_values(values):
    with Session.begin() as session:
        select_statement = select(User).where(User.email.in_(values))
        result = session.execute(select_statement)
        x = PrettyTable()
        x.field_names = ["id", "name", "email", "password"]
        for row in result.scalars():
            x.add_row([row.id, row.name, row.email, row.password])
        print(x)


def print_table_names():
    print("Available tables:", "; ".join(inspector.get_table_names()))


# add_values(1, "Spongebob", "spongy@mail", "123")
# add_values(2, "Sandy", "sandy@mail", "432")
# add_values(3, "Patrick", "patrick@mail", "2365")
# add_values(4, "Squidward", "squidward@mail", "324")
#
# get_values()

# delete_values("spongy@mail")
#
# get_values()

# search_values("patrick@mail", "krabs@mail")
# get_values()


while True:
    option = input("Choose an option:\n"
                   "1. Add new values\n"
                   "2. Delete values\n"
                   "3. Print table\n"
                   "4. Search by condition\n"
                   "5. Print table names\n")
    if len(option) == 0:
        break

    if option == "5":
        print_table_names()
    # table_name = input("Table name: ")
    if option == "1":
        # values = input("Values: ").split()
        id = int(input("id: "))
        name = input("name:")
        email = input("email:")
        password = input("password:")
        add_values(id, name, email, password)
    if option == "2":
        condition = input("Condition: ")
        delete_values(condition)
    if option == "3":
        get_values()
    if option == "4":
        condition = input("Condition: ").split()
        # print(condition)
        # print(type(condition))
        search_values(condition)

