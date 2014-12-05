import unittest

# multiple classes defined in one file can be imported simply by providing a tuple
from myimports.boo.geyman import (Boogeyman, OogieBoogie)

class TestMultipleClassesPerFile(unittest.TestCase):
    
    def test_boogeyman(self, ):
        assert 78 == Boogeyman().echo(78)
        
    def test_oogieboogey(self,):
        assert 89 == OogieBoogie().echo(89)


    