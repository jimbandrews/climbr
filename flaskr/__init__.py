import os
from flask import Flask, render_template
from flask_migrate import Migrate
from .models import db
# from . import update_gyms as update


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # connecting flask app to PostgreSQL
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://climbr:1148@localhost:5432/climbr"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate = Migrate(app, db)

    # ensure the instance folder exists
    try:
        os.mkdir(app.instance_path)
    except OSError:
        pass

    # registering blueprints
    # app.register_blueprint(update.bp)
    from . import auth
    app.register_blueprint(auth.bp)

    # homepage
    @app.route("/")
    def home():
        return render_template("index.html")

    return app
