# Converted from notebook: 4.ipynb

# --- Cell 1 (markdown) ---
# # Problem 4
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$
# Find the largest palindrome made from the product of two $3$-digit numbers.

# --- Cell 2 (code) ---
import numpy as np

# --- Cell 3 (code) ---
# reverse order of the list of palindrome numbers between 10k and 100k
list_of_palindrome_6_digits = [_number for _number in range(10_000, 1_00_000) if str(_number) == str(_number)[::-1]][::-1]

# --- Cell 4 (code) ---
