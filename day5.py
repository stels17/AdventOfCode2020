def get_seat_number(letters, begin=0, end=None):
    if end == None: end = 2**(len(letters)) - 1  # first call of func

    if len(letters) == 1:  # shall we stop
        if letters[0] in ['F', 'L']:
            return begin
        elif letters[0] in ['B', 'R']:
            return end
    # calculate the middle
    middle = (end - begin + 1) // 2
    # And then take lower(F|L) or upper(B|R) part
    direction = letters.pop(0)
    if direction in ['F', 'L']:
        end = begin + middle - 1
    elif direction in ['B', 'R']:
        begin = begin + middle
    return get_seat_number(letters, begin, end)


def strip_seats(seats):  # for task2
    '''
    Technically, not the best way of doing it...
    We'll just remove 'very front' seats
    '''
    if seats[1] - seats[0] == 1: return strip_seats(seats[1:])
    return seats[1]


def exercise():
    f = open("ex5.txt", "rt")
    lines = f.read().strip().split()
    f.close()

    highest_seat_number = 0  # for task1
    total_seats = list(range(0, 1024))  # for task2. All seats

    for line in lines:
        row_letters = line[:7]
        col_letters = line[-3:]
        row = get_seat_number(list(row_letters))
        col = get_seat_number(list(col_letters))
        seat = row * 8 + col
        if seat > highest_seat_number: highest_seat_number = seat
        total_seats.remove(seat)  # for task 2

    print(f"The highest seat: {highest_seat_number}")
    print("My seat:", strip_seats(total_seats))


exercise()
