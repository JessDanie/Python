#y=list(map(int, input().split(" ")))
y=input()
i = y.replace("-", "").replace("*", "").replace("#", "").replace("+", "")
if i.isalnum() or i=='':
    v={'a':2, 'b':2, 'c':2,'d':3, 'e':3, 'f':3, 'g':4, 'h':4, 'i':4,'g':5, 'k':5, 'l':5,'m':6, 'n':6, 'o':6,'p':7, 'q':7, 'r':7,'s':7, 't':8, 'u':8,'v':8, 'w':9, 'x':9,'y':9, 'z':9}
    y=y.lower()
    for g in y:
        if g.isalpha():
            y=y.replace(g, str(v[g]))

    print(y)
else:
    print(y+" invalid")

