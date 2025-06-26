def base_10(num_n,n):
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10

def base_n(num_10,n):
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return int(str_n[::-1])

def EtoF(a):
    s=0
    i=0
    while a>0:
        r=a%10
        if r == 8:
            r = 5
        s=s+r*10**i
        a=a//10
        i=i+1
    return s

n, k = map(int, input().split())

if n != 0:
    for i in range(k):
        n = base_10(n, 8)
        n = base_n(n, 9)
        n = EtoF(n)

print(n)