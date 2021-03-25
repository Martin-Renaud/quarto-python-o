import unittest
import piece
from sequence import Sequence


class MyTestCase(unittest.TestCase):


    def test_equality1(self):
        s1 = Sequence([piece.PTTTF, None, None, piece.PTTTT])
        s2 = Sequence([piece.PTTTF, None, None, piece.PTTTT])
        self.assertEqual(s1, s2, "Equality expected 1.")
        self.assertTrue(s1 == s2, "Equality expected 2.")
        self.assertFalse(s1 != s2, "Equality expected 3.")

        s3 = Sequence([piece.PTTTF, piece.PTTTT])
        self.assertEqual(s1, s3, "Equality expected 4.")
        self.assertEqual(s2, s3, "Equality expected 5.")

        # sa has a different order of the same two piece, so its different
        s4 = Sequence([piece.PTTTT, piece.PTTTF])
        self.assertNotEqual(s1, s4, "Inequality expected 1.")
        self.assertTrue(s1 != s4, "Inequality expected 2.")
        self.assertFalse(s1 == s4, "Inequality expected 3.")


    def test_isWinningPartialSequence(self):
        testee = Sequence([None, None, None, None])
        self.assertFalse(testee.is_winning())

        testee = Sequence([piece.PTTTT, None, None, None])
        self.assertFalse(testee.is_winning())

        testee = Sequence([None, None, None, piece.PTTTT])
        self.assertFalse(testee.is_winning())

        testee = Sequence([piece.PTTTF, None, None, piece.PTTTT])
        self.assertFalse(testee.is_winning())

    def test_isNotWinning(self):
        testee = Sequence([piece.PTTTT, piece.PFFFF, piece.PTFTF, piece.PFTFT])
        self.assertFalse(testee.is_winning())


    def test_is_winning(self):
        testee = Sequence([piece.PTTTT, piece.PTFTT, piece.PTTFF, piece.PTFTF])
        self.assertTrue(testee.is_winning())

        testee = Sequence([piece.PTTTT, piece.PFTTT, piece.PFTFT, piece.PTTFT])
        self.assertTrue(testee.is_winning())


if __name__ == '__main__':
    unittest.main()
