import unittest
from grid import Grid
from piece import Piece
from sequence import Sequence
import piece

class MyTestCase(unittest.TestCase):
    """
    Useful for setting up the grid:

    full_grid = [
        [piece.PTTTT, piece.PTTTF, piece.PTTFT, piece.PTTFF],
        [piece.PTFTT, piece.PTFTF, piece.PTFFT, piece.PTFFF],
        [piece.PFTTT, piece.PFTTF, piece.PFTFT, piece.PFTFF],
        [piece.PFFTT, piece.PFFTF, piece.PFFFT, piece.PFFFF] ]
    """

    def test_grid_sequence1(self):

        initial_state = [
            [piece.PFTTT, None       , piece.PTFFT, piece.PTTFT],
            [None       , None       , None       , None       ],
            [None       , piece.PTTTF, None       , None       ],
            [piece.PTTTT, None       , None       , None       ] ]

        initial_grid = Grid(initial_state)
        #print(initial_grid)
        expected_sequence_effective = {
            0: [piece.PFTTT, piece.PTTTT],
            1: [piece.PTTTF],
            2: [piece.PTFFT],
            3: [piece.PTTFT],
            4: [piece.PFTTT, piece.PTFFT, piece.PTTFT],
            5: [],
            6: [piece.PTTTF],
            7: [piece.PTTTT],
            8: [piece.PFTTT],
            9: [piece.PTTTT, piece.PTTTF, piece.PTTFT],
        }
        expected_sequence_with_none = {
            0: [piece.PFTTT, None, None, piece.PTTTT],
            1: [None, None, piece.PTTTF, None],
            2: [piece.PTFFT, None, None, None],
            3: [piece.PTTFT, None, None, None],
            4: [piece.PFTTT, None, piece.PTFFT, piece.PTTFT],
            5: [None, None, None, None],
            6: [None, piece.PTTTF, None, None],
            7: [piece.PTTTT, None, None, None],
            8: [piece.PFTTT, None, None, None],
            9: [piece.PTTTT, piece.PTTTF, None, piece.PTTFT],
        }
        for i in range(10):
            self.assertEqual(Sequence(expected_sequence_effective[i]), initial_grid.getSeq(i), "Unexpected Sequence 1:  " + str(i))
            self.assertEqual(Sequence(expected_sequence_with_none[i]), initial_grid.getSeq(i), "Unexpected Sequence 2: " + str(i))

    def test_grid_sequence2(self):

        initial_state = [
            [piece.PFTTT, None       , piece.PTFFT, piece.PTTFT],
            [None       , None       , None       , None       ],
            [None       , piece.PTTTF, None       , None       ],
            [piece.PTTTT, None       , None       , None       ] ]

        initial_grid = Grid(initial_state)
        new_grid = initial_grid.place(piece.PFFTF, 11)
        # print(new_grid)
        expected_sequence = {
            0: [piece.PFTTT, None, piece.PTTTT],
            1: [piece.PTTTF],
            2: [piece.PTFFT],
            3: [piece.PTTFT, piece.PFFTF],
            4: [piece.PFTTT, piece.PTFFT, piece.PTTFT],
            5: [None, None, None, None],
            6: [piece.PTTTF, piece.PFFTF],
            7: [piece.PTTTT],
            8: [piece.PFTTT],
            9: [piece.PTTTT, piece.PTTTF, piece.PTTFT],
        }
        for i in range(10):
            self.assertEqual(Sequence(expected_sequence[i]), new_grid.getSeq(i), "Unexpected Sequence " + str(i))

    def test_basics(self):
        grid = Grid()
        p = grid.at(0)
        self.assertIsNone(p)

        expected = piece.PTTTF
        newGrid = grid.place(expected, 7)
        res = newGrid.at(7)
        self.assertEqual(expected, res, "Unexpected value found: " + str(res))

    def test_grid_basic_validations1(self):
        initial_state = [
            [piece.PTTTT, None,  piece.PTTFT, piece.PTTFF],
            [piece.PTFTT, None,  piece.PTFFT, None       ],
            [piece.PFTTT, None,  None,        piece.PFTFF],
            [piece.PFFTT, None,  piece.PFFFT, piece.PFFFF] ]

        testee = Grid(initial_state)
        # print(testee)
        self.assertEqual(piece.PFTTT, testee.at(8), "Unexpected piece found 1")
        self.assertEqual(piece.PFFFT, testee.at(14), "Unexpected piece found 2")
        self.assertEqual(None, testee.at(7), "Unexpected piece found 3")

        # has_winner because of Seq(0) has 4 pieces that share the last 2 attributes values.
        self.assertTrue(testee.has_winner(), "This board contains a winning sequence.")
        self.assertTrue(testee.getSeq(0).is_winning(), "This is the only winning sequence of this grid.")
        for i in range(1, 10):
            self.assertFalse(testee.getSeq(i).is_winning(), "This is not a winning sequence.")

    def test_grid_basic_validations2(self):
        initial_state = [
            [None       , None       , None       , piece.PTTFF],
            [None       , None       , piece.PTFFT, None       ],
            [None       , piece.PFTTF, None       , None       ],
            [piece.PFFTT, None       , None       , None       ] ]

        testee = Grid(initial_state)
        # print(testee)

        # has no winner because the only completed seq(9) has pieces with no common attribute.
        self.assertFalse(testee.has_winner(), "This board does not contain a winning sequence.")
        self.assertTrue(len(testee.getSeq(9)) == 4, "This is the only completed sequence.")
        self.assertFalse(testee.getSeq(9).is_winning(), "And it is not winning.")
        # The other sequences for row and columns only have in piece in it.
        for i in range(8):
            self.assertTrue(len(testee.getSeq(i)) == 1, "This is an incomplete sequence.")
            self.assertFalse(testee.getSeq(i).is_winning(), "And of course, it is not winning.")
        # The other diagonal sequence (8) is empty.
        self.assertTrue(len(testee.getSeq(8)) == 0, "This is an empty sequence.")

    def test_grid_place_and_win(self):

        initial_state = [
            [None       , None       , None       , piece.PTTFT],
            [None       , None       , None       , None       ],
            [None       , piece.PTTTF, None       , None       ],
            [piece.PTTTT, None       , None       , None       ] ]

        initial_grid = Grid(initial_state)
        # print(testee)

        # has no winner because no sequence is completed.
        #  However, seq(9) can make this board win by putting the right pieces to index 6
        self.assertFalse(initial_grid.has_winner(), "This board does not contain a winning sequence.")
        self.assertTrue(len(initial_grid.getSeq(9)) == 3, "This is the sequence to complete.")

        # Place the winning piece (T...)
        new_grid = initial_grid.place(piece.PTFFT, 6)
        self.assertTrue(new_grid.has_winner(), "This board has now a winning sequence.")
        self.assertTrue(new_grid.getSeq(9).is_winning(), "And this is the diagonal we completed.")

    def test_grid_complete_sequence_no_win(self):

        initial_state = [
            [None       , None       , None       , piece.PTTFT],
            [None       , None       , None       , None       ],
            [None       , piece.PTTTF, None       , None       ],
            [piece.PTTTT, None       , None       , None       ] ]

        initial_grid = Grid(initial_state)
        # print(testee)

        # has no winner because no sequence is completed.
        #  However, seq(9) can make this board win by putting the right pieces to grid(6)
        self.assertFalse(initial_grid.has_winner(), "This board does not contain a winning sequence.")
        self.assertTrue(len(initial_grid.getSeq(9)) == 3, "This is the sequence to complete.")

        # Let put the wrong piece at the right place...
        new_grid = initial_grid.place(piece.PFFFF, 6)
        self.assertFalse(new_grid.has_winner(), "This board has still no winning sequence.")
        self.assertTrue(len(new_grid.getSeq(9)) == 4, "And this diagonal sequence is now completed.")

    def test_place_over_another_piece(self):

        empty_grid = Grid()
        grid1 = empty_grid.place(piece.PTTTT, 5)
        with self.assertRaises(AssertionError):
            grid1.place(piece.PTTTT, 5)

        grid2 = grid1.place(piece.PTTFF, 8)
        with self.assertRaises(AssertionError):
            grid2.place(piece.PTTFF, 8)
        with self.assertRaises(AssertionError):
            grid2.place(piece.PTTFF, 5)


if __name__ == '__main__':
    unittest.main()
