from flask import render_template,url_for, flash, redirect, request
from app import app, db, bcrypt
from flask_login import login_required
from app.forms import RegistrationForm, LoginForm, UploadForm
from app.models import User, Logs
from flask_login import login_user, current_user, logout_user, login_required


#main page
@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


#signup page
@app.route('/register', methods = ['GET', 'POST'])
def reg():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():     #
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            nextpg = request.args.get('next')
            return redirect(nextpg) if nextpg else redirect(url_for('index'))
        else:
            flash("Login Failed. Please try again", 'danger')
        
    return render_template('login.html', title = 'User Login', form = form)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/account')
@login_required
def account():
    return render_template('account.html', title = 'Account')

'''
#dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    form = Dashboard()
    return render_template('dashb.html', title = 'Dashboard Page', form = form)'''
