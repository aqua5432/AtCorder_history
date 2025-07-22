a, b, c = map(int, input().split())
judge = 1
for _ in range(b):
    judge *= c
if a < judge:
    print("Yes")
else:
    print("No")