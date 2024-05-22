#!/usr/bin/env python3

def print_fibonacci(length):
    # write fibonacci sequence of length length
    if length == 0:
        return []
    else:
        fibonacci_sequence = [0, 1]

        for i in range(2, length):
            fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])

        return fibonacci_sequence


print(print_fibonacci(0))