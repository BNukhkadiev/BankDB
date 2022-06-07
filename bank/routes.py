from bank import app, db
from flask import render_template, request, redirect, url_for, flash
from bank.models import Employee, BankAccount, Transfer, Client, Credit, User
from bank.forms import RegisterForm, LoginForm, TransferForm, UserToDelete
from flask_login import login_user, logout_user, login_required
from wtforms import Label

@app.route('/')
@app.route('/home')
def home_page():
    name = request.args.get('name', 'world')
    return render_template('index.html', name=name)


@app.route("/accounts")
@login_required
def accounts_page():
    accounts = BankAccount.query.all()
    return render_template('accounts.html', accounts=accounts)


@app.route("/employees")
@login_required
def employees_page():
    employees = Employee.query.all()
    return render_template('employees.html', employees=employees)


@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        account_to_create = User(name=form.username.data,
                                 email=form.email_address.data,
                                 password=form.password1.data)
        db.session.add(account_to_create)
        db.session.commit()
        return redirect(url_for("login_page"))
    if form.errors != {}:  # if there are no errors
        for err_msg in form.errors.values():
            print(f"Error: {err_msg}")
    return render_template("register.html", form=form)


@app.route('/transfer')
@login_required
def transfer_page():
    transfers = Transfer.query.all()
    return render_template("transfer.html", transfers=transfers)


@app.route('/clients')
@login_required
def clients_page():
    clients = Client.query.all()
    return render_template("clients.html", clients=clients)


@app.route('/users')
@login_required
def users_page():
    users = User.query.all()
    return render_template("users.html", users=users)


@app.route('/login', methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(name=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            print(f"Success! You are logged in as {attempted_user.name}")
            return redirect(url_for('users_page'))
        else:
            print("Username and password do not match. ")

    return render_template("login.html", form=form)


@app.route("/logout")
def logout_page():
    logout_user()
    print("You have been logged out")
    return redirect(url_for("home_page"))


def delete_transfer():
    print("deleting transfer")


@app.route("/new_transfer", methods=["GET", "POST"])
@login_required
def new_transfer_page():
    form = TransferForm()
    if form.validate_on_submit():
        transfer_to_create = Transfer(sender_id=form.sender_id.data,
                                      receiver_id=form.receiver_id.data,
                                      amount=form.amount.data)
        db.session.add(transfer_to_create)
        db.session.commit()
        return redirect(url_for("transfer_page"))

    return render_template("new_transfer.html", form=form)


@app.route("/delete_transfer", methods=["GET", "POST"])
@login_required
def delete_transfer_page():
    form = TransferForm()
    form.submit.label = Label(form.submit.id, "Delete transfer")
    if form.validate_on_submit():
        transfer_to_delete = Transfer.query.filter_by(sender_id=form.sender_id.data,
                                                      receiver_id=form.receiver_id.data,
                                                      amount=form.amount.data).first()
        db.session.delete(transfer_to_delete)
        db.session.commit()
        return redirect(url_for("transfer_page"))

    return render_template("delete_transfer.html", form=form)


@app.route("/delete_user", methods=["GET", "POST"])
@login_required
def delete_user_page():
    form = UserToDelete()
    if form.validate_on_submit():
        user_to_delete = User.query.filter_by(email=form.email.data).first()
        print(user_to_delete)
        if user_to_delete:
            db.session.delete(user_to_delete)
            db.session.commit()
        return redirect(url_for("users_page"))

    return render_template("delete_user.html", form=form)
