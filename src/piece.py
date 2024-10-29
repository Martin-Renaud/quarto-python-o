class Piece:
    """ Represent a Quarto piece and the state of all its attributes.
    """

    def __init__(self, v0, v1, v2, v3):
        # TODO: Prevent creation of Piece instances outside this class/module.
        self.values = (v0, v1, v2, v3)

    def v(self, index):
        assert 0 <= index <= 3
        return self.values[index]

    def __str__(self):
        return ''.join(list(map(lambda v: 'O' if v else 'X', self.values)))

    def __eq__(self, other):
        if other is None:
            return False
        return self.values == other.values

    def __hash__(self):
        return hash(str(self.values))


PTTTT = Piece(True, True, True, True)
PTTTF = Piece(True, True, True, False)
PTTFT = Piece(True, True, False, True)
PTTFF = Piece(True, True, False, False)
PTFTT = Piece(True, False, True, True)
PTFTF = Piece(True, False, True, False)
PTFFT = Piece(True, False, False, True)
PTFFF = Piece(True, False, False, False)
PFTTT = Piece(False, True, True, True)
PFTTF = Piece(False, True, True, False)
PFTFT = Piece(False, True, False, True)
PFTFF = Piece(False, True, False, False)
PFFTT = Piece(False, False, True, True)
PFFTF = Piece(False, False, True, False)
PFFFT = Piece(False, False, False, True)
PFFFF = Piece(False, False, False, False)

MASTER_SET = {
    PTTTT, PTTTF, PTTFT, PTTFF,
    PTFTT, PTFTF, PTFFT, PTFFF,
    PFTTT, PFTTF, PFTFT, PFTFF,
    PFFTT, PFFTF, PFFFT, PFFFF
}


def create_listofpieces():
    return list(MASTER_SET)
