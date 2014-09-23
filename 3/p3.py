#!/bin/env python3

NUM_FACTOR = 600851475143

def prime_factors(n):
    factors = []
    num = 2

    while num < int(n**0.5) + 1:
    #while num*num <= n:
        while n % num == 0:
            factors.append(num)
            n /= num
        num += 1
    factors.append(int(n))
    return set(factors)
    #return factors

print("max factor: ", max(prime_factors(NUM_FACTOR)))
