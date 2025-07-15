"""def base_n(num_10,n):
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return int(str_n[::-1])


a = int(input())
n = int(input())
#回文の条件
#値の長さが奇数(3桁): 真ん中は変わらず、その横同士が同じ121,12321
#値の長さが偶数(4桁): 左右対称 2442, 123321
#回文のため、末尾に0がつくことはない
sum = 0
nlen = len(str(n))
for i in range(1, nlen+1):
    if i == 1:
        for j in range(1, 10):
            if j > n:
                break
            d = base_n(j,a)
            e = str(d)[::-1]
            if str(d) == e:
                sum += j
    elif i == 3:
        for j in range(1, 10):
            for k in range(10):
                ju = 100*j+10*k+j
                if ju > n:
                    break
                d = base_n(ju,a)
                e = str(d)[::-1]
                if str(d) == e:
                    sum += ju
    elif i == 5:
        for j in range(1, 10):
            for k in range(10):
                for l in range(10):
                    ju = 10000*j+1000*k+100*l+10*k+j
                    if ju > n:
                        break
                    d = base_n(ju,a)
                    e = str(d)[::-1]
                    if str(d) == e:
                        sum += ju
    elif i == 7:
        for j in range(1, 10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        ju = j*1000000+k*100000+l*10000+m*1000+100*l+10*k+j
                        if ju > n:
                            break
                        d = base_n(ju,a)
                        e = str(d)[::-1]
                        if str(d) == e:
                            sum += ju
    elif i == 9:
        for j in range(1, 10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        for o in range(10):
                            ju = j*100000000+k*10000000+l*1000000+m*100000+o*10000+1000*m+100*l+10*k+j
                            if ju > n:
                                break
                            d = base_n(ju,a)
                            e = str(d)[::-1]
                            if str(d) == e:
                                sum += ju
    elif i == 11:
        for j in range(1, 10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        for o in range(10):
                            for p in range(10):
                                ju = j*10000000000+k*1000000000+l*100000000+m*10000000+o*1000000+p*100000+o*10000+1000*m+100*l+10*k+j
                                if ju > n:
                                    break
                                d = base_n(ju,a)
                                e = str(d)[::-1]
                                if str(d) == e:
                                    sum += ju
    elif i == 2:
        for j in range(1, 10):
            ju = 10*j+j
            if ju > n:
                break
            d = base_n(ju,a)
            e = str(d)[::-1]
            if str(d) == e:
                sum += ju
    elif i == 4:
        for j in range(1, 10):
            for k in range(10):
                ju = 1000*j+100*k+10*k+j
                if ju > n:
                    break
                d = base_n(ju,a)
                e = str(d)[::-1]
                if str(d) == e:
                    sum += ju
    elif i == 6:
        for j in range(1, 10):
            for k in range(10):
                for l in range(10):
                    ju = j*100000+k*10000+l*1000+100*l+10*k+j
                    if ju > n:
                        break
                    d = base_n(ju,a)
                    e = str(d)[::-1]
                    if str(d) == e:
                        sum += ju
    elif i == 8:
        for j in range(1, 10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        ju = j*10000000+k*1000000+l*100000+m*10000+m*1000+100*l+10*k+j
                        if ju > n:
                            break
                        d = base_n(ju,a)
                        e = str(d)[::-1]
                        if str(d) == e:
                            sum += ju
    elif i == 10:
        for j in range(1, 10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        for o in range(10):
                            ju = j*1000000000+k*100000000+l*10000000+m*1000000+o*100000+o*10000+1000*m+100*l+10*k+j
                            if ju > n:
                                break
                            d = base_n(ju,a)
                            e = str(d)[::-1]
                            if str(d) == e:
                                sum += ju
    elif i == 12:
        for j in range(1, 10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        for o in range(10):
                            for p in range(10):
                                ju = j*100000000000+k*10000000000+l*1000000000+m*100000000+o*10000000+p*1000000+p*100000+o*10000+1000*m+100*l+10*k+j
                                if ju > n:
                                    break
                                d = base_n(ju,a)
                                e = str(d)[::-1]
                                if str(d) == e:
                                    sum += ju
print(sum)"""


def is_palindromic_in_base(x: int, base: int) -> bool:
    """x が base 進数で回文かどうかを判定"""
    digits = []
    while x > 0:
        digits.append(x % base)
        x //= base
    return digits == digits[::-1]

def solve(a: int, n: int) -> int:
    b = 10
    answers = []
    powb = [1]  # 10のべき乗

    length = 1
    while True:
        # powbを必要な長さまで拡張
        while len(powb) < length:
            powb.append(powb[-1] * b)

        if powb[length - 1] > n:
            break

        d = [0] * ((length + 1) // 2)  # 上半分の桁。d[0] が最上位
        d[0] = 1

        while True:
            # dから回文数を復元
            val = 0
            for i in range(length):
                idx = i if i < len(d) else length - 1 - i
                val += powb[i] * d[idx]

            if val <= n and is_palindromic_in_base(val, a):
                answers.append(val)

            # 次のdに進める
            has_next = False
            for i in reversed(range(len(d))):
                if d[i] == b - 1:
                    d[i] = 0
                else:
                    d[i] += 1
                    has_next = True
                    break
            if not has_next:
                break

        length += 1

    return sum(answers)

# 入力と実行
if __name__ == "__main__":
    a = int(input())
    n = int(input())
    print(solve(a, n))
