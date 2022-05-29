from sqlalchemy import create_engine
from sqlalchemy import text, inspect
from sqlalchemy import MetaData
from sqlalchemy import select
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import registry
from sqlalchemy.orm import sessionmaker

from prettytable import PrettyTable

from bank.models import Client, Account, Employee

engine = create_engine("sqlite:///bank/bank.db", future=True)
metadata = MetaData()
Session = sessionmaker(bind=engine, future=True)
session = Session()


def select_all(table_name):
    x = PrettyTable()
    with engine.connect() as connection:
        rows = connection.execute(text("select * from employee")).all()
    x.field_names = list(rows._mapping.keys())
    x.add_rows(rows)
    print(x)


# def add():
#     with engine.connect() as connection:
#         connection.execute(
#             text("insert into employee (emp_name) values (:emp_name)"),
#             {"emp_name": "mr. krabs"}
#         )
#         connection.commit()


input("Choose an option:\n"
      "1. Add values\n"
      "2. Print table\n"
      "3. Delete values\n"
      "4. Select rows\n")


def print_tables():
    inspector = inspect(engine)
    for i in inspector.get_table_names():
        print(i)


# print("Available tables: ")
# print_tables()

# print(select())


# print(User.__table__)
# print(select(User.__table__))
#
# spongebob = User(username="spongebob", fullname="Spongebob Squarepants")
# print(spongebob)

# with engine.begin() as connection:
#     mapper_registry.metadata.create_all(connection)
#
# session.add(spongebob)
# print(session.new)

# select_statement = select(User).filter_by(username="spongebob")
# result = session.execute(select_statement)
# print(result)
#
# also_spongebob = result.scalar()
# print(also_spongebob)


# session.add_all([
#     Employee(name="spongebob", position="cook"),
#     Employee(name="squidward", position="manager")
# ])
#
# session.commit()

# result = session.execute(
#     select(User).where(User.username.in_(["spongebob", "fakeuser"]))
# )
#
# print(result.all())
#

# print(User.username == "spongebob")
#
def print_table():
    query = (
        select(Account)
    )

    result = session.execute(query)
    print(result)
    for row in result.scalars():
        print(row)

print_table()

