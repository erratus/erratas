from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# DataFrames to store user and account information
accounts_df = pd.DataFrame(columns=['username', 'bank_name', 'account_no'])
user_df = pd.DataFrame(columns=['username', 'password', 'email', 'name', 'country', 'phone_number'])

@app.route('/')
def home():
    return render_template('homepage.html', title='Home Page')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check for username and pass existence
        if (username in user_df['username'].values) and (password in user_df.loc[user_df['username'] == username, 'password'].values):
            # redirect in case of a match
            return redirect(url_for('account'))

    # If login fails show the login page
    return render_template('login.html', title='Login Page')

@app.route('/account')
def account():
    return render_template('account.html', title='Account Page')

@app.route('/test')
def test():
    print(accounts_df)
    print(user_df)
    return render_template('test.html', title='test Page')

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

        # Checking for pass=confirmed pass or not (backup can be removed)
        if password != confirmed_password:
            print('Passwords do not match')
            return render_template('register.html', message='Passwords do not match. Please try again.')

        # Check for username existence
        if username in user_df['username'].values:
            print('Username already exists')
            return render_template('register.html', message='Username already exists')

        # Appending data to user_df
        user_df.loc[len(user_df)] = [username, confirmed_password, email, name, country_code, phone_number]
        print(user_df)

        # Redirecting to add_accounts if appending success
        return redirect(url_for('add_accounts', username=username))

    # Redirecting to register page if any error is returned
    return render_template('register.html', message='')

@app.route('/add_accounts/<username>', methods=['GET', 'POST'])
def add_accounts(username):
    if request.method == 'POST':
        bank_name = request.form['bank_name']
        account_no = request.form['account_no']

        # Check if the 'action' key is present in the form data
        if 'action' in request.form:
            # Check the value of the 'action' key
            if request.form['action'] == 'finish':
                # Redirect to 'finish_adding_accounts' endpoint
                return redirect(url_for('finish_adding_accounts', username=username))

        # If 'action' key is not present or not equal to 'finish', append data to accounts_df
        accounts_df.loc[len(accounts_df)] = [username, bank_name, account_no]

    # Render the same page for further data entry
    return render_template('add_accounts.html', username=username)

@app.route('/finish_adding_accounts/<username>', methods=['GET', 'POST'])
def finish_adding_accounts(username):
    return redirect(url_for('success', username=username))

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
