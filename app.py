from flask import Flask,render_template,url_for, flash, redirect
from forms import RegistrationForm, LoginForm, UploadForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ba75c255983c24387fc22ce96a71a507'

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
#form uploading page
@app.route('/forms')
def formupload():
    form = UploadForm()
    return render_template('forms.html', title = 'Upload Form', form = form)'''

if __name__ == '__main__':
    app.run(debug=True)