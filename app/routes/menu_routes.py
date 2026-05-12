from flask import Blueprint, render_template, request, redirect
from app.models.menu import Menu
from app import db

menu_bp = Blueprint("menu", __name__)
# from flask import Blueprint, render_template, request, redirect
# from app.models.menu import Menu
# from app import db


menu_bp = Blueprint("menu", __name__)


@menu_bp.route("/")
def menu_list():

    menus = Menu.query.all()

    return render_template(
        "menu/menu_list.html",
        menus=menus
    )


@menu_bp.route("/add", methods=["GET", "POST"])
def add_menu():

    if request.method == "POST":

        new_menu = Menu(
            name=request.form["name"],
            category=request.form["category"],
            price=request.form["price"]
        )

        db.session.add(new_menu)
        db.session.commit()

        return redirect("/")

    return render_template("menu/add_menu.html")
