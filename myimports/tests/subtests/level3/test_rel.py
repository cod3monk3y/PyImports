#!/usr/bin/env python

# relative import
# '..' plus '.' for every level additional => '..' + '.' + '.'

from ....foo import Foo
from ....bar_abs import Bar as BarAbs
from ....bar_rel import Bar as BarRel
from ....goo.ber.goober import Goober # up 3 levels and down 2

import unittest

class TestRelImport(unittest.TestCase):
    def test_foo(self):
        self.assertEqual('bar', Foo().bar())
        
    def test_bar_abs(self, ):
        self.assertEqual('bar', BarAbs().foo())
        
    def test_bar_rel(self, ):
        self.assertEqual('bar', BarRel().foo())
    
    def test_goober(self, ):
        self.assertEqual(9, Goober().echo(9))
    
