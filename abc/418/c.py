N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
sumA = sum(A)
sumAlist = []
sumAlistnum = []
for i in range(10**3):
    count1 = sumA
    count2 = 0
    for j in range(len(A)):
        if A[j] >= i:
            count1 -= A[j]
            count2 += 1
    sumAlist.append(count1)
    sumAlistnum.append(count2)
for i in range(10**3, 10**6+1):
    count1 = sumA
    count2 = 0
    for j in range(len(A)):
        if A[j] >= i:
            count1 -= A[j]
            count2 += 1
    sumAlist.append(count1)
    sumAlistnum.append(count2)
for i in range(Q):
    B = int(input())
    if max(A) < B:
        print(-1)
    else:
        index = B-1
        count = sumAlist[index] + (B-1)*sumAlistnum[index]
        print(count+1)