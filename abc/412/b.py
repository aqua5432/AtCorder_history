s = input()
t = input()
ls = list(s)
lt = list(t)
bool = True
for i in range(2, len(ls)):
    if ls[i].isupper():
        if ls[i-1] not in lt:
            bool = False
if bool:
    print("Yes")
else:
    print("No")