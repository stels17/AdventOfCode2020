from datetime import datetime


######################## PART 1 ######################

class NumberSpoken:
    def __init__(self, number: int, spoken_at: int):
        self.number = number
        self.spoken_last = spoken_at
        self.spoken_before = 0

    def spoken_again(self, round: int):
        self.spoken_before = self.spoken_last
        self.spoken_last = round


def play_round(all_spoken_numbers: dict, previous_number: NumberSpoken,
               round: int):

    if previous_number.spoken_before == 0:
        reply = 0
    else:
        # that number had been spoken before
        reply = previous_number.spoken_last - previous_number.spoken_before

    if reply not in all_spoken_numbers.keys():
        # print ('And this is a new number!')
        all_spoken_numbers.update({reply: NumberSpoken(reply, round)})
    else:
        all_spoken_numbers[reply].spoken_again(round)

    return reply


def play_game(all_spoken_numbers: dict, sequence: list, round: int):

    while round != 2021:
        previous_number = all_spoken_numbers[sequence[-1]]
        sequence.append(play_round(all_spoken_numbers, previous_number, round))
        round += 1

    return sequence


def exercise1():
    f = open('ex15.txt', 'rt')
    starting_numbers = list(map(int, f.read().strip().split(',')))
    f.close()

    all_spoken_numbers = dict()
    sequence = []
    # Read starting numbers spoken
    for i, starting_number in enumerate(starting_numbers):
        number_object = NumberSpoken(starting_number, i + 1)
        sequence.append(starting_number)
        all_spoken_numbers.update({starting_number: number_object})

    play_game(all_spoken_numbers, sequence, len(starting_numbers) + 1)

    print("2020th number: ", sequence.pop())



######################## PART 2 ######################

class AllSpokenNumbers:
    def __init__(self):
        # Reserve the first element for 0
        self.all_numbers = {0: NumberSpoken(0, 0)}

    def already_spoken_numbers(self):
        return self.all_numbers.keys()

    def add_number(self, number: int, round: int):
        new_number = NumberSpoken(number, round)
        self.all_numbers.update({number: new_number})
        return new_number

    def zero_spoken(self, round: int):
        self.all_numbers[0].spoken_again(round)
        return self.all_numbers[0]

    def existing_number_spoken(self, number: int, round: int):
        number_object = self.all_numbers[number]
        number_object.spoken_again(round)
        return number_object


def play_round2(all_spoken: AllSpokenNumbers, previous_number: NumberSpoken,
                round: int):

    if not previous_number.spoken_before:
        return all_spoken.zero_spoken(round)

    # That number had been spoken before
    reply = previous_number.spoken_last - previous_number.spoken_before

    if reply in all_spoken.already_spoken_numbers():
        return all_spoken.existing_number_spoken(reply, round)
    # new number
    return all_spoken.add_number(reply, round)


def play_game2(all_spoken: AllSpokenNumbers, previous_number: NumberSpoken,
               round: int):
    while round != 30000001:  #2000000:  #2021:
        previous_number = play_round2(all_spoken, previous_number, round)
        round += 1

    return previous_number.number


def exercise2():
    f = open('ex15.txt', 'rt')
    starting_numbers = list(map(int, f.read().strip().split(',')))
    f.close()

    all_spoken = AllSpokenNumbers()

    # Read starting numbers spoken
    for i, starting_number in enumerate(starting_numbers):
        all_spoken.add_number(starting_number, i + 1)

    that_number = play_game2(all_spoken, all_spoken.all_numbers[starting_number],
                             len(starting_numbers) + 1)

    print("30000000th number spoken: ", that_number)


d = datetime.now()
exercise1()
exercise2()
delta = datetime.now() - d
print("Total time:", delta)
