#test case
t= int (input())
#loop for taste case
for tc in range(t):
    a,b,c,x,y=[ int(x) for x in input().split(',') ]

    if (a+b+c)!=(x+y):
        print("NO")

    elif y<min(a,min(b,c)) or x<min(a,min(b,c)):
        print("NO")

    else:
        print("YES")

