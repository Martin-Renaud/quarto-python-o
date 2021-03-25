import unittest
from piece import Piece
from piece import create_listofpieces


class MyTestCase(unittest.TestCase):
    def test_string(self):
        p = Piece(True, True, False, False)
        self.assertEqual(str(p), "OOXX")

        p = Piece(True, True, True, True)
        self.assertEqual(str(p), "OOOO")

        p = Piece(False, False, False, False)
        self.assertEqual(str(p), "XXXX")

    def test_factory_method(self):
        s1 = create_listofpieces()
        self.assertEqual(16, len(s1))

        s2 = create_listofpieces()
        self.assertEqual(s1, s2, "They are expected to contains both the same elements.")

        s1.clear()
        self.assertEqual(0, len(s1), "Expected to be cleared.")
        self.assertEqual(16, len(s2), "Expected to be unaffected 1.")

        s3 = create_listofpieces()
        self.assertEqual(s2, s3, "They are expected to contains both all elements.")
        self.assertEqual(0, len(s1), "Expected to be unaffected 2.")


    def test_equality(self):
        p1 = Piece(True, True, True, True)
        p2 = Piece(True, True, True, True)
        self.assertEqual(p1, p2, "Pieces must be equals 1")
        self.assertTrue(p1 == p2, "Pieces must be equals 2")
        self.assertFalse(p1 != p2, "Pieces must be equals 3")
        self.assertTrue(p1 is not p2, "Pieces are not the same object.")

        p3 = Piece(False, True, True, True)
        self.assertNotEqual(p1, p3, "Pieces must be not equals 1")
        self.assertFalse(p1 == p3, "Pieces must not be equals 2")
        self.assertTrue(p1 != p3, "Pieces must not be equals 3")



if __name__ == '__main__':
    unittest.main()
