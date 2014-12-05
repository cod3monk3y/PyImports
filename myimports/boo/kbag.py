
class Bookbag(object):
    def mul(self, *args ):
        k = 1
        for v in args:
            k = k*v
        return k
