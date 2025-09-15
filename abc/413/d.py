"""t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = a.copy()
    a = [abs(i) for i in a]
    a.sort()
    for j in range(n):
        if a[j] not in b:
            a[j] = a[j] * -1
    judge1 = True
    for j in range(1, n-1):
        if a[j + 1] != a[j] * a[1] // a[0]:
            judge1 = False
    if judge1:
        print("Yes")
    else:
        print("No")
"""
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    # すべて同じ値なら Yes(公比が1のとき)
    if A.count(A[0]) == N:
        print("Yes")
        continue

    # A[0] と -A[0] のみで構成されており、
    # 個数がそれぞれN/2なら Yes(公比が-1)
    pos = A.count(A[0])
    neg = A.count(-A[0])
    if pos + neg == N and min(pos, neg) == N // 2:
        print("Yes")
        continue

    # 絶対値の降順にソート
    A.sort(key=lambda x: abs(x), reverse=True)

    # 等比数列の条件を交差乗算でチェック（浮動小数誤差なし）
    ok = True
    for i in range(N - 2):
        if A[i] * A[i + 2] != A[i + 1] * A[i + 1]:
            ok = False
            break

    print("Yes" if ok else "No")

