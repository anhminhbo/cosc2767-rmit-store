import unittest
import rmit_store_methods as methods


class RmitStoreAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_database_connection():
        methods.setUp()
        methods.checkDatabaseErrorAppear()
        methods.tearDown()
