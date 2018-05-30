#euler 35
import sqlite3

conn = sqlite3.connect('primes.db')
cur = conn.cursor()
primes = ['2']

def getprimes():
    print('Collecting primes from DB. Please wait...')
    for row in cur.execute('''select prime from primes where prime<1000000'''):
        if not row in primes and '0' not in str(row) and '2' not in str(row) and '4' not in str(row) and '6' not in str(row)and '8' not in str(row):
            primes.append(str(row[0]))
            #print('adding',row[0], 'to list')

            
def cycle(prime):
    cyclelist = list()
    primestr = str(prime)
    for i in range(len(primestr)):
        cyclelist.append(primestr)
        primestr = primestr[-1] + primestr[:len(primestr)-1]
    return cyclelist


print('Loading Prime list')
getprimes()
print(primes)

print('checking primes')
for prime in primes:
    print('trying',prime)
    print(set(cycle(prime)).intersection(primes))
    if set(cycle(prime)).intersection(primes) == set(cycle(prime)):
        print('These worked!', cycle(prime))
    else:
        primes.remove(prime)
        print('removed',prime)
    

print('here is what is in the list',primes)
print(len(primes))

