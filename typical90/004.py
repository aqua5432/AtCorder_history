H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]
answer = [[0] * W for i in range(H)]

#できなかったところ
#事前に縦の合計と横の合計を出すとO(H * W)にできる!
#O(H * W * (H + W) )はタイムオーバー(Hに制約がないため)
rowSum = [sum(i) for i in A]
colSum = [sum(A[i][j] for i in range(H)) for j in range(W)]

for i in range(H):
    for j in range(W):
        answer[i][j] = rowSum[i] + colSum[j] - A[i][j]
for i in range(H):
    print(*answer[i])