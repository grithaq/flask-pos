from extensions import db
import datetime

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    create_at = db.Column(db.DateTime, default=datetime.datetime.now())
    update_at = db.Column(db.DateTime, onupdate=datetime.datetime.now())

    def __repr__(self) -> str:
        return self.name