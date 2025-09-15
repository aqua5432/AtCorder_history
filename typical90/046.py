n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
count = 0
"""for i in range(n):
    for j in range(n):
        for k in range(n):
            if (a[i]+b[j]+c[k]) % 46 == 0:
                count += 1"""
#以下解説閲覧
a_mod = [0] * 46
b_mod = [0] * 46
c_mod = [0] * 46
for i in range(n):
    a_mod[a[i] % 46] += 1
    b_mod[b[i] % 46] += 1
    c_mod[c[i] % 46] += 1
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k) % 46 == 0:
                count += a_mod[i] * b_mod[j] * c_mod[k]
print(count)