from bank import app, db
from flask import render_template, request, redirect, url_for
from bank.models import Employee, Account
from bank.forms import RegisterForm


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


@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        # account_to_create = Account(email=form.email_address.data,
        #                             password=form.password1.data)
        # db.session.add(account_to_create)
        # db.session.commit()
        return redirect(url_for("accounts_page"))
    return render_template("register.html", form=form)
