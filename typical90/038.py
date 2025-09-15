import math
a, b = map(int, input().split())
num = math.lcm(a, b)
if num <= 10 ** 18:
    print(num)
else:
    print("Large")