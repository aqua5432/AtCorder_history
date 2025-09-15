n = int(input())
user = set()

#文字列の入力は最初にすべて受け付けてから実行する必要なし(読み取った順に処理してOK)
for i in range(1, n+1):
    s = input()
    if s in user:
        continue
    set.add(s)
    print(i)
