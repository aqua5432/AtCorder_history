N = int(input())
S = input()
slist = list(S)
answer = ""
if N < 3:
    print("No")
else:
    for i in range(N-3,N):
        answer += slist[i]
    if answer == "tea":
        print("Yes")
    else:
        print("No")