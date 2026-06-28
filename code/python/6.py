# Converted from notebook: 6.ipynb

# --- Cell 1 (markdown) ---
# # Problem - 6
# The sum of the squares of the first ten natural numbers is,
# $$1^2+2^2+\dots+10^2=385$$
# The square of the sum of the first ten natural numbers is,
# $$(1+2+\dots+10)^2=55^2=3025$$
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# $$3025-385=2640$$
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# --- Cell 2 (code) ---
import numpy as np

# --- Cell 3 (code) ---
def sum_n_numbers_math(n):
    return n*(n+1)/2

def sum_n_square_math(n):
    return n*(n+1)*(2*n+1)/6

def sum_n(end, start=0, increment=1):
    return np.sum(np.arange(start,end,increment))

def sum_n_square(end, start=0, increment=1):
    return np.sum([i**2 for i in np.arange(start,end,increment)])

# --- Cell 4 (code) ---
diff_math = sum_n_numbers_math(101)**2 - sum_n_square_math(101)
diff = sum_n(101)**2 - sum_n_square(101)
diff
