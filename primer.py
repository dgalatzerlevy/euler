import math
# import datetime

primes = list()
primes.append(2)
#Eratosthenes method to get a list of primes as high as n. Ok for n < 10000
def eratos(n):
    numbers = list()
    primes = list()
    for i in range(2,n+1):
        primes.append(i)
    for prime in primes:
        for i in range(prime+1, n+1):
            if i%prime == 0 and i in primes:
                primes.remove(i)
    return primes

#A method of adding primes to your list though brute force

def addprimes(primes, counts):
    remainders = list()
    n = primes[-1]
    print('starting at:', n)
    for i in range(counts):
        n = n+1
        # print('checking:', n)
        # if n in primes:
        #     print(n, 'is a known Prime')
        for prime in primes:
            # print(n, '/',prime)
            remainders.append(n%prime)
            # if n%prime == 0:
            #     print(n, 'devides by', prime)
        if not 0 in remainders and not n in primes:
            # print(n, 'is a found prime')
            primes.append(n)
        # print(remainders)
        remainders = list()
    return primes

def getint():
    n = input('...')
    try:
        n = int(n)
        return(n)
    except:
        print("That's not an integer! Try again...")
        getint()


#
# def isPrime(n):
#     for i in range(2,round(n/2)):
#         if (n % i) == 0:
#             print(n, 'is divisable by', i, 'and', n/i, '... at least')
#             print("NOT PRIME!")
#             break

# print('How high should Eratosthenes go? (<10k)')
# n = getint()
# start = datetime.datetime.now()
# primes = eratos(n)
# print(len(primes), 'known primes <', n)
# print('Largest:',primes[-1])
# finish = datetime.datetime.now()
# print(finish-start)

# print('How high should we go?')

# n = getint()
# counts = n - primes[-1]
# start = datetime.datetime.now()
# addprimes(primes, counts)
# print(len(primes), 'known primes <',  n)
# print('Largest:',primes[-1])
# finish = datetime.datetime.now()
# print(finish-start)
