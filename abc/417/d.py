N = int(input())
present = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
tenshon_list_index = []
tenshon_list_num = []
for _ in range(Q):
    X = int(input())
    tenshon = X
    if X in tenshon_list_index:
        print(tenshon_list_num[tenshon_list_index.index(X)])
        continue
    for i in range(N):
        if tenshon <= present[i][0]:
            tenshon += present[i][1]
        else:
            tenshon = max(tenshon-present[i][2], 0)
    print(tenshon)
    tenshon_list_num.append(tenshon)
    tenshon_list_index.append(X)