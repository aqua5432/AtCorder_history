n, l, r = map(int, input().split())
s = input()
slist = list(s)
judge = True
for i in range(l-1, r):
    if slist[i] != "o":
        judge = False
if judge:
    print("Yes")
else:
    print("No")
