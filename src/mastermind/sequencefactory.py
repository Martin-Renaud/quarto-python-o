from mastermind.sequence import Sequence
import random


class SequenceFactory:

    def __init__(self, nb_possible_value, length):
        assert nb_possible_value > 2
        assert nb_possible_value <= 10
        assert length > 0
        self.length = length
        self.nb_possible_value = nb_possible_value
        self.nb_of_possible_sequence = pow(self.nb_possible_value, self.length)

    def create(self, index_value=0):
        assert index_value >= 0
        assert index_value < self.nb_of_possible_sequence
        return Sequence(self, index_value)

    def create_random(self):
        index_value = random.randrange(self.nb_of_possible_sequence)
        return Sequence(self, index_value)

    def create_from_string(self, stingval):
        assert len(stingval) == self.length
        index = int(stingval, self.nb_possible_value)
        return Sequence(self, index)

    def next(self, seq):
        next_index_value = seq.index_value + 1
        if next_index_value >= self.nb_of_possible_sequence:
            next_index_value = 0
        return Sequence(self, next_index_value)
