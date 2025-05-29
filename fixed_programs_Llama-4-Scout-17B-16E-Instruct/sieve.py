import math

def sieve(max_num):
    if max_num < 2:
        return []

    sieve_list = [True] * (max_num + 1)
    sieve_list[0:2] = [False, False]

    for current_prime in range(2, int(math.sqrt(max_num)) + 1):
        if sieve_list[current_prime]:
            for multiple in range(current_prime*2, max_num + 1, current_prime):
                sieve_list[multiple] = False

    return [num for num, is_prime in enumerate(sieve_list) if is_prime]