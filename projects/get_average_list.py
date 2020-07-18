# Get the average

# import statistics

# num_list = [1, 2, 3, 4, 5, 6]

# print(statistics.mean(num_list))#> 3.5
# -----------------
# import numpy

# num_list = [1, 2, 3, 4, 5, 6]

# print(numpy.mean(num_list)) #> 3.5 aparently numpy is better performant than statistics
# ------------

#reduce
# my version
from functools import reduce

num_list = [1, 2, 3, 4, 5, 6]

adding = lambda first_num, next_num: first_num + next_num
reduced_list = reduce(adding, num_list)
average = reduced_list / len(num_list)
print(len(num_list)) #>6
print(reduced_list)#> 21
print(average)#> 3.5

print('-----------')
# Jordans version

# already imported reduce
number_list = [1, 2, 3, 4, 5, 6]
def get_average(number_list):
    total = reduce((lambda total , element:total + element), number_list)
    return total / len(number_list)

print(get_average(number_list))#>3.5