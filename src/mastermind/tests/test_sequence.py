import unittest

from mastermind.sequencefactory import SequenceFactory
from mastermind.sequence import Sequence


class MyTestCase(unittest.TestCase):

    def test_str(self):
        sf = SequenceFactory(4, 4)

        s = sf.create(0)
        self.assertEqual('0000', str(s))

        s = sf.create(255)
        self.assertEqual('3333', str(s))

    def test_equals(self):
        sf = SequenceFactory(5, 6)
        s1 = sf.create(4565)
        s2 = sf.create(4565)
        self.assertTrue(s1 is not s2)
        self.assertTrue(s1 == s2)
        self.assertEqual(s1, s2)
