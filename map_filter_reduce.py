# -------------------------------MAP---------------------------
from functools import reduce
print("Working of map function:")
num = [1, 2, 3, 4, 5]
ls = list(map(lambda x: x**2, num))
print(ls)

# ------------------------------FILTER-------------------------
print("Working of filter function")
ls = list(filter(lambda x: x % 2 == 0, num))
print(ls)
# ------------------------------REDUCE-------------------------
print("Working of reduce")
ls = reduce(lambda x, y: x*y, num)
print(ls)
