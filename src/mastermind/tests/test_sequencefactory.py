import unittest
from mastermind.sequencefactory import SequenceFactory


class MyTestCase(unittest.TestCase):

    def test_ctor_argument_validation(self):
        self.assertRaises(AssertionError, SequenceFactory, 1, 5)
        self.assertRaises(AssertionError, SequenceFactory, 2, 5)
        self.assertRaises(AssertionError, SequenceFactory, 11, 5)
        self.assertRaises(AssertionError, SequenceFactory, 5, -1)
        self.assertRaises(AssertionError, SequenceFactory, 5, 0)

    def test_computation_of_possibilities(self):
        self.assertEqual(5 * 5 * 5, SequenceFactory(nb_possible_value=5, length=3).nb_of_possible_sequence)

    def test_create_argument_validation(self):
        sf = SequenceFactory(3, 4)
        self.assertRaises(AssertionError, sf.create, -1)
        self.assertRaises(AssertionError, sf.create, 81)
        sf.create(0)
        sf.create(80)

    def test_create_from_string(self):

        sf = SequenceFactory(3, 4)
        s = sf.create_from_string('0010')
        self.assertEqual(3, s.index_value)
        s = sf.create_from_string('2222')
        self.assertEqual(3**4-1, s.index_value)

    def test_create_from_string_exception(self):
        sf = SequenceFactory(nb_possible_value=3, length=4)
        self.assertRaises(AssertionError, sf.create_from_string, '12345')
        self.assertRaises(ValueError, sf.create_from_string, '2223')

    def test_next(self):

        sf = SequenceFactory(3, 2)
        s = sf.create()
        self.assertEqual('00', str(s))
        s = sf.next(s)
        self.assertEqual('01', str(s))
        s = sf.next(s)
        self.assertEqual('02', str(s))
        s = sf.next(s)
        self.assertEqual('10', str(s))
        s = sf.next(s)
        self.assertEqual('11', str(s))
        s = sf.next(s)
        self.assertEqual('12', str(s))
        s = sf.next(s)
        self.assertEqual('20', str(s))
        s = sf.next(s)
        self.assertEqual('21', str(s))
        s = sf.next(s)
        self.assertEqual('22', str(s))
        s = sf.next(s)
        self.assertEqual('00', str(s))
