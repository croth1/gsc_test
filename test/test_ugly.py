import unittest
from ugly import is_valid_ensembl_id


# after installing nosetests, you can run the test by navigating
# into the directory containing ugly.py and running nosetests -v

class UglyTestcase(unittest.TestCase):

    def dummy_test(self):
        # obvious, because 21 is only half of the truth!
        self.assertTrue(42 > 21)
