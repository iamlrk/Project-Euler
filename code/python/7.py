# Converted from notebook: 7.ipynb

# --- Cell 1 (markdown) ---
# # Problem - 7
# ### By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13. We can see that the 6th prime is 13. What is the 10,001st prime number?

# --- Cell 2 (code) ---
import numpy as np

# --- Cell 3 (markdown) ---
# #### Crude Method
# Only 101st Prime.

# --- Cell 4 (code) ---
def is_prime_no_optimisation(i):
    _j = i-1
    while _j > 1:
        if i % _j == 0:
            return False
        _j -= 1
    return True

# --- Cell 5 (code) ---
def is_prime_first_optimisation(i, primes):
    for _p in primes:
        if i % _p == 0:
            return False
    return True

# --- Cell 6 (code) ---
def progress_bar(current, total):
    return "[" + "_" * int(current*100/total) + "-" * (99 - int(current*100/total)) + "]"

# --- Cell 7 (code) ---
i = 1
a = []
limit = 101
while True:
    i += 1
    eval_current_number = is_prime_no_optimisation(i)
    # eval_current_number = is_prime_first_optimisation(i, a)
    if eval_current_number:
        print(f"Calculate {len(a)} prime Numbers - {progress_bar(len(a), limit)}", end="\r")
        a.append(i)
        if len(a) >= limit:
            print(f"Prime {i=}")
            break
    else:
        continue
print(a[-1])

# --- Cell 8 (markdown) ---
# The calculated answer from the no optimisation is 104743. Takes 3 min 22 sec to run.

# --- Cell 9 (code) ---
primes = [2, 3, 5]
limit = 10001
i = primes[-1]
while len(primes) < limit:
    i += 1
    if is_prime_first_optimisation(i, primes):
        print(f"Calculate {len(primes)} prime Numbers - {progress_bar(len(primes), limit)}", end="\r")
        primes.append(i)

print()
print(primes[-1])
