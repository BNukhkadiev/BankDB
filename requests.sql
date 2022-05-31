CREATE TABLE transfer(
    transfer_id INTEGER PRIMARY KEY,
    account_id INTEGER,
    employee_id INTEGER,
    receiver_account_id INTEGER,
    transfer_amount FLOAT,
    FOREIGN KEY(employee_id) REFERENCES employee(id),
    FOREIGN KEY(account_id) REFERENCES account(id),
    FOREIGN KEY(receiver_account_id) REFERENCES account(id));

CREATE TABLE journal_account (
operation_datetime DATETIME,
operation_type VARCHAR(20),
table_name VARCHAR(20),
operation_id INT);


CREATE TABLE account (
        id INTEGER PRIMARY KEY,
        balance FLOAT NOT NULL,
        client_id INTEGER,
        FOREIGN KEY(client_id) REFERENCES client(id)
);
CREATE TRIGGER account_log AFTER INSERT
ON account
BEGIN
INSERT INTO journal_account(operation_datetime, operation_type, table_name, operation_id) VALUES (DATETIME("now", "localtime"), "INSERT", "account", new.id);
END;

CREATE TABLE credit (
        id INTEGER NOT NULL,
        employee_id INTEGER,
        client_id INTEGER,
        percentage FLOAT NOT NULL,
        credit_amount FLOAT NOT NULL,
        last_payment_date DATE NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(employee_id) REFERENCES employee (id),
        FOREIGN KEY(client_id) REFERENCES client (id)
);

CREATE TABLE employee (
        id INTEGER PRIMARY KEY (id),
        name VARCHAR(225) NOT NULL,
        position VARCHAR(60),
);

CREATE TABLE transfer(
    transfer_id INTEGER PRIMARY KEY,
    account_id INTEGER,
    employee_id INTEGER,
    receiver_account_id INTEGER,
    transfer_amount FLOAT,
    FOREIGN KEY(employee_id) REFERENCES employee(id),
    FOREIGN KEY(account_id) REFERENCES account(id),
    FOREIGN KEY(receiver_account_id) REFERENCES account(id));

CREATE TABLE client (
        id INTEGER PRIMARY KEY,
        name VARCHAR(30) NOT NULL,
        gender BOOL,
        birth_date DATE,
        passport_number CHAR(10),
        address VARCHAR(225));


INSERT INTO account VALUES (1, 500, 1);
INSERT INTO account VALUES (2, 300, 1);
INSERT INTO account VALUES (3, 700, 1);


INSERT INTO client VALUES (1, "Pavel", 0, "1999-05-24", "1234382345", "Wall Street");
INSERT INTO client VALUES (2, "Ivan", 0, "1996-05-24", "3898982835", "Baker Street");
INSERT INTO client VALUES (3, "Billy", 0, "2000-05-24", "0725489613", "Sesame Street");
INSERT INTO client VALUES (4, "Jimmy", 0, "2001-05-24", "948274561", "21 Street");
INSERT INTO client VALUES (5, "Kate", 1, "1980-05-24", "7392816472", "Wall Street");


INSERT INTO account VALUES (1, 500, 1);
INSERT INTO account VALUES (2, 1233, 2);
INSERT INTO account VALUES (3, 825, 3);
INSERT INTO account VALUES (4, 420, 4);
INSERT INTO account VALUES (5, 8097, 5);


UPDATE account SET email = "mymail" || id || "@domen.com";

