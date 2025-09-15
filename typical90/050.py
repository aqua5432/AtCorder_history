import math
N, L = map(int, input().split())
syou = N // L
amari = N % L
count = 0
kazu = 10 ** 9 + 7
while syou > -1:
    goukei = syou + amari
    count += math.comb(goukei, syou)
    syou -= 1
    amari += L
print(count  % kazu)