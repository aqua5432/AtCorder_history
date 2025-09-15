N, A, B = map(int, input().split())
S = input()
Slist = list(S)
answer = ""
for i in range(A, N-B):
    answer += Slist[i]
print(answer)