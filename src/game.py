/import logging
from minimax.patate import Patate
from minimax.minimax import Minimax
from minimax.smartminimax import SmartMinimax
from randomplayer import RandomPlayer
from context import TurnContext
from piece import create_listofpieces
from grid import Grid

class Game:

    def configure(self):
        logging.basicConfig(filename='game.log',filemode='w', format="%(asctime)s %(levelname)s %(name)s %(message)s",
                            level=logging.DEBUG)
        logging.info('Logging module initialized.')

    def start(self):
        self.configure()
        result = ()
        p1 = SmartMinimax("Player 1")
        p2 = SmartMinimax("Player 2")
        remaining_pieces = create_listofpieces()
        piece_to_place = remaining_pieces.pop()
        active_player = p1
        turn_context = TurnContext(Grid(), piece_to_place, remaining_pieces)

        print("Game Start")
        while not turn_context.grid.is_full():
            assert turn_context.grid.has_winner() is False
            logging.info(f"*******************\n{active_player} has to place {turn_context.piece_to_place} on grid:\n{turn_context.grid}")
            #print(f"{active_player} has to place {turn_context.piece_to_place} on grid:\n{turn_context.grid}")

            turn_context = active_player.play(turn_context)
            logging.info(f"{active_player} played at position  {turn_context.last_played_index} and picked {turn_context.piece_to_place}")
            if turn_context.grid.has_winner():
                logging.info(f"{active_player} won the game! Final grid:\n{turn_context.grid}", )
                break
            if active_player is p1:
                active_player = p2
            else:
                active_player = p1

        logging.info("Game finished.")
        p = Patate()
        p.foo()
        return result


g = Game()
g.start()
