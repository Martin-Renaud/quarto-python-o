class TurnContext:

    def __init__(self, grid, piece_to_place, remaining_pieces, last_played_index=None):
        self.grid = grid
        self.piece_to_place = piece_to_place
        self.remaining_pieces = remaining_pieces
        self.last_played_index = last_played_index
