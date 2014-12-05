# `bar_rel` imports foo using relative imports
from .foo import Foo

class Bar(object):
    def foo(self, ):
        return Foo().bar()
    