import unittest
from grid import Grid
from piece import Piece
import piece
from context import TurnContext
from minimax.minimax import Minimax

class MyTestCase(unittest.TestCase):

    def test_1(self):
        initial_state = [
            [piece.PFFTF, None,         None,        piece.PFTTT],
            [piece.PTTTF, piece.PTTFF,  piece.PTFFF, piece.PFFFT],
            [piece.PTFTT, piece.PFTFF,  piece.PTTFT, None],
            [piece.PFTFT, piece.PFFTT,  piece.PTFFT, piece.PFTTF]]

        grid = Grid(initial_state)
        self.assertFalse(grid.has_winner())

        piece_to_place = piece.PTTTT
        remaining_pieces = [piece.PTFTF, piece.PFFFF]

        testee = Minimax()
        tc = TurnContext(grid, piece_to_place, remaining_pieces, 4)
        result = testee.play(tc)

        self.assertTrue(result.grid.has_winner())
        self.assertEqual(result.last_played_index, 2)

    def test_2(self):
        initial_state = [
            [piece.PTTTF, piece.PFFFT,  piece.PFTTT, piece.PTFTF],
            [piece.PFTFT, piece.PFTTF,  piece.PTFFF, None],
            [None,        None       ,  piece.PFFFF, piece.PTFFT],
            [piece.PTFTT, piece.PTTFT,  None,        piece.PFFTT]]

        grid = Grid(initial_state)
        self.assertFalse(grid.has_winner())

        piece_to_place = piece.PFFTF
        remaining_pieces = [piece.PTTTT, piece.PFTFF, piece.PTTFF]

        testee = Minimax()
        tc = TurnContext(grid, piece_to_place, remaining_pieces, 99)
        result = testee.play(tc)

        self.assertTrue(result.grid.has_winner())
        self.assertEqual(result.last_played_index, 7)

        # ---
        piece_to_place = piece.PTTTT
        remaining_pieces = [piece.PFFTF, piece.PFTFF, piece.PTTFF]

        testee = Minimax()
        tc = TurnContext(grid, piece_to_place, remaining_pieces, 99)
        result = testee.play(tc)

        self.assertTrue(result.grid.has_winner())
        self.assertEqual(result.last_played_index, 9)


    def test_3(self):
        initial_state = [
            [None,        None, None,        piece.PTTFT],
            [None,        None, piece.PTTFF, None],
            [None,        None, None,        None],
            [piece.PFTTT, None, None,        None]]

        grid = Grid(initial_state)
        self.assertFalse(grid.has_winner())

        piece_to_place = piece.PFTFF
        remaining_pieces = [piece.PFFTF, piece.PTFTT, piece.PFFTT, piece.PFFFF, piece.PTFFT, piece.PFTFT,
                            piece.PFTTF,  piece.PTFFF, piece.PTTTF, piece.PFFFT,  piece.PTFTF, piece.PTTTT]

        testee = Minimax()
        tc = TurnContext(grid, piece_to_place, remaining_pieces, 99)
        result = testee.play(tc)

        self.assertTrue(result.grid.has_winner())
        self.assertEqual(result.last_played_index, 9)

    def test_4(self):
        initial_state = [
            [None,        None, None,        piece.PTTFT],
            [None,        None, piece.PTTFF, None],
            [None,        None, None,        None],
            [piece.PFTTT, None, None,        None]]

        grid = Grid(initial_state)
        self.assertFalse(grid.has_winner())

        piece_to_place = piece.PFFFF
        remaining_pieces = [piece.PFFTF, piece.PTFTT, piece.PFFTT, piece.PFTFF, piece.PTFFT, piece.PFTFT,
                            piece.PFTTF,  piece.PTFFF, piece.PTTTF, piece.PFFFT,  piece.PTFTF, piece.PTTTT]

        testee = Minimax()
        tc = TurnContext(grid, piece_to_place, remaining_pieces, 99)
        result = testee.play(tc)

        self.assertTrue(result.grid.has_winner())
        self.assertEqual(result.last_played_index, 9)