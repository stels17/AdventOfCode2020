from functools import reduce


def exercise1():
    f = open("ex6.txt", "rt")
    lines = f.read().strip().split('\n\n')
    f.close()

    total = 0

    for line in lines:
        quest_any_answered_yes = set(line.replace('\n', ''))
        total += len(quest_any_answered_yes)

    print("Total:", total)


def exercise2():
    f = open("ex6.txt", "rt")
    lines = f.read().strip().split('\n\n')
    f.close()

    total = 0

    for line in lines:
        # we need to find intersections
        line_arr = line.split()
        quest_all_answered_yes = reduce(
            lambda acc, x: set(x).intersection(acc), line_arr,
            set(line_arr[0]))
        total += len(quest_all_answered_yes)

    print("Total:", total)


exercise1()
exercise2()
