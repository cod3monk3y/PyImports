# `bar_abs` imports Foo using absolute imports
from myimports.foo import Foo

class Bar(object):
    def foo(self, ):
        return Foo().bar()
    