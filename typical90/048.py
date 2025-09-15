"""
n, k = map(int, input().split())
#a_b = [list(map(int, input().split())) for _ in range(n)]
alist = []
blist = []
blistzip = []
for i in range(n):
    a, b = map(int, input().split())
    alist.append(a)
    blist.append(b)
zipped = sorted(zip(alist, blist), reverse=True)
a_sorted, b_sortedzip = zip(*zipped)
alist = list(a_sorted)
blist.sort(reverse=True)
blistzip = list(b_sortedzip)
print(alist)
print(blist)
print(blistzip)
time = 0
amount = 0
a_index = 0
b_index = 0
while(time < k):
    if blistzip.index(blist[b_index]) == a_index:
        b_index += 1
    if alist[a_index] >= 2*blist[b_index] and k-time > 1:
        time += 2
        amount += alist[a_index]
        a_index += 1
    else:
        time += 1
        amount += blist[b_index]
        b_index += 1
    print(amount)
    
print(amount)"""
#以下解説閲覧済み
# 入力の受け取り
N, K = map(int, input().split())
A = [0] * (1 << 18)
B = [0] * (1 << 18)
vec = []

# Step #1. 入力処理
for i in range(1, N + 1):
    a_i, b_i = map(int, input().split())
    A[i] = a_i
    B[i] = b_i
    vec.append(b_i)
    vec.append(a_i - b_i)

# Step #2. 大きい順にK個選んで加算
vec.sort(reverse=True)
Answer = sum(vec[:K])

# Step #3. 出力
print(Answer)