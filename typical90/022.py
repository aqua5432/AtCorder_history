def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a, b, c = map(int, input().split())
#1辺が1なら切断回数は(a-1)+(b-1)+(c-1)
#1辺が2なら切断回数は(a/2-1)+(b/2-1)+(c/2-1)
#1辺がnなら切断回数は(a/n-1)+(b/n-1)+(c/n-1)※nはa, b, cの最大公約数
min_num = min(a, b, c)

n = gcd(gcd(a, b), c)
print(a//n + b//n + c//n -3)