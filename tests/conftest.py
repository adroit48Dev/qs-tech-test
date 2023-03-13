# """Configuration file for test
# """

# import pytest
# import os
# # from src.api.routes import load_db
# from ..src import create_app, db


# @pytest.fixture(scope='module')
# def test_client():
#     # Create a Flask app configured for testing
#     flask_app = create_app()
#     flask_app.config.from_object('config.TestingConfig')

#     # Create a test client using the Flask application configured for testing
#     with flask_app.test_client() as testing_client:
#         # Establish an application context
#         with flask_app.app_context():
#             yield testing_client  # this is where the testing happens!


# @pytest.fixture(scope='module')
# def init_database(test_client):
#     # Create the database and the database table
#     db.create_all()
#     # load_db()

#     yield  # this is where the testing happens!

#     db.drop_all()


# @pytest.fixture(scope='module')
# def cli_test_client():
#     flask_app = create_app()
#     flask_app.config.from_object('config.TestingConfig')

#     runner = flask_app.test_cli_runner()

#     yield runner 


