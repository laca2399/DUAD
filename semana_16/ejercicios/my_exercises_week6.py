def sum_nums (param1):
    return sum (param1)

def turn_around_string(param1):
    return param1[::-1]

def count_mayus_minus(string):
    mayus = sum(1 for letter in string if letter.isupper())
    minus = sum(1 for letter in string if letter.islower())
    return mayus, minus

def sort_words(string):
    words = string.split("-")
    words.sort()
    result = "-".join(words)
    return result

def is_prime(num):
    if num < 2:
        return False
    for n in range (2,num):
        if num % n == 0:
            return False
    return True

def filter_pri(numbers):
    return [num for num in numbers if is_prime(num)]