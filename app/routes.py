from flask import render_template,url_for, flash, redirect
from app import app, db, bcrypt
from flask_login import login_required
from app.forms import RegistrationForm, LoginForm, UploadForm

from app.models import User, Logs

#main page
@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


#signup page
@app.route('/register', methods = ['GET', 'POST'])
def reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pswd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_pswd)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', category='success')
        return redirect(url_for('index'))
    return render_template('register.html', title = 'Register User', form = form)


#login page
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():     #
        flash("You are now logged in", 'success ')
        return redirect(url_for('index'))
    return render_template('login.html', title = 'User Login', form = form)

'''
#dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    form = Dashboard()
    return render_template('dashb.html', title = 'Dashboard Page', form = form)'''
