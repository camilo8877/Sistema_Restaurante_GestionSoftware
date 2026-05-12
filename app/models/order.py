from app import db
from datetime import datetime


class Order(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100))
    status = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

