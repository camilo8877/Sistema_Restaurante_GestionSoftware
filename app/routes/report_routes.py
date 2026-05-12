from flask import Blueprint, render_template


report_bp = Blueprint("reports", __name__)


@report_bp.route("/reports")
def reports():
    return render_template("reports/reports.html")
