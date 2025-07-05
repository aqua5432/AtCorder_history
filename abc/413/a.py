n, m = map(int, input().split())
a = list(map(int, input().split()))
sum = 0
for i in range(n):
    sum += a[i]
if m >= sum:
    print("Yes")
else:
    print("No")