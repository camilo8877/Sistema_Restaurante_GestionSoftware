from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Importar modelos
    from app.models.user import User
    from app.models.menu import Menu
    from app.models.order import Order
    from app.models.reservation import Reservation

    # Importar rutas
    from app.routes.auth_routes import auth_bp
    from app.routes.menu_routes import menu_bp
    from app.routes.order_routes import order_bp
    from app.routes.reservation_routes import reservation_bp
    from app.routes.report_routes import report_bp

    # Registrar blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(menu_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(reservation_bp)
    app.register_blueprint(report_bp)

    # Crear tablas
    with app.app_context():
        db.create_all()

    return app