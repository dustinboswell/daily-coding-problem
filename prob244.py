'''
The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).
'''

from collections import defaultdict

def iter_primes():
    number_to_prime_divisors = defaultdict(list)  # n -> which primes divides it, if any
    n = 2
    while True:
        prime_divisors = number_to_prime_divisors[n]
        if not prime_divisors:
            yield n
            number_to_prime_divisors[2 * n].append(n)
        else:
            for p in prime_divisors:
                number_to_prime_divisors[p + n].append(p)

        del number_to_prime_divisors[n]
        n += 1

def iter_primes_slow():
    n = 2
    while True:
        if not any(n % i == 0 for i in range(2, n)):
            yield n
        n += 1

from itertools import islice

assert list(islice(iter_primes(), 1000)) == list(islice(iter_primes_slow(), 1000))
