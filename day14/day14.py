# Part 1
def decode1(number: int, mask: str) -> int:
    # To apply zeroes, we need to perform &
    # To apply ones, we need to perform |
    mask_for_0 = ''
    mask_for_1 = ''
    for digit in mask:
        digit0 = '0' if digit == '0' else '1'
        digit1 = '1' if digit == '1' else '0'
        mask_for_0 += digit0
        mask_for_1 += digit1

    mask_for_0 = int(mask_for_0, 2)
    mask_for_1 = int(mask_for_1, 2)
    return number & mask_for_0 | mask_for_1


def exercise1():
    memory = dict()

    f = open('ex14.txt', 'rt')
    lines = f.read().splitlines()
    f.close()

    for line in lines:
        mask_or_location, value = line.split(' = ')
        if mask_or_location == 'mask':
            mask = value
            continue
        else:
            location = mask_or_location[4:-1]
        number_masked = decode1(int(value), mask)
        memory.update({location: number_masked})

    print(sum(memory.values()))


# Part 2


def decode2(address: int, mask: str) -> str:
    binary_adress = bin(address)[2:]
    # add leading zeroes
    result = '0' * (36 - len(binary_adress)) + binary_adress
    changed = ''
    for i, digit in enumerate(mask):
        if digit == '0':
            changed += result[i]
        else:
            changed += digit

    return changed


def resolve_floattness(floating_address: str, resulting_list: list) -> list:
    '''
  Recursive function. For each 'X' in the number gives two variants: with '0' and with '1'. Returns list of resolved numbers
  '''
    X = floating_address.count('X')
    if X == 0:
        resulting_list.append(int(floating_address, 2))
    else:
        position = floating_address.index('X')
        result1 = floating_address[0:position] + '0' + floating_address[
            position + 1:]
        result2 = floating_address[0:position] + '1' + floating_address[
            position + 1:]
        resolve_floattness(result1, resulting_list)
        resolve_floattness(result2, resulting_list)
        return resulting_list


def exercise2():
    memory = dict()

    f = open('ex14.txt', 'rt')
    lines = f.read().splitlines()
    f.close()

    for line in lines:
        mask_or_location, value = line.split(' = ')
        if mask_or_location == 'mask':
            mask = value
            continue
        else:
            location = mask_or_location[4:-1]
        decoded_address = decode2(int(location), mask)
        resolved_addresses = resolve_floattness(decoded_address, [])
        for address in resolved_addresses:
            memory.update({address: int(value)})

    print(sum(memory.values()))


exercise1()

exercise2()
