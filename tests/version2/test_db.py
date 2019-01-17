"""Tests the database connection and tables creation"""
import unittest

from app import create_app
from app.API.utilities.database import connection

class DBCase(unittest.TestCase):
    """Unit testiing for the connection and creation of tables"""
    def setUp(self):
        """Initialize the app and database connections"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

        with self.app.app_context():
            connection.dbconnection()
            connection.initializedb()

    def tearDown(self):
        """Drops all tables after tests are done"""
        with self.app.app_context():
            connection.dbconnection()
            connection.drop_tables()