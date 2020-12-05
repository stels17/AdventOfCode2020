def passport_validate_fields(passport_dict):
    # for task2. Fields format validation

    for key, value in passport_dict.items():
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if key == 'byr':
            if not 1920 <= int(value) <= 2002: return False
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        elif key == 'iyr':
            if not 2010 <= int(value) <= 2020: return False
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        elif key == 'eyr':
            if not 2020 <= int(value) <= 2030: return False
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        elif key == 'hcl':
            chars_a_f = map(lambda x: chr(x), range(ord('a'), ord('g')))
            allowed_chars = set(
                map(lambda x: str(x),
                    list(range(0, 10)) + list(chars_a_f)))
            if value[0] != '#' or len(value) != 7 or set(
                    value[1:]).difference(allowed_chars):
                return False
        #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        elif key == 'ecl':
            allowed_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if value not in allowed_colors: return False
        #pid (Passport ID) - a nine-digit number, including leading zeroes.
        elif key == 'pid':
            if len(value) != 9 or not value.isdigit(): return False
        # hgt (Height) - a number followed by either cm or in:
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76.
        elif key == 'hgt':
            cm = value[-2:] == 'cm' and 150 <= int(value[:-2]) <= 193
            inch = value[-2:] == 'in' and 59 <= int(value[:-2]) <= 76
            if not (cm or inch): return False

    return True


def exercise1():
    f = open("ex4.txt", "rt")

    all_data = f.read()
    f.close()

    mandatory_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    # step 1 - split passports from each other
    passports_raw_data = all_data.strip().split("\n\n")

    # step 2 - remove \n inside set of each passport's fields
    # and split key:value pairs of each passport
    passports_raw_data = list(
        map(lambda x: x.replace("\n", ' ').split(" "), passports_raw_data))
    # step 3 - create a dictionary from passport's key:value pairs

    valid_passports_count_task1 = 0
    valid_passports_count_task2 = 0

    for p in passports_raw_data:
        # set of keys of each passport
        passport_set = set(list(map(lambda x: x[:3], p)))
        if not mandatory_fields.difference(passport_set):
            valid_passports_count_task1 += 1
            # lets create a dict for each passport and check it
            passport_dict = dict(list(map(lambda x: x.split(':'), p)))
            if passport_validate_fields(passport_dict):
                valid_passports_count_task2 += 1

    print(f'Valid passports, task 1: {valid_passports_count_task1}')
    print(f'Valid passports, task 2: {valid_passports_count_task2}')


exercise1()
