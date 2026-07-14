import datetime
from app import db,loginmngr
from flask_login import UserMixin

@loginmngr.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    uid = db.Column(db.Integer, primary_key = True )
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.username}')"


class Logs(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    filename = db.Column(db.String(100), nullable = False )
    upload_date = db.Column(db.DateTime, default = datetime.timezone.utc)
    analysis = db.Column(db.Text)
    raw = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('uid'), nullable = False)

    def __repr__(self):
        return f"Log('{self.filename}', '{self.upload_date}')"
    
