# MY WAY
from decimal import Decimal
import math
        
price = 3.20
old_decimal = Decimal(price) % 1
ninety_nine = 0.99
ninety_five = 0.95
new_price = float(price) - float(old_decimal) + ninety_five
# new_price = float(price) - float(old_decimal) + ninety_nine
# print(price)
# print(new_price)

def pretty_price(price, new_decimal):
    old_decimal = Decimal(price) % 1
    if math.ceil(price) == math.floor(price) + 1:
        new_price = float(price) - float(old_decimal) + new_decimal
    print(new_price)

pretty_price(3.20, ninety_five)
pretty_price(3.20, ninety_nine)
pretty_price(48.78, ninety_five)
pretty_price(107.53, ninety_nine)

# >>> from decimal import Decimal
# >>> Decimal('4.20') % 1
# Decimal('0.20')
# Decimal(str(n)) % 1
print('-----------')
# Jordans way

def pretty_prices(gross_price, extension):
    if isinstance(extension, int):
        extension = extension * 0.01
    return int(gross_price) + extension

print(pretty_prices(3.50, 0.95))
print(pretty_prices(3.50, 95))