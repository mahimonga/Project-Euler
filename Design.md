# Project-Euler

## Problem 1: Multiples of 3 and 5
1.  `multiples(limit, factors, union = True, intersection = False)`

    Returns a list of multiples under `limit` of any/all numbers in `factors`.

    union (*default* : `True`): If true, returns list of all multiples of any of numbers in `factors`.

    intersection (*default* : `False`): If true, returns list of multiples of all of numbers in `factors`.

    If both `intersection` and `union` are simultaneously:

    a. `False`, then list of list of all multiples of each factor in `factors` is returned

    b. `True`, then throws an exception.

    **Note**: Even though, `multiples()` appears to show similar functionalities to `filter_seq()`, it is not so as we pass only a single parameter to the condition function while filtering which is not the case with multiples as we take multiple inputs in `is_multiple()`. 

2. `is_multiple(n, factors, all = true)`

    Returns whether `n` is a multiple of all/any of numbers in `factors`

    all (*default* : `True`): 
    
    - If true, returns `True` if `n` is a multiple of all numbers in `factors` 

    - Else if false, returns `True` if `n` is a multiple of any number in `factors`

3. `sum_seq(seq)`
    Returns the sum of all numbers in `seq`

## Problem 2: Even Fibonacci Numbers
1. `fibonacci_seq(n, until = True, length = False)`

    Returns the fibonacci sequence of length `n` or until the value `n` is approached

    until (*default* : `True`): If true returns Fibonacci sequence until the no. `n` is reached.

    length (*default* : `False`): If true returns first `n` Fibonacci numbers.

    If both until and length are `False`, first `n` Fibonacci numbers are returned.

    If both until and length are `True`, method throws an exception.

2. `filter_seq(seq, condition = None, custom = None falsy = False)`

    Returns a list of values from `seq` obeying the given `condition`

    `condition` (*str*): Can take values: 
    - even
    - palindrome
    - prime

    `falsy` (*bool*): If true returns a list of values from seq not obeying the condition 

    `custom`: Pass a custom method which checks a condition. `filter_seq()` then returns a list of values which obey the condition in the custom method

3. `even(n)`

    Returns true if `n` is even.

## Problem 3: Largest Prime Factor
1. `factors(n, proper = True)`

    Returns the factors of an integer `n`.

    proper (*default* : True): If true, returns all proper factors (all factors including 1 and `n`) of `n` else return improper factors.

2. `prime(n)`

    Returns True if `n` is prime else returns False

3. `max_value(seq)`
    
    Returns the maximum value in a sequence `seq`.

## Problem 4: Largest Palindrome Product

1. `products(multipliers, num_of_multipliers = 2)`

    Returns the list of products of numbers from  `multipliers` taken `num_of_multipliers` at a time.

2. `palindrome(n)`

    Checks whether `n` is a palindrome or not.

## Problem 5: Smallest Multiple

1. `least_common_multiple(nums)`

    Returns the LCM of all numbers in nums.

2. `greatest_common_divisor(nums)`

    Returns the GCD of all numbers in nums.

## Problem 6: Sum square difference
1. `power_num(n, power)`

    Returns the value of `n` to the power `power`. 

2. `power_seq(seq, power)`

    Returns the list of all numbers in the `seq` raised to the power `power`

## Problem 7: 10001th Prime
1. `prime_seq(n, until = False, length = True)`
    
    Returns a seq of the first `n` prime numbers if `length` is `True` 
    
    Else if `until` is `True`, it returns a seq of prime numbers until the value approaches `n`

    If both `until` and `length` are `True`, then an exception is thrown.

    If both `until` and `length` are `True`, then the first `n` primes are returned.

2. `nth_number(n, num_type = "natural", custom_type = None)`

    Returns the `n`th `num_type` number

    `num_type` (*default* : "natural"): Type of nth number needed. Takes the values: "prime", "even", "odd", "palidrome"

    `custom_type` (*default* : None): pass a function to check the type of number. `nth_number()` then returns the nth number of type whose custom type is checked. 

## Problem 10: Summation of Primes
Uses the functions documented above

## Problem 11: 

## Problem 12:

## Problem 13: 

## Problem 14:


