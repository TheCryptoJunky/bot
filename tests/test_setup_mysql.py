# File: /tests/test_setup_mysql.py

import unittest
from unittest.mock import patch, MagicMock
from setup_mysql import connect_to_db, create_tables, create_user_and_database

class TestSetupMySQL(unittest.TestCase):
    @patch("setup_mysql.mysql.connector.connect")
    def test_connect_to_db(self, mock_connect):
        """
        Test database connection setup.
        """
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        conn, cursor = connect_to_db()
        self.assertIsNotNone(conn)
        self.assertIsNotNone(cursor)

    @patch("setup_mysql.mysql.connector.connect")
    def test_create_tables(self, mock_connect):
        """
        Test table creation during MySQL setup.
        """
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        create_tables(mock_conn.cursor())
        mock_conn.cursor().execute.assert_called()  # Ensure execute was called at least once

    @patch("setup_mysql.mysql.connector.connect")
    def test_create_user_and_database(self, mock_connect):
        """
        Test user and database creation.
        """
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        create_user_and_database(mock_conn.cursor())
        mock_conn.cursor().execute.assert_called()  # Ensure execute was called at least once

if __name__ == "__main__":
    unittest.main()
