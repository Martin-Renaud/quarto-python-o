from mastermind.sequence import Sequence
from mastermind.sequencefactory import SequenceFactory
from mastermind.sequencecomparator import compare
import random
import time

class Simul:

    def start(self):

        factory = SequenceFactory(nb_possible_value=6, length=4)

        hidden_seq = factory.create_random()
        guessed_seq = factory.create_random()

        print('Hidden Sequence:', hidden_seq)
        print('Initial guess  :', guessed_seq)
        print('=============================')
        timer_start = time.perf_counter()
        real_result = compare(hidden_seq, guessed_seq)
        print('Result  :', real_result)
        nb_attempts = 1
        candidate_list = list()
        for index in range(factory.nb_of_possible_sequence):
            candidate_seq = factory.create(index)
            result = compare(candidate_seq, guessed_seq)
            if result == real_result:
                candidate_list.append(candidate_seq)

        timer_end = time.perf_counter()
        pc = "{0:.1%}".format(1 - len(candidate_list)/factory.nb_of_possible_sequence)
        print(f"Initial pass selected %s candidate from all the %s existing. A %s reduction. Execution: {timer_end - timer_start:0.8f} s."
              % (len(candidate_list), factory.nb_of_possible_sequence, pc))

        guessed_seq = random.choice(candidate_list)
        while guessed_seq != hidden_seq:

            timer_start = time.perf_counter()
            nb_attempts += 1
            real_result = compare(hidden_seq, guessed_seq)
            print('-----------------------------')
            print('Next guess:', guessed_seq)
            print('Result    :', real_result)
            for candidate_seq in candidate_list:
                result = compare(candidate_seq, guessed_seq)
                if result != real_result:
                    candidate_list.remove(candidate_seq)
            timer_end = time.perf_counter()
            print(f"Now %s possibilities remaining. Execution: {timer_end - timer_start:0.8f} s." % len(candidate_list))
            guessed_seq = random.choice(candidate_list)
        print('=============================')
        print("Victory in %s attempt" % nb_attempts)



if __name__ == '__main__':

    Simul().start()

