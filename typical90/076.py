"""N = int(input())
A = list(map(int, input().split()))
cakesize = sum(A)
if cakesize % 10 != 0:
    print("No")
else:
    piecesize = cakesize // 10
    judge = False
    for i in range(N):
        amount = 0
        index = 0
        while amount < piecesize:
            if i+index == N:
                index -= N
            amount += A[i+index]
            index += 1
        if amount == piecesize:
            judge = True
            break
    if judge:
        print("Yes")
    else:
        print("No")
"""
#回答
import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))
cakesize = sum(A)

if cakesize % 10 != 0:
    print("No")
    exit()

piecesize = cakesize // 10

# 配列を2倍にして環状を直線化
A = A * 2
S = [0]
for x in A:
    S.append(S[-1] + x)

# 判定
seen = set(S)
for s in S[:N]:
    if s + piecesize in seen:
        print("Yes")
        break
else:
    print("No")