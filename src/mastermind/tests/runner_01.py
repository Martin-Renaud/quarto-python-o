from mastermind.sequence import Sequence
from mastermind.sequencefactory import SequenceFactory
from mastermind.sequencecomparator import compare
import random


class Runner:

    def run(self):



        factory = SequenceFactory(nb_possible_value=7, length=5)

        hidden_seq = factory.create_random()
        guessed_seq = factory.create_random()
