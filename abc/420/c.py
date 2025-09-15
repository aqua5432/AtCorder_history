N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
anscheck = []
for i in range(N):
    ans += min(A[i], B[i])
    anscheck.append(min(A[i], B[i]))
for i in range(Q):
    c, x, v = input().split()
    X = int(x)
    V = int(v)
    if c == "A":
        A[X-1] = V
    else:
        B[X-1] = V
    a = anscheck[X-1]
    anscheck[X-1] = min(A[X-1],B[X-1])
    ans += (anscheck[X-1])-a
    print(ans)

