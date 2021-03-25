from context import TurnContext
import random

class Player:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def play(self, turn_context):
        pass


