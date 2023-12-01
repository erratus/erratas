from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'LOREM_IPSUM'
conn = sqlite3.connect('./instances/OBS.db', check_same_thread=False)
cursor = conn.cursor()
app.app_context().push()

@app.route('/')
def home():
    return render_template('homepage.html', title='Home Page')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()

        if user:
            session['username'] = username
            return redirect(url_for('account'))

    return render_template('login.html', title='Login Page')

@app.route('/account')
def account():
    if 'username' in session:
        username = session['username']

        # Fetch accounts and their balances for the logged-in user
        cursor.execute("SELECT account_no, balance FROM balance WHERE account_no IN (SELECT account_no FROM accounts WHERE username=?)", (username,))
        accounts_info = cursor.fetchall()

        # Fetch transaction history for the user's accounts
        cursor.execute("SELECT * FROM transactions WHERE from_account_no IN (SELECT account_no FROM accounts WHERE username=?) OR to_account_no IN (SELECT account_no FROM accounts WHERE username=?)", (username, username))
        transactions = cursor.fetchall()

        return render_template('account.html', username=username, accounts_info=accounts_info, transactions=transactions)
    
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirmed_password = request.form['confirmpassword']
        country_code = request.form['country']
        phone_number = request.form['phone_number']

        if password != confirmed_password:
            return render_template('register.html', message='Passwords do not match. Please try again.')

        cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)",
                       (username, password, email, name, country_code, phone_number))
        conn.commit()

        return redirect(url_for('add_accounts', username=username))

    return render_template('register.html', message='')

@app.route('/add_accounts/<username>', methods=['GET', 'POST'])
def add_accounts(username):
    if request.method == 'POST':
        bank_name = request.form['bank_name']
        account_no = request.form['account_no']

        if 'action' in request.form:
            if request.form['action'] == 'finish':
                return redirect(url_for('finish_adding_accounts', username=username))

        cursor.execute("INSERT INTO accounts VALUES (?, ?, ?)", (account_no, username, bank_name))
        conn.commit()

    return render_template('add_accounts.html', username=username)

@app.route('/finish_adding_accounts/<username>', methods=['POST'])
def finish_adding_accounts(username):
    bank_name = request.form.get('bank_name')
    account_no = request.form.get('account_no')
    if bank_name and account_no:
        cursor.execute("INSERT INTO accounts VALUES (?, ?, ?)", (account_no, username, bank_name))
        conn.commit()

    return redirect(url_for('success', username=username))

@app.route('/transfer_funds', methods=['POST'])
def transfer_funds():
    if 'username' in session:
        username = session['username']
        from_account = request.form['from_account']
        to_account = request.form['to_account']
        amount = float(request.form['amount'])  # Convert amount to float

        # Fetch current balances of from and to accounts
        cursor.execute("SELECT balance FROM balance WHERE account_no = ?", (from_account,))
        from_balance = cursor.fetchone()[0]
        cursor.execute("SELECT balance FROM balance WHERE account_no = ?", (to_account,))
        to_balance = cursor.fetchone()[0]

        if from_balance >= amount:
            # Update balances
            new_from_balance = from_balance - amount
            new_to_balance = to_balance + amount

            # Update balances in the database
            cursor.execute("UPDATE balance SET balance = ? WHERE account_no = ?", (new_from_balance, from_account))
            cursor.execute("UPDATE balance SET balance = ? WHERE account_no = ?", (new_to_balance, to_account))
            conn.commit()

            # Log transaction in the transactions table
            cursor.execute("INSERT INTO transactions (from_account_no, to_account_no, amount) VALUES (?, ?, ?)", (from_account, to_account, amount))
            conn.commit()

            return redirect(url_for('account'))
        else:
            return "Insufficient balance for the transfer"

    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove username from session
    return redirect(url_for('login'))


@app.route('/withdraw')
def withdraw():
    return render_template('withdraw.html', title='Withdraw Page')

@app.route('/transfer')
def transfer():
    return render_template('transfer.html', title='Transfer Page')

@app.route('/success/<username>')
def success(username):
    return render_template('success.html', username=username)

if __name__ == "__main__":
    app.run(debug=True)
