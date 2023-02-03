from extensions import db
import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(100))
    email = db.Column(db.String(25))
    gender = db.Column(db.String(25))
    is_admin = db.Column(db.Boolean, default=False)
    is_superuser = db.Column(db.Boolean, default=False)
    create_at = db.Column(db.DateTime, default=datetime.datetime.now())
    update_at = db.Column(db.DateTime, onupdate=datetime.datetime.now())

    def __repr__(self) -> str:
        return self.username



    