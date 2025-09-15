n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
count = 0
for i in range(n):
    if ab[i][1] > ab[i][0]:
        count += 1
print(count)