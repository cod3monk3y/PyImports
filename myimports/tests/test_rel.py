#!/usr/bin/env python

# relative import

from ..foo import Foo
from ..bar_abs import Bar as BarAbs
from ..bar_rel import Bar as BarRel

import unittest

class TestRelImport(unittest.TestCase):
    def test_foo(self):
        self.assertEqual('bar', Foo().bar())
        
    def test_bar_abs(self, ):
        self.assertEqual('bar', BarAbs().foo())
        
    def test_bar_rel(self, ):
        self.assertEqual('bar', BarRel().foo())
    
    
