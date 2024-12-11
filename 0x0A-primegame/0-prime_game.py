#!/usr/bin/python3

def sieve(n):
    """ Return a list of primes up to n using the Sieve of Eratosthenes. """
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]


def isWinner(x, nums):
    """ Determine the winner of the prime game. """
    maria_wins = 0
    ben_wins = 0
    max_n = max(nums)
    primes = sieve(max_n)

    for n in nums:
        prime_count = len([p for p in primes if p <= n])
        if prime_count % 2 == 1:  # Maria wins if the count of primes is odd
            maria_wins += 1
        else:  # Ben wins if the count of primes is even
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
