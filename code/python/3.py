# Converted from notebook: 3.ipynb

# --- Cell 1 (markdown) ---
# # Problem - 3
# The prime factors of 13195 are 5, 7, 13 and 29
#
# What is the largest prime factor of the number 600851475143?
#

# --- Cell 2 (code) ---
import numpy as np

# --- Cell 3 (code) ---
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    if n <= 0:
        return False
    return all(n % i for i in range(3, int(np.sqrt(n)) + 1, 2))

def get_primes(end=1000, start=2):
    _primes = [_number for _number in range(start, end) if is_prime(_number)]
    return _primes

# --- Cell 4 (code) ---
def get_prime_factors_slowly(number):
    return [_prime for _prime in get_primes(number) if number % _prime == 0]

# --- Cell 5 (code) ---
def get_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            print(n, i)
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors 

# --- Cell 6 (code) ---
print(get_prime_factors(600851475143))
