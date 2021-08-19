import os
from flask import Flask
from flask_socketio import SocketIO
from werkzeug.debug import DebuggedApplication
from src.models import db
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

socketio = SocketIO(cors_allowed_origins='*')

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    # this is so we can debug the app, even without running it through flask run
    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

    app.config.from_mapping(
        SECRET_KEY='secret',
    )

    app.config[
    "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{table}".format(
        user=os.getenv("POSTGRES_USER"),
        passwd=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=5432,
        table=os.getenv("POSTGRES_DB"),
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate = Migrate(app, db)
    with app.app_context():
        db.create_all()

    # add your routes here! try to write them as blueprints if you can
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import api

    app.register_blueprint(api.bp)

    from . import chat

    app.register_blueprint(chat.bp)

    from . import multiplayer

    app.register_blueprint(multiplayer.bp)

    from . import databaseHelper

    app.register_blueprint(databaseHelper.bp)

    socketio.init_app(app, async_mode='gevent')

    return app