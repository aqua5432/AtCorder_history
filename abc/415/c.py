"""import itertools
t = int(input())# 4*10^4
for _ in range(t):
    n = int(input()) #18以下
    s = input()
    s_num = list(s) # 5 * 10^5を超えない = 20 * 10^9は超えない
    danger_list = []
    medi_num = []
    medi_list = [[]]
    if int(s_num[-1]) == 1:
        print("No")
        continue
    for i in range(len(s_num)):
        if int(s_num[i]) == 1:
            x = i+1
            y = format(x, 'b')
            w = list(y)
            z = len(w)
            index = z
            for j in range(z):
                index -= 1
                if int(w[index]) == 1:
                    medi_num.append(j+1)
            danger_list.append(medi_num)
            medi_num = []
    vec = [i for i in range(1, n + 1)]
    flag = False
    for perm in itertools.permutations(vec):
        perm_list = []
        judge = True
        for k in range(len(perm)):
            perm_list.append(perm[k])
            perm_list.sort()
            if perm_list in danger_list:
                judge = False
        if judge:
            flag = True
    if flag:
        print("Yes")
    else:
        print("No")
"""
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    s = '0' + s  # 1-indexed にするため先頭に '0' を追加
    ok = [0] * (1 << n)
    ok[0] = 1  # 空集合はOK

    for i in range(1 << n): #1<<n = 2^n
        if ok[i] == 0:
            continue
        for j in range(n):
            if i & (1 << j):
                continue
            next_state = i | (1 << j)
            if s[next_state] == '0':
                ok[next_state] = 1

    if ok[(1 << n) - 1]:
        print("Yes")
    else:
        print("No")
