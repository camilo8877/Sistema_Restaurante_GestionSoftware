from app import db


class Reservation(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100))
    reservation_date = db.Column(db.String(50))
    reservation_time = db.Column(db.String(50))