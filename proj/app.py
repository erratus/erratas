from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html',title='Home Page')

@app.route('/login')
def login():
    return render_template('login.html',title='login Page')

@app.route('/register')
def register():
    return render_template('register.html',title='register Page')

@app.route('/withdraw')
def withdraw():
    return render_template('withdraw.html',title='withdraw Page')

@app.route('/transfer')
def transfer():
    return render_template('transfer.html',title='transfer Page')


if __name__=="__main__":
    app.run(debug=True)