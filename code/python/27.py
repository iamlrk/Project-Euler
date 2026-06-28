# Converted from notebook: 27.ipynb

# --- Cell 1 (markdown) ---
# # Question 27

# --- Cell 2 (markdown) ---
# Euler discovered the remarkable quadratic formula:
# $n^2 + n + 41$
# It turns out that the formula will produce $40$ primes for the consecutive integer values $0 \le n \le 39$. However, when $n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41$ is divisible by $41$, and certainly when $n = 41, 41^2 + 41 + 41$ is clearly divisible by $41$.
# The incredible formula $n^2 - 79n + 1601$ was discovered, which produces $80$ primes for the consecutive values $0 \le n \le 79$. The product of the coefficients, $-79$ and $1601$, is $-126479$.
# Considering quadratics of the form:
#
# > $n^2 + an + b$, where $|a| < 1000$ and $|b| \leq 1000$
# > 
# > where $|n|$ is the modulus/absolute value of $n$
# > 
# > e.g. $|11| = 11$ and $|-4| = 4$
#
# Find the product of the coefficients, $a$ and $b$, for the quadratic expression that produces the maximum number of primes for consecutive values of $n$, starting with $n = 0$.

# --- Cell 3 (code) ---
import numpy as np
import pandas as pd

# --- Cell 4 (code) ---
global MAX_A
global MAX_B
MAX_A = 999
MAX_B = 1000

# --- Cell 5 (code) ---
def progress_bar(current, total):
    return "[" + "_" * int(current*100/total) + "-" * (99 - int(current*100/total)) + "]"

# --- Cell 6 (code) ---
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    if n <= 0:
        return False
    return all(n % i for i in range(3, int(np.sqrt(n)) + 1, 2))

def get_primes(end=1000, start=2):
    _primes = [_number for _number in range(start, end) if is_prime(_number)]
    return _primes

# --- Cell 7 (code) ---
equation = lambda n, a, b: n**2 + a * n + b

# --- Cell 8 (code) ---
a = np.arange(-999,1000)
b = np.arange(-1000,1001)
# a = np.arange(-9,10)
# b = np.arange(-10,11)

# --- Cell 9 (code) ---
# Create a meshgrid
A, B = np.meshgrid(a, b)

# Flatten the arrays to get combinations
combinations = np.column_stack((A.flatten(), B.flatten()))

# --- Cell 10 (code) ---
equation = lambda n, a, b: n**2 + a * n + b

# --- Cell 11 (code) ---
def check_pair(_a, _b):
    equation = lambda n, a, b: n**2 + a * n + b
    consecutive = True
    length = 0
    while consecutive:
        for i in range(1, 1000):
            if is_prime(equation(i, _a, _b)):
                length += 1
                continue
            else:
                consecutive = False
                break
    return length+1

# --- Cell 12 (code) ---
print(f"{check_pair(-79, 1601) = }")
print(f"{check_pair(1, 41) = }")

# --- Cell 13 (code) ---
# values = [check_pair(__a, __b) for __a, __b in combinations]
values = [((__a, __b), check_pair(__a, __b)) for __a, __b in combinations]
max_value = max(values, key=lambda x: x[1])
print(max_value)
print(f"Result = {max_value[0][0]} X {max_value[0][1]} = {max_value[0][0]*max_value[0][1]}")
