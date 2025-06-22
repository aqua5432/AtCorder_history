h, w = map(int, input().split())
#LEDを奇数列の奇数行におけばどの4空間でもかぶらずに設置できる
#行もしくは列が1行の時、すべてのLEDが光っていても不適切な状態にはならない
if h == 1 or w == 1:
    print(h * w)
else:
    hmax = (h + 1) // 2
    wmax = (w + 1) // 2
    print(hmax * wmax)