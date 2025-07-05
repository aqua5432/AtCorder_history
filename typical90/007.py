from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
q = int(input())
a.sort()#O(nlogn)
for j in range(q):#O(3*10^5)
    b = int(input())
    """if n < 1000:
        minNum = abs(a[0]-b)
        for i in range(1, n):
            calcNum = abs(a[i]-b)
            if minNum > calcNum:
                minNum = calcNum
        print(minNum)
    else:
        index = 0
        #aのリストを1000分割して、どの位置の近くにいるのかを判定し、その近くのみ探索
        for i in range(1000):
            if b <= a[i*n//1000]:
                index = i-1
                break
        minNum = abs(a[0]-b)
        for i in range(index*n//1000, (index+1)*n//1000):
            calcNum = abs(a[i]-b)
            if minNum > calcNum:
                minNum = calcNum
        print(minNum)"""
    index = bisect_left(a,b)#二分探索
    res = 2 ** 60
    if index < n:
        res = min(res, abs(b - a[index]))
    if index > 0:
        res = min(res, abs(b - a[index-1]))
    print(res)