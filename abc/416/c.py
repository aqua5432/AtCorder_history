n, k, x = map(int, input().split())
s = [input() for _ in range(n)]
slist = []
if k == 1:
    for i in range(n):
        slist.append(s[i])
elif k == 2:
    for i in range(n):
        for j in range(n):
            slist.append(s[i]+s[j])
elif k == 3:
    for i in range(n):
        for j in range(n):
            for l in range(n):
                slist.append(s[i]+s[j]+s[l])
elif k == 4:
    for i in range(n):
        for j in range(n):
            for l in range(n):
                for m in range(n):
                    slist.append(s[i]+s[j]+s[l]+s[m])
elif k == 5:
    for i in range(n):
        for j in range(n):
            for l in range(n):
                for m in range(n):
                    for o in range(n):
                        slist.append(s[i]+s[j]+s[l]+s[m]+s[o])
slist.sort()
print(slist[x-1])