import unittest

# these classes are imported into __init__.py
from myimports.boo import (Booger, Boogeyman, OogieBoogie)

# bookbag must be imported directly, as it is *not* defined
# in `myimports.boo.__init__.py` (it is commented out)
from myimports.boo.kbag import Bookbag

class TestImportFromModule(unittest.TestCase):
    
    # __init__.py import
    def test_booger(self):
        assert Booger().add(1,2,3,4) == 10
        
    def test_boogeyman(self, ):
        assert Boogeyman().echo(1) == 1
        
    def test_oogieboogie(self,):
        assert OogieBoogie().echo(2) == 2

    # direct import
    def test_bookbag(self, ):
        assert Bookbag().mul(1,2,3,4) == 24
        
    
    
