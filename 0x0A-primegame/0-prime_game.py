#!/usr/bin/python3
"""Module for isWinner function"""


def sieve_of_eratosthenes(n):
    """Return a list where each index is True if the index is a prime number"""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve


def isWinner(x, nums):
    """
    Determines and returns who wins the prime game by who wins the most rounds
    """
    if x < 1 or not nums:
        return None

    n = max(nums)
    sieve = sieve_of_eratosthenes(n)

    primes_count = [0] * (n + 1)
    count = 0

    for i in range(len(sieve)):
        if sieve[i]:
            count += 1
            primes_count[i] = count

    maria_rounds_won = 0
    ben_rounds_won = 0

    for round_of_num in nums:
        if primes_count[round_of_num] % 2 == 1:
            maria_rounds_won += 1
        else:
            ben_rounds_won += 1

    if maria_rounds_won > ben_rounds_won:
        return "Maria"
    elif ben_rounds_won > maria_rounds_won:
        return "Ben"
    else:
        return None
