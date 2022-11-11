from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["JSON_AS_ASCII"] = False

    from apps.analytics import view as analytics_views

    app.register_blueprint(analytics_views.analytics, url_prefix="/analytics")

    return app
