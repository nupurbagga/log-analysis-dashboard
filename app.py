from flask import Flask,render_template,url_for
from forms import UploadForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ba75c255983c24387fc22ce96a71a507'

#main page
@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

#form uploading page
@app.route('/forms')
def formupload():
    form = UploadForm()
    return render_template('forms.html', title = 'Upload Form', form = form)

if __name__ == '__main__':
    app.run(debug=True)