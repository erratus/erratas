from flask import Flask,render_template,request
import pandas as pd
app = Flask(__name__)

user_df = pd.DataFrame(columns=['username', 'password', 'email', 'name', 'country', 'phone_number'])

@app.route('/')
def home():
    return render_template('homepage.html',title='Home Page')

@app.route('/login')
def login():
    return render_template('login.html',title='login Page')

@app.route('/test')
def test():
    print(user_df)
    return render_template('test.html',title='test Page')

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        global user_df
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirmed_password = request.form['confirmpassword'] 
        country_code = request.form['country']
        phone_number = request.form['phone_number']

        if password != confirmed_password:
            print('Passwords do not match')
            return render_template('register.html', message='Passwords do not match. Please try again.')

        if username in user_df['username'].values:
            print('Username already exists')
            return render_template('register.html', message='Username already exists')

        user_df.loc[len(user_df)] = [username, confirmed_password, email, name, country_code, phone_number]
        print(user_df)

        return render_template('success.html', name=name)

    return render_template('register.html', message='')


@app.route('/withdraw')
def withdraw():
    return render_template('withdraw.html',title='withdraw Page')

@app.route('/transfer')
def transfer():
    return render_template('transfer.html',title='transfer Page')


if __name__=="__main__":
    app.run(debug=True)
