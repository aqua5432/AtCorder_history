n, m = map(int, input().split())
#ab = [list(map(int, input().split())) for _ in range(m)]
myset = set([])
myset2 = set([])
count = 0
for i in range(m):
    a, b = map(int, input().split())
    if max(a, b) in myset:
        if max(a,b) not in myset2:
            count += 1
            myset2.add(max(a,b))
    else:
        myset.add(max(a,b))
print(len(myset)-count)