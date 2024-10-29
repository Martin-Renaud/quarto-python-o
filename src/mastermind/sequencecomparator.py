import time

from mastermind.sequence import Sequence


def compare(seq1, seq2):
    assert seq1.factory is seq2.factory


    str1 = str(seq1)
    str2 = str(seq2)
    perfect = 0
    str1Others = {}
    str2Others = {}
    for idx in range(0, len(str1)):
        if str1[idx] == str2[idx]:
            perfect += 1
        else:
            str1Others[str1[idx]] = str1Others.get(str1[idx], 0) + 1
            str2Others[str2[idx]] = str2Others.get(str2[idx], 0) + 1
    common_keys = str1Others.keys() & str2Others.keys()
    almost = 0
    for k in common_keys:
        almost = almost + min(str1Others[k], str2Others[k])

    # timer_start = time.perf_counter_ns()
    # timer_end = time.perf_counter_ns()
    # print(f"sequencecomparator.compare: Temp execution: {timer_end - timer_start:0.10f} seconds.")
    return perfect, almost
    #, timer_end - timer_start
