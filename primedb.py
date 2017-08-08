import sqlite3

conn = sqlite3.connect('primes.db')
cur = conn.cursor()
primes = list()

def getprimes():
    print('Collecting primes from DB. Please wait...')
    for row in cur.execute('''select prime from primes'''):
        if not row in primes:
            primes.append(row[0])

def addprimes():
    remainders = list()
    n = primes[-1]
    print('starting at:', n)
    input("Any key to began")
    try:
        # for i in range(70):
        while True:
            n = n+1
            for prime in primes:
                remainders.append(n%prime)
            if not 0 in remainders and not n in primes:
                primes.append(n)
                print('found a prime!', n)
                print('Adding', n, 'to DB')
                cur.execute('INSERT INTO primes (prime) VALUES (?)', (n,))
            remainders = list()
    except KeyboardInterrupt:
        pass

def primestodb(primes):
    print('Adding to DB')
    for prime in primes:
        cur.execute('SELECT prime FROM primes WHERE prime = ?', (prime,))
        row = cur.fetchone()
        if row is None:
            print('Adding', prime, 'to DB')
            cur.execute('INSERT INTO primes (prime) VALUES (?)', (prime,))




getprimes()
addprimes()
# primestodb(primes)
print('Committing to DB. Please wait...')
conn.commit()
