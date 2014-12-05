# absolute import
import unittest

from myimports.foo import Foo
from myimports.bar_abs import Bar as BarAbs
from myimports.bar_rel import Bar as BarRel
from myimports.goo.ber.goober import Goober

class TestAbsImport(unittest.TestCase):
    def test_foo(self):  
        self.assertEqual('bar', Foo().bar())
        
    def test_bar_abs(self, ):
        self.assertEqual('bar', BarAbs().foo())
        
    def test_bar_rel(self, ):
        self.assertEqual('bar', BarRel().foo())
    
    def test_goober(self, ):
        self.assertEqual(9, Goober().echo(9))
    