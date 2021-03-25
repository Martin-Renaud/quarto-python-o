import logging

from context import TurnContext
from player import Player
from randomplayer import RandomPlayer
from minimax.minimax import Minimax


class SmartMinimax(Player):
    logger = logging.getLogger(__name__)

    def __init__(self, name = "Smart Minimax"):
        super().__init__(name)
        self.random_player = RandomPlayer("Utility Random")
        self.minimax_payer = Minimax("Utility Minimax")

    def play(self, tc):

        if len(tc.remaining_pieces) > 10:
            SmartMinimax.logger.debug(f"{self.name} plays random - {len(tc.remaining_pieces)} remaining pieces.")
            return self.random_player.play(tc)

        SmartMinimax.logger.debug(f"{self.name} plays optimal - {len(tc.remaining_pieces)} remaining pieces.")
        return self.minimax_payer.play(tc)
