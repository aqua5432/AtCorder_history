X, C = map(int, input().split())
index = 0
i = X // 1000
for j in range(1, i):
    judge =(1000 + C) * j
    if judge <= X:
        index = j
print(1000 * index)