
# Integer Datatype
product_id = 123
# Float a type of decimal that isn´t pescise
sale_price = 14.99
# Percentages
tip_percentage = 1/5
new_product = 150
print(sale_price + new_product)


from decimal import Decimal

product_cost = 88.40
commission_rate = 0.08
qty = 450

product_cost += (commission_rate*product_cost)
print(product_cost*qty) #42962.4

product_cost = Decimal(88.40)
commission_rate = Decimal(0.08)
qty = 450

product_cost += (commission_rate*product_cost)
print(product_cost*qty) #42962.40000000000282883716451

from decimal import Decimal

product_cost = Decimal(88.80)
commission_rate = (0.08)
qty = 450

print(int(product_cost))
print(float(qty))
print(Decimal(product_cost))
print(complex(commission_rate))