n, q = map(int, input().split())
a = list(map(int, input().split()))
index = 0
for i in range(q):
    t, x, y = map(int, input().split())
    if t == 1:
        x = (x + index-1) % n
        y = (y + index-1) % n
        num = a[x]
        a[x] = a[y]
        a[y] = num
    elif t == 2:
        index -= 1
    elif t == 3:
        indexnum = (x + index-1) % n
        print(a[indexnum])