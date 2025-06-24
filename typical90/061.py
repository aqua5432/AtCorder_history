q = int(input())
tx = [list(map(int, input().split())) for _ in range(q)]
deck = []
for i in range(q):
    if tx[i][0] == 1:
        deck.insert(0, tx[i][1])
    elif tx[i][0] == 2:
        deck.append(tx[i][1])
    else:
        print(deck[tx[i][1]-1])