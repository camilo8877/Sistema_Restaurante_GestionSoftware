from flask import Blueprint, render_template


reservation_bp = Blueprint("reservations", __name__)


@reservation_bp.route("/reservations")
def reservations():
    return render_template("reservations/reservations.html")
