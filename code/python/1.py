# Converted from notebook: 1.ipynb

# --- Cell 1 (markdown) ---
# # Problem - 1
#
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# --- Cell 2 (markdown) ---
# ### Specific Solution

# --- Cell 3 (code) ---
answer = sum([_n for _n in range(1000) if _n % 3 == 0 or _n % 5 == 0])
print(answer)

# --- Cell 4 (markdown) ---
# ### General Solution

# --- Cell 5 (code) ---
def get_multiples(upper_limit, *multiples, lower_limit=0):
    """Returns the sum of all natural numbers between lower and upper limit that are divisible by the listed multiples

    Parameters
    ----------
    upper_limit : int
        should be greater than 0
    lower_limit : int, optional
        should be greater than 0 and less than upper_limit, by default 0

    Returns
    -------
    int
        sum of numbers divisible by the multiples between the specified range
    """
    return [_n for _n in range(lower_limit, upper_limit) if any(_n % divisor == 0 for divisor in multiples)]

# --- Cell 6 (code) ---
print(sum(get_multiples(1000, 3, 5)))
