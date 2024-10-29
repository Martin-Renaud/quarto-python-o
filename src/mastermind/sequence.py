from numpy import base_repr


class Sequence:

    def __init__(self, factory, index_value=0):
        self.factory = factory
        self.index_value = index_value

    def __str__(self):
        s = base_repr(self.index_value, self.factory.nb_possible_value).zfill(self.factory.length)
        return s

    def __eq__(self, other):
        if other is None:
            return False
        return self.index_value == other.index_value
