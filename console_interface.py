import datetime

from bank import db
from bank.models import *


def print_tables():
    for i in db.metadata.tables:
        print(i)


print("Доступные таблицы: ")
print_tables()

table_name = input("Выберите таблицу для взаимодействия: ")
print(db.metadata.tables[table_name])


# cl1 = Client(id=6,


#              name="Igor",
#              gender=0,
#              passport_number="7623178904",
#              birth_date=datetime.date(1999, 5, 16),
#              address="Spooky Street")
# db.session.add(cl1)
# db.session.commit()


# print(type(db.metadata.tables))

