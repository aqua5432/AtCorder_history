n = int(input())
A = list(map(int, input().split()))
x = int(input())
judge = False
for i in range(n):
    if A[i] == x:
        judge = True
if judge:
    print("Yes")
else:
    print("No")