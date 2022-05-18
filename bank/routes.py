from bank import app
from flask import render_template, request
from bank.models import Employee


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


@app.route("/employees")
def employees_page():
    employees = Employee.query.all()
    return render_template('employees.html', employees=employees)

# @app.route("/register", methods=["POST"])
# def register():
#     name = request.args.get("name")
#     dorm = request.args.get("dorm")
#
