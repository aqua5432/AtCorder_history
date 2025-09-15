'''t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    fnum = s[0]
    lnum = s[n-1]
    s.sort()
    count = 2
    index = s.index(fnum)
    lastindex = s.index(lnum)
    maxindex = 1
    judge = True
    if index > lastindex:
        count += 1
        lastindex = n-1
        judge = False
    while(index < lastindex):
        if 2*s[index] < s[index+1]:
            if judge:
                count = -1
            else:
                count = 2
            break
        while(2*s[index] > s[index+maxindex]):
            maxindex += 1
            if index + maxindex > lastindex:
                break
        if index + maxindex == lastindex+1:
            break
        count += 1
        if maxindex > 1:
            maxindex -= 1
        index += maxindex
        maxindex = 1    
    print(count)'''

#模範回答
def solve():
    N = int(input())
    A = list(map(int, input().split()))

    used = [0] * N
    ans = 1
    last = 0

    while True:
        if A[last] * 2 >= A[N - 1]:
            ans += 1
            break

        nxt = -1
        for i in range(1, N):
            if used[i]:
                continue
            if A[last] * 2 >= A[i]:
                if nxt != -1 and A[nxt] >= A[i]:
                    continue
                nxt = i

        if nxt == -1 or A[nxt] <= A[last]:
            print(-1)
            return

        ans += 1
        last = nxt
        used[nxt] = 1

    print(ans)


T = int(input())
for _ in range(T):
    solve()
