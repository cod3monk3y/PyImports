
# one class in each file, import directly from the file
from myimports.boo.ger import Booger
from myimports.boo.kbag import Bookbag

import unittest

class TestBooger(unittest.TestCase):
    def test_booger(self, ):
        assert 12 == Booger().add(6,2,0,4)
        
    def test_bookbag(self, ):
        assert 48 == Bookbag().mul(2,3,2,2,2)
    
    
