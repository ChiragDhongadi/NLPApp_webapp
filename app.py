from flask import Flask, render_template,request,redirect,session
from db import DataBase
import api

app = Flask(__name__)
app.secret_key = "fj39fjk4@!kfj3948fj!kfd"

dbo = DataBase()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response = dbo.insert(name,email,password)

    if response:
        return render_template('login.html',message="Registration Successful. Kindly login to proceed.")
    else:
        return render_template('register.html',message="Email already exists")

@app.route('/perform_login',methods=['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response = dbo.search(email,password)

    if response:
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('login.html',message='Incorrect email/password')

@app.route('/profile')
def profile():
    if session:
        return render_template('profile.html')
    else:
        return redirect('/')

@app.route('/ner')
def ner():
    if session:
        return render_template('ner.html')
    else:
        return redirect('/')

@app.route('/perform_ner',methods=['post'])
def perform_ner():
    if session:
        text = request.form.get('ner_text')
        response = api.ner(text)
        return render_template('ner.html',response=response)
    else:
        return redirect('/')

@app.route('/sentiment')
def sentiment():
    if session:
        return render_template('sentiment.html')
    else:
        return redirect('/')

@app.route('/perform_sentiment',methods=['POST'])
def perform_sentiment():
    if session:
        text = request.form.get('sentiment_text')
        response = api.sentiment_analysis(text)
        return render_template('sentiment.html',response=response)
    else:
        return redirect('/')

@app.route('/language')
def language():
    if session:
        return render_template('language.html')
    else:
        return redirect('/')

@app.route('/perform_language',methods=['POST'])
def perform_language():
    if session:
        text = request.form.get('language_text')
        response = api.language_detection(text)
        print(response)
        return render_template('language.html',response=response)
    else:
        return redirect('/')


app.run(debug=True)
