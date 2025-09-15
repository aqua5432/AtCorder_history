T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    amount1 = 0
    for j in range(N):
        amount1 += (A[j]+B[j]) % M
    B.sort(reverse=True)
    amount2 = 0
    for j in range(N):
        amount2 += (A[j]+B[j]) % M
    B.sort()
    amount = 0
    for j in range(N):
        amount += (A[j]+B[j]) % M
    print(min(amount, amount1, amount2))