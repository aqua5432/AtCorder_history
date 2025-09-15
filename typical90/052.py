N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
#解説閲覧
amount = []
for i in range(N):
    goukei = 0
    for j in range(6):
        goukei += A[i][j]
    amount.append(goukei)
count = 1
for i in range(N):
    count *= amount[i]
kazu = 10 ** 9 + 7
print(count % kazu)