from functools import reduce
product = reduce(lambda x, y : x * y, range(1, 6))
print(product)