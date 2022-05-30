from sqlalchemy.engine import result
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Column, Integer, Float, ForeignKey, String, Date, Table
from sqlalchemy import select, text, inspect
from prettytable import PrettyTable, from_db_cursor

# establish connections
engine = create_engine("sqlite:///../bank/bank.db")
inspector = inspect(engine)


# initialize the Metadata Object
# meta = MetaData(bind=engine)


# MetaData.reflect(meta)


# create a table schema
class Account:
    __table__ = "account"
    id = Column(Integer, primary_key=True)
    balance = Column(Float, nullable=False)
    client_id = Column(Integer, ForeignKey("client.id"))
    email = Column(String)
    password = Column(String)


class Credit:
    __table__ = "credit"
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey("employee.id"))
    client_id = Column(Integer, ForeignKey("client.id"))
    percentage = Column(Float)
    credit_amount = Column(Float)
    last_payment_date = Column(Date)


class Employee:
    __table__ = "employee"


class Transfer:
    __table__ = "transfer"


class Client:
    __table__ = "client"


def add_values(table_name, *values):
    values = tuple(values)
    query = f"INSERT INTO {table_name} VALUES {values}"
    with engine.begin() as connection:
        connection.execute(text(query))
    print(values)


def select_table(table_name):
    query = f"SELECT * FROM {table_name}"
    with engine.begin() as connection:
        rows = connection.execute(text(query)).all()
    x = PrettyTable()
    x.field_names = rows[0]._mapping.keys()
    x.add_rows(rows)
    print(x)


def delete_from_table(table_name, condition):
    query = f"DELETE FROM {table_name} WHERE {condition}"
    with engine.begin() as connection:
        connection.execute(text(query))


def search_values(table_name, condition):
    query = f"SELECT * FROM {table_name} WHERE {condition}"
    with engine.begin() as connection:
        rows = connection.execute(text(query)).all()
    x = PrettyTable()
    x.field_names = rows[0]._mapping.keys()
    x.add_rows(rows)
    print(x)


def print_table_names():
    print("Available tables:", "; ".join(inspector.get_table_names()))


while True:
    option = input("Choose an option:\n"
                   "1. Add new values\n"
                   "2. Delete values\n"
                   "3. Print table\n"
                   "4. Search by condition\n"
                   "5. Print table names\n")
    if len(option) == 0:
        break

    table_name = input("Table name: ")

    if option == "1":
        values = input("Values: ").split()
        add_values(table_name, *values)
    if option == "2":
        condition = input("Condition: ")
        delete_from_table(table_name, condition)
    if option == "3":
        select_table(table_name)
    if option == "4":
        condition = input("Condition: ")
        search_values(table_name, condition)
    if option == "5":
        print_table_names()
