"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError
    
    list = []
    num = 2
    while number_of_primes != 0:
        isPrime = True
        for i in range(2, num-1):
            if num % i == 0:
                isPrime = False
        if isPrime == True:
            list.append(num)
            number_of_primes -= 1
        num += 1
    return list

