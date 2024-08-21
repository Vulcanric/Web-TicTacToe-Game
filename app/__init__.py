from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from os import path

db = SQLAlchemy()
socketio = SocketIO()

# Define the database file
DB_NAME = "tictactoe.db"

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Kirikou'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    socketio.init_app(app)

    # Import blueprints
    from .routes import main

    # Register blueprints
    app.register_blueprint(main, url_prefix="/")

    # Create the database if it doesn't exist
    with app.app_context():
        if not path.exists(f'instance/{DB_NAME}'):
            db.create_all()
            print('Database created!')

    return app
