from nose.tools import assert_equal

__author__ = 'Hans'

import unittest
import nose
from __init__ import splitConnectionsData

class splitConnectionsTestCase(unittest.TestCase):

    def setUp(self):
        print("setup")

        print("setup completed")

    def test_split_connection(self):
        print("testing connections!")

        #assert_equal(splitConnectionsData(),3671,"split connections has to run with 3671 lines!")

        print("testing connections complete!")




if __name__ == '__main__':
    unittest.main()

