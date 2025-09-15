S = input()
slist = list(S)
t_index = [i for i, x in enumerate(slist) if x == "t"]
tlist = []
answer = 0
if t_index == []:
    print(0)
elif len(t_index) < 2:
    print(0)
else:
    for j in t_index:
        for i in range(t_index[0], t_index[j-1]+1):
            tlist.append(slist[i])
        if len(tlist) >= 3:
            X = tlist.count("t")
            num = (X-2)/(len(tlist)-2)
            answer = max(answer, num)
    print(answer)
