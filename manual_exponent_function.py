"""
We need to
manual_exponent(2, 3)
#>8

manual_exponent(10, 2)
#> 100
"""
from functools import reduce

def manual_exponent(number, exponent):
    computed_list = [number] * exponent
    return (reduce(lambda number, exponent: number * exponent, computed_list))


print(manual_exponent(2, 3))
print(manual_exponent(10, 2))

def example(num, exp):
    list = [num] * exp
    return(reduce(lambda total, element: total * element, list))
print(example(12, 2))
#>144
"""
from functools import reduce

def manual_exponent (number, exponent):
    counter = exponent - 1
    total = number

    while counter > 0:
        total *= number
        counter -= 1
        
    return total

print(manual_exponent(2, 3))
print(manual_exponent(10, 2))
"""


# import operator
# from functools import reduce

# """
# dynamic_reducer([1, 2, 3, 4]), '+') #10
# dynamic_reducer([1, 2, 3, 4]), '-') #-
# dynamic_reducer([1, 2, 3, 4]), '*') #
# dynamic_reducer([1, 2, 3, 4]), '/') #
# """
# def dynamic_reducer(collection, op):
#     operators = {
#         '+':operator.add,
#         '-':operator.sub,
#         '*':operator.mul,
#         '/':operator.truediv,
#     }

#     return reduce((lambda total, element:operators[op](total,element)),collection)

# # total= flexible_counter([1, 2, 3], '/') 

# print(dynamic_reducer([1, 2, 3], '+'))
# print(dynamic_reducer([1, 2, 3], '-'))
# print(dynamic_reducer([1, 2, 3], '*'))
# print(dynamic_reducer([1, 2, 3], '/'))

