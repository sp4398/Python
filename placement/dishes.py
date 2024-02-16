#test case
t=int(input())
for tc in range(t):
    n=int(input())
    itemList=list(map(int,input().split()))
    i=0
    max=0
    itemType=itemList[0]
    while i<n:
        c=1
        j=i+1
        while j<n:
            if itemList[i]==itemList[j] and j!=i+1:
                c=+1
                if j<n-1 and itemList[j]==itemList[j+1]:
                    j+=1
            j+=1
        if max<c:
            max=c
            itemType=itemList[i]
        i+=1
    print(itemType)