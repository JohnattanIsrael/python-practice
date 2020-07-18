# Order of operations
# calculation = 8 + 2 * 5 - ( 9 + 2 ) **2
# print(calculation)
"""
Please -> () parenthesis
Excuse -> ** exponents
My -> * multiplication
Dear -> / division
Aunt -> + addition
Sally -> - substraction

8 + 2 * 5 - ( 9 + 2 ) **2
8 + 2 * 5 - ( 11 ) **2
8 + 2 * 5 - 121
8 + 10 - 121
-103
"""

"""
print('Addition')
print(100 + 42)

print('Subtraction')
print(100 - 42)

print('Division')
print(100 / 42)
print(100 / 38)

print('Floor Division')
print(100 // 42)
print(100 // 38)

print('Multiplication')
print(100 * 42)

print('Modulus')
print(100 % 42)

print('Exponents')
print(100 ** 42)
"""
"""
Tools
-math library
-sorted function
-list slicing
-computations
"""
import math

sale_prices = [
    100,
    83,
    220,
    40,
    100,
    400,
    10,
    1,
    3,
]
sorted_prices = sorted(sale_prices)
sorted_prices_list = [str(item) for item in sorted_prices]

media_index = math.ceil(len(sorted_prices_list)/2)-1

media = sorted_prices_list [media_index]

print(media_index)
print(sorted_prices)
print(sorted_prices_list)
print(media + '-------- ')

sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)
first_sale_items =sorted_list[:half_slice]
last_sale_items =sorted_list[-half_slice:]
median = sorted_list[half_slice:half_slice + 1]


print(sorted_list)
print(num_of_sales)
print(first_sale_items)
print(last_sale_items)

print(median)
print('---------')
from decimal import Decimal
# Decimal('4.20') % 1
# Decimal('0.20')
# Decimal(str(n)) % 1

price = 3.20

old_decimal = Decimal(price) % 1
print(float(price) - float(old_decimal) + 0.99)


print(float(price))












