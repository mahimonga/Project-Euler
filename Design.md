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
1. `generate_seq(n, until = True, length = False, seq_type = "natural_no")`

    Returns a sequence of type `seq_type` of length `n` or until the value `n` is approached

    until (*default* : `True`): If true returns sequence until the no. `n` is reached.

    length (*default* : `False`): If true returns first `n` numbers in the seq.

    seq_type (*default* : `"natural_no"`): Defines the type of the sequence required. Takes values:
    
    - "fibonacci"
    - "natural_no"
    - "triangular"
    - "collatz"
    - "prime"
    - "even"
    - "palindrome"
    - "odd"


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
1. `factors(nums, proper = True, separate = True, union = False, intersection = False)`

    Returns the factors of all numbers in `nums`.

    union (*default* : `True`): If true, returns list of all factors of any of numbers in `nums`.

    intersection (*default* : `False`): If true, returns list of factors of all of numbers in `nums`.

    If both `intersection` and `union` are simultaneously:

    a. `False`, then list of list of all factor of each no. in `nums` is returned

    b. `True`, then throws an exception.

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
1. `nth_number(n, num_type = "natural", custom_type = None)`

    Returns the `n`th `num_type` number

    `num_type` (*default* : "natural"): Type of nth number needed. Takes the values: "prime", "even", "odd", "palidrome"

    `custom_type` (*default* : None): pass a function to check the type of number. `nth_number()` then returns the nth number of type whose custom type is checked. 

## Problem 10: Summation of Primes
Uses the functions documented above

## Problem 11: Largest product in a grid
1. `columns(grid)`
    
    Returns the columns of a grid.

2. `rows(grid)`

    Returns the rows of a grid.

3. `diagonals(grid)`

    Returns the elements along slants of a grid.

## Problem 12: Highly divisible triangular number
1. `no_of_factors_seq(seq)`

    Returns the list of no. of factors of each value in a sequence.

## Problem 13: Large sum
1. `first_n_digits(num, n)`

    Returns the list of the first `n` digits of a number `num`

## Problem 14: Longest Collatz sequence
1. `size_seq(limits, type = "natural_nos")`
    
    Returns a list of sizes of all sequences having their limit in `limits`.

    type (*default* : "natural_nos"): Defines type of a seq. Can take the values:

    - "fibonacci"
    - "natural_no"
    - "triangular"
    - "collatz"
    - "prime"
    - "even"
    - "palindrome"
    - "odd"

