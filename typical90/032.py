import itertools
import sys
sys.setrecursionlimit(10**7)
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
xy = [list(map(int, input().split())) for _ in range(m)]
# 道の走り方の全パターン10! = 3.6288 * 10^6(n = 10のとき)
# 以下解説閲覧し、記述
mintime = float('inf')# 無限大
kenaku = [[False] * (n+1) for i in range(n+1)]
for i in range(m):
    kenaku[xy[i][0]][xy[i][1]] = True
    kenaku[xy[i][1]][xy[i][0]] = True
vec = []
for i in range(1, n + 1):
    vec.append(i)
for perm in itertools.permutations(vec):
    flag = True
    for i in range(n-1):
        if kenaku[perm[i]][perm[i+1]]:
            flag = False
            break
    if flag:
        sum = 0
        for i in range(n):
            sum += a[perm[i]-1][i]
        mintime = min(mintime, sum)

if mintime == float('inf'):
    print(-1)
else:
    print(mintime)
        
