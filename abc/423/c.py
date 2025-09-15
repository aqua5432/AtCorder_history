"""N, R = map(int, input().split())
L = list(map(int, input().split()))
amount = 0
zerolist = []
for i in range(N):
    if L[i] == 0:
        amount += 1
        zerolist.append(i)
if zerolist ==[]:
    print(amount)
else:
    if R == N and L[R-1] == 1:
        amount += 2
    if R == 0 and L[0] == 1:
        amount += 2
    mi = min(zerolist)
    ma = max(zerolist)
    for i in range(1, N-1):
        if L[i] == 1:
            if i <= R:
                if mi < i:
                    amount += 2
            else:
                if ma > i:
                    amount += 2
    print(amount)"""
#以下回答例
N, R = map(int, input().split())
L = list(map(int, input().split()))

zerolist = [i for i, v in enumerate(L) if v == 0]

if not zerolist:
    print(0)
else:
    # 区間を決める（R は部屋番号なのでそのまま使う）
    left = min(R, zerolist[0])
    right = max(R, zerolist[-1] + 1)

    # 0 は1回、1は2回数える
    ans = sum(L[left:right]) + (right - left)
    print(ans)
