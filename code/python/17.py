# Converted from notebook: 17.ipynb

# --- Cell 1 (markdown) ---
# # Problem 17
# If the numbers $1$ to $5$ are written out in words: one, two, three, four, five, then there are $3 + 3 + 5 + 4 + 4 = 19$ letters used in total.
# If all the numbers from $1$ to $1000$ (one thousand) inclusive were written out in words, how many letters would be used? 
# NOTE: Do not count spaces or hyphens. For example, $342$ (three hundred and forty-two) contains $23$ letters 
# and $115$ (one hundred and fifteen) contains $20$ letters. 
# The use of "and" when writing out numbers is in compliance with British usage.

# --- Cell 2 (code) ---
ONES = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
TENS = {10: "ten", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
HUNDREDS = {_i * 100: " ".join([ONES[_i], "hundred"]).strip() for _i in range(1, 10)}
THOUSANDS = {_i * 1000: " ".join([ONES[_i], "thousand"]).strip() for _i in range(1, 10)}

# --- Cell 3 (code) ---
EXCEPTIONS = {11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",}

# --- Cell 4 (code) ---
HARD_CODED = ONES | TENS | HUNDREDS | THOUSANDS | EXCEPTIONS

# --- Cell 5 (code) ---
def seperate_digits(i):
    # calculating number of digits. and multiplying by hundred. There is -1 because there is   
    no_of_digits = 10 ** (len(str(i)) - 1)
    individual_digits = [int(_i) for _i in str(i)]
    denomination = [digit * no_of_digits // (10 ** index) for index, digit in enumerate(individual_digits)]
    return denomination

def number_to_text(i):    
    if i in HARD_CODED:
        return HARD_CODED.get(i)
    
    numbers = seperate_digits(i)
    
    teen_name = None
    # handling teens
    if numbers[-2] == 10:
        teens = numbers[-2] + numbers[-1]
        teen_name = HARD_CODED.get(teens)
    
    texts_ind = [HARD_CODED.get(_n) for _n in numbers]
    
    # handling till tens
    if teen_name is None:
        tens_place = " ".join(texts_ind[-2:])
    else:
        tens_place = teen_name
    
    # return if below tens
    if len(numbers) <= 2:
        return tens_place

    # handling from 100
    hundreds_place = " and ".join([texts_ind[-3], tens_place])
    
    if len(numbers) == 3: 
        return hundreds_place
    
    # from thousand
    # print(texts_ind[:-3])
    rest_places = " ".join(texts_ind[:-3])
    
    return rest_places + " " + hundreds_place

# --- Cell 6 (code) ---
texts = [number_to_text(_n) for _n in range(1,1001)]
nospaces = "".join("".join(texts).split(" "))
print(len(nospaces))

# --- Cell 7 (code) ---
print(seperate_digits(112))
print(number_to_text(122))
