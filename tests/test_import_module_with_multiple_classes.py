#!/usr/bin/env python

import unittest

# this works, but we only want to focus on the sub-module `boo`
#import myimports

# only import from submodule boo
import myimports.boo


class TestImportModuleWithMultipleClasses(unittest.TestCase):
    
    # okay, referenced directly
    def test_direct_reference(self, ):
        assert myimports.boo.kbag.Bookbag().mul(3,4) == 12
    
    # indirect references through boo, since Boo
    # is imported into `myimports.boo`
    def test_module_imports_file(self, ):
        # this is actually located at `myimports.boo.ger.Booger`
        assert myimports.boo.Booger().add(5,6) == 11
    
    # 'module' has no attribute 'Bookbag'
    # (since it was not imported via __init__.py)
    #def test_invalid_indirect_ref(self, ):
    #    assert myimports.boo.Bookbag().mul(9,8) == 72
    
    # I would expect this NOT to work, but it does
    def test_other_submodule_not_imported(self,):
        assert myimports.goo.ber.goober.Goober().echo(8) == 8
    