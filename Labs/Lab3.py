"""
 String, List - Level 2.0
"""


def count_hi(string: str):
    """
    Return the number of times that the string "hi" appears anywhere in the given string.
    """
    nots = 0
    for i in range(len(string) - 1):
        if string[i:i+2] == 'hi':
            nots += 1
    return nots
    # return string.count('hi')



def cat_dog(string: str):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
    """
    cp = 0
    dp = 0
    for i in range(len(string) - 2):
        if string[i:i + 3] == 'cat':
            cp += 1
        elif string[i:i + 3] == 'dog':
            dp += 1
    # if cp == dp:
    #     return True
    # return False
    return cp == dp
    # return string.count('cat') == string.count('dog')


def count_code(string):
    """
    Return the number of times that the string "code" appears anywhere in the given string,
    except it'll accept any letter for the 'd', so 'cope' and 'cooe' count.
    """
    coxe = 0
    for i in range(len(string) - 3):
        if string[i:i + 2] == 'co' and string[i + 3] == 'e':
            coxe += 1
    return coxe


def end_other(a, b):
    """
    Given two strings, return True if either of the strings appears at the very end of the other string,
    ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
    Note: s.lower() returns the lowercase version of a string.
    """

    sa = a.lower()
    sb = b.lower()

    if len(a) > len(b):
        return sa[-(len(b)):] == sb
    elif len(a) < len(b):
        return sb[-(len(a)):] == sa
    return sa == sb
    # a = a.lower()
    # b = b.lower()
    # if len(a) < len(b):
    #     a, b = b, a
    # return a[-(len(b)):] == b


def count_evens(nums):
    """
    Return the number of even ints in the given list.
    Note: the % 'mod' operator computes the remainder, e.g. 5 % 2 is 1.
    """
    ep = 0
    for num in nums:
        if num % 2 == 0:
            ep += 1
    return ep
    # return len([i for i in nums if i % 2 == 0])


def big_diff(nums):
    """
    Given a list length 1 or more of ints, return the difference between the largest and smallest values in the array.
    Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
    """
    mx = mn = nums[0]
    for i in range(1, len(nums)):
        if mn > nums[i]:
            mn = nums[i]
        elif mx < nums[i]:
            mx = nums[i]
    return mx - mn
    # return max(nums) - min(nums)


def sum13(nums):
    """
    Return the sum of the numbers in the list, returning 0 for an empty array.
    Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
    """
    i = 0
    sum = 0
    while i < (len(nums)):
        if nums[i] != 13:
            sum += nums[i]
            i += 1
        else:
            i += 2
    return sum


def sum67(nums):
    """
    Return the sum of the numbers in the list, except ignore sections of numbers starting with a 6
    and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
    """
    # sum = i = 0
    # switch = True
    # while i < len(nums):
    #     if nums[i] == 6:
    #         switch = False
    #         i += 1
    #         continue
    #     if nums[i] == 7:
    #         switch = True
    #         i += 1
    #         continue
    #     if switch:
    #         sum += nums[i]
    #         i += 1
    # return sum
    sum = 0
    switch = True
    for num in nums:
        if num == 6 and switch:
            switch = False
            continue
        if num == 7 and not switch:
            switch = True
            continue
        if switch:
            sum += num
    return sum


def has22(nums):
    """
    Given a list of ints, return True if the array contains a 2 next to a 2 somewhere.
    """
    for i in range(len(nums) - 1):
        # if nums[i:i + 2] == [2,2]:
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False

