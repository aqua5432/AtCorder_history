#回答閲覧
mod = 10**9 + 7

#欲しいa ** bを桁数を抑えて求める
def binpower(a, b):
    ans = 1
    while b != 0:
        if b % 2 == 1:
            ans = ans * a % mod
        a = a * a % mod
        b //= 2
    return ans

def main():
    N, K = map(int, input().split())

    if K == 1:
        print(1 if N == 1 else 0)
    elif N == 1:
        print(K % mod)
    elif N == 2:
        print(K * (K - 1) % mod)
    else:
        print(K * (K - 1) % mod * binpower(K - 2, N - 2) % mod)

if __name__ == "__main__":
    main()
