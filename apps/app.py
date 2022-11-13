from pathlib import Path

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    app.config["JSON_AS_ASCII"] = False

    app.config.from_mapping(
        SECRET_KEY="3700c757-8e0d-4039-99f4-2530cbd82853",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        WTF_CSRF_SECRET_KEY="5a38f877-3357-416c-b38d-eba99997b909",
    )

    db.init_app(app)
    Migrate(app, db)
    csrf.init_app(app)

    from apps.analytics import views as analytics_views
    from apps.crud import views as crud_views

    app.register_blueprint(analytics_views.analytics, url_prefix="/analytics")
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app
