n = int(input())
sentence = ""
count = 0
for i in range(n):
    c, lstr = input().split()
    l = int(lstr)
    count += l
    if count <= 100:
        for j in range(l):
            sentence += c
if count <= 100:
    print(sentence)
else:
    print("Too Long")