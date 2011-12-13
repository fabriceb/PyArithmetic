"""
This module is a collection of functions related to prime manipulation
and prime-related arithmetic operations

Copyright 2011 Fabrice Bernhard <fabriceb at theodo.fr>
"""

_primes = [2, 3, 5, 7]

def isprime(n):
    """Tests primality

    >>> isprime(157)
    True
    >>> isprime(157 * 13)
    False

    """
    for p in primes():
        if not n % p:
            return False
        if p ** 2 > n:
            return True

def primes():
    """Generates the list of all primes

    >>> someprimes = []
    >>> for p in primes():
    ...     if p > 30: break    
    ...     someprimes.append(p)
    >>> print someprimes
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    """
    global _primes
    for n in _primes: yield n
 
    n = _primes[-1]
    while True:
        n += 2
        for x in _primes:
            if not n % x:
                break
            if x ** 2 > n:
                _primes.append(n)
                yield n
                break

def primedividers(n):
    """Generates the prime decomposition as a list

    >>> [p for p in primedividers(36)]
    [2, 2, 3, 3]

    """
    for p in primes():
        if p ** 2 > n:
            break
        while n % p == 0:
            yield p
            n /=p
    if n > 1:
        yield n

def primedecomposition(n):
    """Returns the prime decomposition as a dictionary
    with primes as key and their exponent as value

    >>> primedecomposition(36)
    {2: 2, 3: 2}

    """
    decomposition = {}
    for factor in primedividers(n):
        if not factor in decomposition:
            decomposition[factor] = 0
        decomposition[factor] += 1

    return decomposition

def numdividers(n):
    """Returns the number of dividers

    For example for 28, the answer is 6: 1, 2, 4, 7, 14, 28
    >>> numdividers(28)
    6
    >>> numdividers(95558400)
    432

    """
    decomposition = primedecomposition(n)

    num = 1
    for prime in decomposition:
        num *= decomposition[prime] + 1

    return num
