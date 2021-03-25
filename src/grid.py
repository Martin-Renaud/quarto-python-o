import logging
from sequence import Sequence


class Grid:
    DIMENSION = 4

    logger = logging.getLogger(__name__)

    """
    There are 10 sequences in on the grid, each with their own id (0-9)
        # seqId 0-3 : columns / vertical
        # seqId 4-7 : rows / horizonal
        # seqId 8   : diagonal 1 - downward
        # seqId 9   : diagonal 2 - upward
            Sequence- [index]
            
          Sequence- Index in pieces (indexes_from_seqIndex maps this)
       8    0  1  2  3    9
            |  |  |  |
       4-   0  1  2  3
       5-   4  5  6  7
       6-   8  9 10 11
       7-  12 13 14 15

       Sequence will contain only real pieces. The None are removed.
    """

    indexes_from_seqIndex = {
        0: (0, 4, 8, 12),
        1: (1, 5, 9, 13),
        2: (2, 6, 10, 14),
        3: (3, 7, 11, 15),
        4: (0, 1, 2, 3),
        5: (4, 5, 6, 7),
        6: (8, 9, 10, 11),
        7: (12, 13, 14, 15),
        8: (0, 5, 10, 15),
        9: (12, 9, 6, 3)
    }

    def __init__(self, pieces=None):

        self.pieces_list = list()
        if pieces is None:
            self.pieces_list = [None] * 16
        elif len(pieces) == Grid.DIMENSION:
            for line in pieces:
                assert len(line) == Grid.DIMENSION
                self.pieces_list += line
        else:
            assert len(pieces) == Grid.DIMENSION ** 2
            self.pieces_list += pieces
        self.available_indexes = self.free_indexes()

    def __str__(self):
        result = "Grid:"
        for i in range(len(self.pieces_list)):
            if i % 4 == 0:
                result += "\n\t"
            if self.pieces_list[i] is None:
                result += "<....> "
            else:
                result += "<" + str(self.pieces_list[i]) + "> "
        return result

    def place(self, piece, index):
        """ index is between 0 and 15 and is expected to be free. """
        assert 0 <= index < Grid.DIMENSION ** 2
        assert self.pieces_list[index] is None

        new_pieces_list = self.pieces_list.copy()
        new_pieces_list[index] = piece
        return Grid(new_pieces_list)

    def at(self, index):
        assert 0 <= index < Grid.DIMENSION ** 2
        return self.pieces_list[index]

    def is_full(self):
        """ Indicate is there is still room on the grid for another piece. """
        return None not in self.pieces_list

    def has_winner(self):
        """Return True is the grid contains a winning sequence."""
        i = 0
        while i < 10:
            if self.getSeq(i).is_winning():
                return True
            i += 1
        return False

    def free_indexes(self):
        result = list()
        for i in range(len(self.pieces_list)):
            if self.at(i) is None:
                result.append(i)
        return result

    def getSeq(self, seqIndex):
        """
        There are 10 sequences in on the grid, each with their own id (0-9)
          Sequence- Index in pieces
           8   0  1  2  3     9
                |  |  |  |
           4-   0  1  2  3
           5-   4  5  6  7
           6-   8  9 10 11
           7-  12 13 14 15
        """
        assert 0 <= seqIndex < 10
        indexes = Grid.indexes_from_seqIndex[seqIndex]
        return Sequence([self.pieces_list[indexes[0]], self.pieces_list[indexes[1]], self.pieces_list[indexes[2]], self.pieces_list[indexes[3]]])
