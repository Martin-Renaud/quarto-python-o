import unittest

from mastermind.sequencecomparator import *
from mastermind.sequence import Sequence
from mastermind.sequencefactory import SequenceFactory


class MyTestCase(unittest.TestCase):

    def test1(self):
        self.validate(SequenceFactory(nb_possible_value=10, length=6), '012345', '019954', 2, 2)
        self.validate(SequenceFactory(nb_possible_value=10, length=6), '012345', '543210', 0, 6)
        self.validate(SequenceFactory(nb_possible_value=10, length=6), '012345', '012345', 6, 0)
        self.validate(SequenceFactory(nb_possible_value=10, length=6), '881888', '019954', 0, 1)

    def validate(self, sf, str1, str2, r1, r2):
        s1 = sf.create_from_string(str1)
        s2 = sf.create_from_string(str2)
        res = compare(s1, s2)
        self.assertEqual(res[0] == r1)
        self.assertEqual(res[2] == r2)
