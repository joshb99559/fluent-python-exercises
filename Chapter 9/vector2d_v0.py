from array import array
import math

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    # Make iterable for easy conversion into list-types
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    # Utilize repr of object name and member fields
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    # Can convert member fields to tuple via iterator
    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    # Boolean value determined by positive/zero value of abs
    def __bool__(self):
        return bool(abs(self))