N, Q = map(int, input().split())
A = list(map(int, input().split()))

L = [0] * Q
R = [0] * Q
V = [0] * Q
for i in range(Q):
    L[i], R[i], V[i] = map(int, input().split())

# Step #2. 初期計算
B = [0] * N
Answer = 0
for i in range(N - 1):
    B[i] = A[i + 1] - A[i]
    Answer += abs(B[i])

# Step #3. シミュレーション
for i in range(Q):
    l = L[i] - 1  # 0-index化
    r = R[i] - 1
    v = V[i]

    mae = abs(B[l - 1]) if l >= 1 else 0
    mae += abs(B[r]) if r < N - 1 else 0

    if l >= 1:
        B[l - 1] += v
    if r < N - 1:
        B[r] -= v

    ato = abs(B[l - 1]) if l >= 1 else 0
    ato += abs(B[r]) if r < N - 1 else 0

    Answer += (ato - mae)
    print(Answer)
