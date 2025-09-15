from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

count = 0
mp = defaultdict(int)

for j in range(N):
    key = j - A[j]
    count += mp[key]       # 条件を満たす過去の i の数を加算
    mp[j + A[j]] += 1      # この j を次以降の i として記録

print(count)
