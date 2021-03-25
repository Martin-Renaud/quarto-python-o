import logging
import unittest
import piece
from minimax.node import Node
from piece import create_listofpieces
from grid import Grid

def total_nb_child_nodes(free_places):
    '''
    1  --> 0
    2  --> 2
    3  --> 18
    4  --> 228
    5  --> 4580
    6  --> 137430
    7  --> 5772102
    8  --> 323237768
    9  --> 23273119368
    10 --> 2094580743210
    11 --> 230403881753210
    12 --> 30413312391423852
    13 --> 4744476733062121068
    14 --> 863494765417306034558
    15 --> 181333900737634267257390
    16 --> 43520136177032224141773840
    '''
    assert free_places >= 1
    if free_places == 1:
        return 0
    return free_places * (free_places - 1) + free_places * (free_places - 1) * total_nb_child_nodes(free_places - 1)

class MyTestCase(unittest.TestCase):

    def test_child_creation_one_free_place(self):

        grid_pieces = [
            [piece.PTTTT, piece.PTTTF, piece.PTTFT, piece.PTTFF],
            [piece.PTFTT, piece.PTFTF, piece.PTFFT, piece.PTFFF],
            [piece.PFTTT, piece.PFTTF, piece.PFTFT, piece.PFTFF],
            [piece.PFFTT, piece.PFFTF, piece.PFFFT, None]]

        remaining_pieces = list()
        piece_to_place = piece.PFFFF
        grid = Grid(grid_pieces)

        node = Node(grid, piece_to_place, remaining_pieces)
        node.build_children()
        total_created = node.build_children(True)
        self.assertEqual(0, len(node.children))
        self.assertEqual(total_nb_child_nodes(1), total_created)


    def test_child_creation_two_free_places(self):

        grid_pieces = [
            [piece.PTTTT, piece.PTTTF, piece.PTTFT, piece.PTTFF],
            [piece.PTFTT, piece.PTFTF, piece.PTFFT, piece.PTFFF],
            [piece.PFTTT, piece.PFTTF, piece.PFTFT, piece.PFTFF],
            [piece.PFFTT, piece.PFFTF, None,        None]]

        remaining_pieces = [piece.PFFFT]
        piece_to_place = piece.PFFFF
        grid = Grid(grid_pieces)

        node = Node(grid, piece_to_place, remaining_pieces)
        total_created = node.build_children(True)
        self.assertEqual(2, len(node.children))
        self.assertEqual(total_nb_child_nodes(2), total_created)

    def test_child_creation_three_free_places(self):

        grid_pieces = [
            [piece.PTTTT, piece.PTTTF, piece.PTTFT, piece.PTTFF],
            [piece.PTFTT, piece.PTFTF, piece.PTFFT, piece.PTFFF],
            [piece.PFTTT, piece.PFTTF, piece.PFTFT, piece.PFTFF],
            [piece.PFFTT, None,        None,        None]]

        remaining_pieces = [piece.PFFFT, piece.PFFTF]
        piece_to_place = piece.PFFFF
        grid = Grid(grid_pieces)

        node = Node(grid, piece_to_place, remaining_pieces)
        total_created = node.build_children(True)
        self.assertEqual(3*2, len(node.children))
        self.assertEqual(total_nb_child_nodes(3), total_created)

    def test_child_creation_four_last_piece(self):

        grid_pieces = [
            [None,        piece.PTTTF, piece.PTTFT, piece.PTTFF],
            [piece.PTFTT, piece.PTFTF, None,        piece.PTFFF],
            [piece.PFTTT, None,        piece.PFTFT, piece.PFTFF],
            [piece.PFFTT, piece.PFFTF, piece.PFFFT, None]]

        remaining_pieces = [piece.PTTTT, piece.PTFFT, piece.PFTTF]
        piece_to_place = piece.PFFFF
        grid = Grid(grid_pieces)

        node = Node(grid, piece_to_place, remaining_pieces)
        total_created = node.build_children(True)
        self.assertEqual(4*3, len(node.children))
        self.assertEqual(total_nb_child_nodes(4), total_created)

    def test_child_creation_x_last_piece(self):

        grid_pieces = [
            [None,        piece.PTTTF, piece.PTTFT, None],
            [piece.PTFTT, piece.PTFTF, None,        None],
            [piece.PFTTT, None,        piece.PFTFT, piece.PFFTF],
            [piece.PFFTT, None,        piece.PFFFT, piece.PTTFF]]

        remaining_pieces = [piece.PTTTT, piece.PFTFF, piece.PTFFT, piece.PFTTF,piece.PTFFF]
        piece_to_place = piece.PFFFF
        grid = Grid(grid_pieces)

        node = Node(grid, piece_to_place, remaining_pieces)
        total_created = node.build_children(True)
        self.assertEqual(6*5, len(node.children))
        self.assertEqual(total_nb_child_nodes(6), total_created)

    def test_child_creation_not_recursive(self):

        remaining_pieces = create_listofpieces()
        piece_to_place = remaining_pieces.pop()
        grid = Grid()

        node = Node(grid, piece_to_place, remaining_pieces)
        total_created = node.build_children(False)
        self.assertEqual(16*15, len(node.children))
        self.assertEqual(16*15, total_created)




if __name__ == '__main__':
    unittest.main()
