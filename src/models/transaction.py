from extensions import db
import datetime

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    sales_id = db.Column(db.Integer, db.ForeignKey('sales.id'))
    total = db.Column(db.Integer)
    create_at = db.Column(db.DateTime, default=datetime.datetime.now())
    update_at = db.Column(db.DateTime, onupdate=datetime.datetime.now())

    def __repr__(self) -> str:
        return f'<order:{self.id}>'