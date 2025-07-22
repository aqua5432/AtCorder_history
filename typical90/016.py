n = int(input())
a = list(map(int, input().split()))
count = 10000
answer = count
"""for i in range(count):
    for j in range(count):
        for k in range(count):
            if a[0] * i + a[1] * j + a[2] * k != n:
                continue
            if answer > i + j + k:
                answer = i + j + k"""
for i in range(count):
    for j in range(count):
        z = a[0] * i + a[1] * j
        x = (n - z) % a[2]
        y = (n - z) // a[2]
        if x != 0 or z> n:
            continue
        if answer > i + j + y:
            answer = i + j + y
print(answer)

