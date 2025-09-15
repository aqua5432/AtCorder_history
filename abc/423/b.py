N =int(input())
L = list(map(int, input().split()))
left = 0
right = 0
for i in range(N):
    look = L[i]
    if look == 1:
        left = i
        break
for i in range(N):
    look = L[N - i -1]
    if look == 1:
        right = N - i -1
        break
print(right -left)