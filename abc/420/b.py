N, M= map(int, input().split())
S = [list(input()) for _ in range(N)]
people = []
ans = []
for i in range(N):
    people.append(0)
for i in range(M):
    judge = []
    for j in range(N):
        judge.append(S[j][i])
    y = judge.count('1')
    x = judge.count('0')
    if x == 0 or y == 0:
        for k in range(N):
            people[k] += 1
    elif x < y:
        for k in range(N):
            if judge[k] == '0':
                people[k] += 1
    else:
        for k in range(N):
            if judge[k] == '1':
                people[k] += 1
maxnum = max(people)
for i in range(N):
    if maxnum == people[i]:
        ans.append(i+1)
print(*ans)
