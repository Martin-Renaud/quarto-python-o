from context import TurnContext
from player import Player
import random

class RandomPlayer(Player):

    def __init__(self, name):
        super().__init__(name)
        random.seed()

    def play(self, turnContext):
        """
        """

        selected_index = self.pick_random_free_index(turnContext.grid)
        new_grid = turnContext.grid.place(turnContext.piece_to_place, selected_index)
        if len(turnContext.remaining_pieces) > 0:
            selected_piece = random.choice(turnContext.remaining_pieces)
            new_remaining = turnContext.remaining_pieces.copy()
            new_remaining.remove(selected_piece)
            #print(f"Placing {turnContext.piece_to_place} at {selected_index} and select {selected_piece} for opponent.")
            return TurnContext(new_grid, selected_piece, new_remaining, selected_index)

        print("Placing", turnContext.piece_to_place, "at", selected_index, "It was the last piece.")
        return TurnContext(new_grid, None, None, selected_index)

    def pick_random_free_index(self, grid):
        free_indexes = grid.available_indexes
        picked_index = random.randint(0, len(free_indexes) - 1)
        # print("Selected index", valid_indexes[pickedIndex], " to place the piece.")
        return free_indexes[picked_index]


