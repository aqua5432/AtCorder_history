n, p, q = map(int, input().split())
a = list(map(int, input().split()))
count = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j + 1, n):
            for l in range(k+1, n):
                for m in range(l+1, n):
                    #数字がでかくなりすぎると実行時間が長くなるから、こまめに計算して数字を小さくする!+pythonで実行時間超過するならPyPyに切り替えてみる!
                    if ((((a[i]*a[j]%p)*a[k]%p)*a[l]%p)*a[m]%p) == q:
                        count+=1
print(count)