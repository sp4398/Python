n=1000
lookup=[-1 for i in range(n+1)]

def fibo(n,lookup):
    if n==0 or n==1:
        lookup[n]=n
        return lookup[n]
    elif lookup[n]!=-1:
        return lookup[n]
    else:
        lookup[n]=fibo(n-1,lookup)+fibo(n-2,lookup)
        return lookup[n]

for i in range(n+1):
    print(i,"=",fibo(i,lookup))