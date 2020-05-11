from flask import render_template
from application import app
from application.models import Posts


@app.route('/')
@app.route('/home')
def home():
    blogData = Posts.query.first()
    return render_template('home.html', title='Home Page', posts=blogData)

@app.route('/about')
def about():
    return render_template('about.html', title='About Page')

@app.route('/login')
def login():
    return render_template('login.html', title='Login Page')

@app.route('/register')
def register():
    return render_template('register.html', title='Register Page')
