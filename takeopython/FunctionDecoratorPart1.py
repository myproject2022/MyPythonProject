"""
Another Example of the function decorator
"""

class Tracer:
    def __init__(self, func):
        self.call = 0
        self.func = func

    def __call__(self, *args):
        self.call += 1
        print("Call", (self.call, self.func.__name__))


@Tracer
def spam(a, b, c):
    print(a, b, c)


spam(1, 2, 3)
spam('a', 'b', 'c')
spam(6, 7, 8)
