q = int(input())
n = []#整数列に保存される数字
m = []#整数列の保存されている数字の個数
listIndex = 0
for i in range(q):
    a = list(map(int, input().split()))
    if a[0] == 1:
        n.append(a[2])
        m.append(a[1])
    elif a[0] == 2:
        p = a[1]
        index = listIndex
        sum = 0
        while(p > 0):
            if m[index] >= p:
                sum += n[index] * p
                m[index] -= p
                p = 0
            else:
                sum += n[index] * m[index]
                p -= m[index]
                m[index] = 0
            index += 1
        count = 0
        for k in range(listIndex, index):
            if m[k] == 0:
                count += 1
        listIndex += count
        print(sum)    

