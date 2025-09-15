X, Y = map(int, input().split())

ans = X + Y
if ans > 12:
    ans -= 12
print(ans)

