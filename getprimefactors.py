import primer
import math


def primefactors(primes, n):
    factors = list()
    for prime in primes:
        if n%prime == 0:
            print(n, 'devides by', prime)
            factors.append(prime)
    print(factors)

print('What shall I factor?')
n = primer.getint()
sqrt = round(math.sqrt(n))
print('Collecting primes less than', sqrt, 'please wait...')
primes = list()
primes.append(2)
primes = primer.addprimes(primes, sqrt)
primefactors(primes, n)
