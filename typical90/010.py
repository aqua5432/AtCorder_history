N = int(input())#10^5
cp = [list(map(int, input().split())) for i in range(N)]
Q = int(input())#10^5
lr = [list(map(int, input().split())) for i in range(Q)]

Points = [[0] * 2 for i in range(Q)] 
#for i in range(Q):
    #for j in range(lr[i][0]-1, lr[i][1]):
        #if(cp[j][0] == 1):
            #Points[i][0] += cp[j][1]
        #else:
            #Points[i][1] += cp[j][1]

#得た知識: 累積和(事前にある生徒の数までの和を計算しておく)
fir_score = [0] * (N + 1)
sec_score = [0] * (N + 1)
for i in range(N):
    if cp[i][0] == 1:
        fir_score[i + 1] = fir_score[i] + cp[i][1]#1組の生徒ならi+1番目の成績の合計はi番目までの合計とi+1番目の生徒の点数の合計
        sec_score[i + 1] = sec_score[i]
    else:
        fir_score[i + 1] = fir_score[i]#2組の生徒ならi+1番目の成績の合計はi番目までの合計
        sec_score[i + 1] = sec_score[i] + cp[i][1]
for i in range(Q):
    l = lr[i][0]
    r = lr[i][1]
    Points[i][0] = fir_score[r] - fir_score[l - 1]#r番目までの和-(l-1)番目{例: 3番目～5番目なら3, 4,5の三人分}
    Points[i][1] = sec_score[r] - sec_score[l - 1]
for i in range(Q):
    print(*Points[i])