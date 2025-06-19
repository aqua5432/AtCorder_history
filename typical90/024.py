n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
#k回の操作でaをbに一致させる
#aとbの差の合計をkから引いてマイナスになる=k回だけでは入れ替えることができない
#aとbの差の合計をkから引いても正の偶数=(k-aとbの差の合計)/2回適当な箇所を+1-1すればよい
#奇数ならこれができないため、不可能

sum = 0
for i in range(n):
    sum += abs(a[i] - b[i])
if k - sum < 0:
    print("No")
elif (k - sum) % 2 == 0:
    print("Yes")
else:
    print("No")