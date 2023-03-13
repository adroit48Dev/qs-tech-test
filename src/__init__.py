""" init flask and database"""

from flask import Flask, jsonify
from logging.handlers import RotatingFileHandler
from flask.logging import default_handler

# from .models import CurrencyRates

from flask_sqlalchemy import SQLAlchemy

from datetime import *
import os, csv, logging
import sqlalchemy as sa

BASEDIR = os.path.abspath(os.path.dirname(__name__))


db = SQLAlchemy()

def create_app(config_filename=None):
    
    app = Flask(__name__)
    
    config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(config_type)
    
    initialize_extensions(app)
    register_blueprints(app)
    configure_logging(app)
    register_cli_commands(app)
    
    engine = sa.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    inspector = sa.inspect(engine)
    if not inspector.has_table('currency_rates'):
        with app.app_context():
            db.drop_all()
            db.create_all()
            # load_db()
            app.logger.info("Initialized the database..")
    else:
        app.logger.info('Database already contains the data!')
        
    return app

# initializing the extensions
def initialize_extensions(app):
    db.init_app(app)
    
# registering blueprints for routes   
def register_blueprints(app):
    from src.api import currency_bp
    
    app.register_blueprint(currency_bp)
    

def configure_logging(app):
    # Logging Configuration
    if app.config['LOG_WITH_GUNICORN']:
        gunicorn_error_logger = logging.getLogger('gunicorn.error')
        app.logger.handlers.extend(gunicorn_error_logger.handlers)
        app.logger.setLevel(logging.DEBUG)
    else:
        file_handler = RotatingFileHandler('instance/currency.log',
                                           maxBytes=16384,
                                           backupCount=20)
        file_formatter = logging.Formatter('%(asctime)s %(levelname)s %(threadName)s-%(thread)d: %(message)s [in %(filename)s:%(lineno)d]')
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

    app.logger.removeHandler(default_handler)

    app.logger.info('Starting the Currency rate flask app...')


def register_cli_commands(app):
    @app.cli.command('init_db')
    def initialize_database():
        """Initialize the database."""
        db.drop_all()
        db.create_all()
        from src.api.routes import load_db
        load_db()
       

