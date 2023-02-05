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


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, unique=True)
    first_name = db.Column(db.db.String(50))
    last_name = db.Column(db.db.String(50))
    address = db.Column(db.db.String(50))
    phone_number = db.Column(db.db.String(50))
    create_at = db.Column(db.DateTime, default=datetime.datetime.now())
    update_at = db.Column(db.DateTime, onupdate=datetime.datetime.now())

    def __repr__(self) -> str:
        return f'<customer:{self.first_name}>'


class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.db.String(50))
    last_name = db.Column(db.db.String(50))
    address = db.Column(db.db.String(50))
    phone_number = db.Column(db.db.String(50))
    nik = db.Column(db.db.String(15))
    create_at = db.Column(db.DateTime, default=datetime.datetime.now())
    update_at = db.Column(db.DateTime, onupdate=datetime.datetime.now())

    def __repr__(self) -> str:
        return f'<sales: {self.first_name}>'