# 1. Write a Python function to find the Max of three numbers
def max_num(a, b, c):
    return max([a, b, c])


# 2. Write a Python function to sum all the numbers in a list
def sum_list(nums):
    result = 0
    for num in nums:
        result += num
    return result


# 3. Write a Python function to multiply all the numbers in a list
def multiply_args(*args):
    result = 1
    for num in args:
        result *= num
    return result


# 4. Write a Python program to reverse a string.
def str_reverse(phrase):
    """
    This function takes as argument a string and reverses it
    :param phrase: str -> any text to be reversed
    :return: str
    """
    result = ""
    for i in range(1, len(phrase) + 1):
        result += phrase[-i]
    return result


# 5. Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.
def factorial(n):
    if n < 0:
        raise Exception("Negative number")
    if n == 0:
        return 0
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 6. Write a Python function to check whether a number is in a given range
def is_in_range(n, r):
    return n in r


# 7. Write a Python function that accepts a string and calculate the
# number of upper case letters and lower case letters
def count_upper_lower(s):
    count_upper = 0
    count_lower = 0
    for c in s:
        if not c.isalpha():
            continue
        if c.islower():
            count_lower += 1
        else:
            count_upper += 1
    return count_upper, count_lower


# 8. Write a Python function that takes a list and returns a new list with unique elements of the first list
def dedupe(lst):
    # return list(set(lst))
    result = []
    for val in lst:
        if val not in result:
            result.append(val)
    return result


# 9. Write a Python function that takes a number as a parameter and check the number is prime or not
def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True


# 10. Write a Python program to print the even numbers from a given list
def print_even(nums):
    for n in nums:
        if n % 2 == 0:
            print(n)


