def check(A, x, y):
    judge = True
    if A[x][y] == 'x' or A[x][y] == '#':
        judge = False
    if judge:
        bunki.append(A[x][y])
        counthozon.append(count)
        hozon.append([x, y])
        j_count += 1
    
H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
s_x = 0
s_y = 0
g_x = 0
g_y = 0
for i in range(H):
    for j in range(W):
        if A[i][j] == "S":
            s_x = i
            s_y = j
        elif A[i][j] == "G":
            g_x = i
            g_y = j
hozon = []
counthozon = []
bunki = []
count = 0
j_count = 0
while s_x != g_x and s_y != g_y:
    if s_x != 0:
        check(A, s_x-1,s_y)
    if s_x != W-1:
        check(A, s_x+1,s_y)
    if s_y != 0:
        check(A, s_x,s_y-1)
    if s_y != H-1:
        check(A, s_x,s_y+1)
    if len(hozon) == 0:
        print(-1)
        break
    elif len(hozon) == 1:
        count += 1
        s_x = hozon[0][0]
        s_y = hozon[0][1]
        if bunki[0] == "?":
            for i in range(H):
                for j in range(W):
                    if A[i][j] == "o":
                        A[i][j] == "x"
                    elif A[i][j] == "x":
                        A[i][j] == "o"
        bunki.clear()
        hozon.clear()
        counthozon.clear()
