__author__ = 'Hans'

import unittest
from __init__ import splitConnectionsData

class splitConnectionsTestCase(unittest.TestCase):

    def setUp(self):
        print("setup")

        print("setup completed")

    def test_split_connection(self):
        print("testing connections!")
        splitConnectionsData()


        print("testing connections complete!")




if __name__ == '__main__':
    unittest.main()

