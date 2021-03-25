import logging

from context import TurnContext
from player import Player


class Node (TurnContext):

    def __init__(self, parent_node, grid, piece_to_place, remaining_pieces, last_played_index):
        super().__init__(grid, piece_to_place, remaining_pieces, last_played_index)
        self.parent_node = parent_node
        self.score = 0
        self.children = list()
        self.expected_next = None


class ExplorationStats:

    def __init__(self):
        self.depth = 0
        self.node_created = 0

    def prefix(self):
        return "D:" + str(self.depth) + " " * ((self.depth - 1) * 4)


class Selector:

    def __init__(self, name, winning_score, reversed_sort):
        self.name = name
        self.winning_score = winning_score
        self.reversed_sort = reversed_sort

    def get_next(self):
        if self == MAX_SELECTOR:
            return MIN_SELECTOR
        return MAX_SELECTOR

    def pick_best_node(self, node_list):
        def score_extractor(node):
            return node.score

        node_list.sort(reverse=self.reversed_sort, key=score_extractor)
        return node_list.pop(0)


MIN_SELECTOR = Selector("MinSelector", -1, False)
MAX_SELECTOR = Selector("MaxSelector", 1, True)


class Minimax(Player):
    logger = logging.getLogger(__name__)

    MAX_DEPTH = 3

    def __init__(self, name = "Minimax"):
        super().__init__(name)

    def play(self, tc):

        stats = ExplorationStats()
        current_node = Node(None, tc.grid, tc.piece_to_place, tc.remaining_pieces, tc.last_played_index)

        self.process_node(current_node, stats, MAX_SELECTOR)

        best_node = MAX_SELECTOR.pick_best_node(current_node.children)

        Minimax.logger.debug(f"{stats.node_created} nodes explored to find best move with score {best_node.score}.")
        # Minimax.logger.debug(f"Opponent is expected to place {best_node.piece_to_place} at "
        #                     f"{best_node.parent_node.last_played_index} and pick {best_node.parent_node.piece_to_place}.")

        return TurnContext(best_node.grid, best_node.piece_to_place, best_node.remaining_pieces, best_node.last_played_index)

    """
        Get the node score.
    """
    def process_node(self, node, stats, selector):
        assert node.grid.has_winner() is False

        stats.depth += 1
        try:
            self.process_node2(node, stats, selector)
        finally:
            stats.depth -=1

    def process_node2(self, node, stats, selector):

        if stats.depth > Minimax.MAX_DEPTH:
            assert False
            return

        if self.create_child(node, stats, selector):
            node.score = selector.winning_score
            Minimax.logger.debug(f"{stats.prefix()} No need to go deeper, one child is winning. Score: {node.score}")
            return

        for child_node in node.children:
            if child_node.score == selector.winning_score:
                Minimax.logger.debug(f"{stats.prefix()} No need to process further, we already found a winning node on this path")
                assert False
                break
            if stats.depth < Minimax.MAX_DEPTH:
                Minimax.logger.debug(f"{stats.prefix()} Exploring playing {child_node.last_played_index} and selecting "
                                     f"{child_node.piece_to_place} for opponent.")
                self.process_node(child_node, stats, selector.get_next())
            else:
                child_node.score = selector.winning_score / 2  # TODO Random or better
                #Minimax.logger.debug(f"{stats.prefix()} Max depth reached, setting heuristic score {child_node.score}")

        best_node = selector.pick_best_node(node.children)
        Minimax.logger.debug(
            f"{stats.prefix()} Best node among {len(node.children)} children as score {best_node.score}. "
            f"{node.piece_to_place} at {best_node.last_played_index} and select {best_node.piece_to_place}.")

    """
        Create all the children of "node" (non-recursively) or until a winning node is created.
    """
    def create_child(self, node, stats, selector):

        # Special case for the last piece to place
        if len(node.remaining_pieces) == 0:
            assert len(node.grid.available_indexes) == 1
            new_grid = node.grid.place(node.piece_to_place, node.grid.available_indexes[0])
            new_node = Node(node, new_grid, None, list(), node.grid.available_indexes[0])
            stats.node_created += 1
            node.children.append(new_node)
            if new_grid.has_winner():
                new_node.score = selector.winning_score
                Minimax.logger.debug(f"{stats.prefix()} Last move wins for score of {new_node.score}.")
                return True
            return False

        for index in node.grid.available_indexes:
            new_grid = node.grid.place(node.piece_to_place, index)
            if new_grid.has_winner():
                # Create a winning  child node (selected piece unimportant)
                new_selected = node.remaining_pieces[0]
                new_remaining = node.remaining_pieces.copy()
                new_remaining.remove(new_selected)
                winning_node = Node(node, new_grid, new_selected, new_remaining, index)
                winning_node.score = selector.winning_score
                stats.node_created += 1
                node.children.append(winning_node)

                Minimax.logger.debug(f"{stats.prefix()} Move wins by placing {node.piece_to_place} at position {index}. "
                                     f"Score is {winning_node.score}.")
                return True

            for new_selected in node.remaining_pieces:
                new_remaining_pieces = node.remaining_pieces.copy()
                new_remaining_pieces.remove(new_selected)
                new_node = Node(node, new_grid, new_selected, new_remaining_pieces, index)
                stats.node_created += 1
                node.children.append(new_node)

        return False
