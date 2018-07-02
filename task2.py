import string
import random

def add_sequence(sequence):
    dict_sequence[sequence] = dict_sequence.get(sequence, 0) + 1

def check_sequence(first, second, third):
    if dict_sequence.get(third, 0) > 40000 - 1:
        return False
    if dict_sequence.get(second + third, 0) > 2000 - 1:
        return False
    if dict_sequence.get(first+second+third, 0) > 100 - 1:
        return False
    return True

if __name__ == '__main__':
    abc = string.ascii_lowercase

    dict_sequence = {}

    first = random.choice(abc)
    add_sequence(first)

    second = random.choice(abc)
    add_sequence(second)

    add_sequence(first + second)

    long_string = first + second

    j = 3
    while j < 1000001:
        third = random.choice(abc)
        if not check_sequence(first, second, third):
            continue
        long_string += third
        add_sequence(third)
        add_sequence(second+third)
        add_sequence(first+second+third)

        first = second

        second = third

        if j / 10000 == j // 10000: #check status
            print(j)
        j += 1

    print(long_string)

    print(dict_sequence)