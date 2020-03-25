def genPrimes():
    x = 1
    primes = [2]
    num = 1
    while True:
        num += 2
        if all((num % n != 0) for n in primes):
            yield primes[-1]
            primes.append(num)
