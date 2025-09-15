n = int(input())
s = [input() for _ in range(n)]
slist = []
for i in range(n):
    for j in range(n):
        if i != j:
            splus = s[i] + s[j]
            if splus not in slist:
                slist.append(splus)
print(len(slist))