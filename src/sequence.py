

class Sequence:

    ''' Contains a set of pieces.

        It contains between 0 and 4 pieces. It need to be complete (so 4 pieces) to be "winning".

        An incomplete sequence can be detected to be a sure non-winner (ex: [TTTT, FFFF])
    '''

    def __init__(self, pieces):
        self.pieces = [p for p in pieces if p is not None]

    def __len__(self):
        return len(self.pieces)

    def __eq__(self, other):
        return self.pieces == other.pieces

    def __hash__(self):
        return hash(str(self.pieces))


    def is_winning(self):
        if len(self.pieces) < 4:
            return False

        v1, v2, v3, v4 = self.pieces[0].v(0), self.pieces[0].v(1), self.pieces[0].v(2), self.pieces[0].v(3)
        a1, a2, a3, a4 = True, True, True, True
        for p in self.pieces:
            if p.v(0) != v1:
                a1 = False
            if p.v(1) != v2:
                a2 = False
            if p.v(2) != v3:
                a3 = False
            if p.v(3) != v4:
                a4 = False
            if not (a1 or a2 or a3 or a4):
                return False

        return a1 or a2 or a3 or a4