import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["JSON_AS_ASCII"] = False

    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY"),
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        WTF_CSRF_SECRET_KEY=os.getenv("WTF_CSRF_SECRET_KEY"),
    )

    db.init_app(app)
    Migrate(app, db)
    csrf.init_app(app)

    from apps.analytics import views as analytics_views
    from apps.crud import views as crud_views

    app.register_blueprint(analytics_views.analytics, url_prefix="/analytics")
    app.register_blueprint(
        crud_views.crud,
    )

    return app
