s = input()
s_word = list(s)
count = 0
baglist = []
for i in range(len(s_word)):
    if s_word[i] == "#":
        count += 1
        baglist.append(i+1)
    if count == 2:
        print(*baglist, sep=',')
        count = 0
        baglist.clear()