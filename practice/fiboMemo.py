n=int(input())
def fibo(n):
    lookup=[-1 for i in range(n+1)]
    lookup[0] =0
    lookup[1]=1
    for i in range(2,n+1):
        lookup[i]=lookup[i-1]+lookup[i-2]
    return lookup[n]

print(fibo(n))

