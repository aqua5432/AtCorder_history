from itertools import product
n = int(input())
a = "("
b = ")"
"""if n % 2 == 0:
    if n == 2:
        print("()")
    elif n == 4:
        print("()()")
        print("(())")
    elif n == 6:
        print("()()()")
        print("(())()")
        print("()(())")
        print("((()))")
    elif n == 8:
        print("()()()()")
        print("(())()()")
        print("()(())()")
        print("()()(())")
        print("((()))()")
        print("(())(())")
        print("()((()))")
        print("(((())))")
    elif n == 10:
        print("()()()()()")"""

for i in product(["(", ")"], repeat=n):#考えられるすべての()の文字列を長さn分作成
    count = 0
    judge = True
    for j in i:
        if j == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            judge = False
    if count != 0:
        judge = False
    if judge:
        print(*i, sep="")