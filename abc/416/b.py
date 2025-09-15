s = input()
slist = list(s)
answer = ""
judge = True
for i in range(len(slist)):
    if slist[i] == "#":
        answer += "#"
        judge = True
    else:
        if judge:
            answer += "o"
            judge = False
        else:
            answer += "."
print(answer)