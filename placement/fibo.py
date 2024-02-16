n=100
def fibo(n):
    if n==0 or n==1:
        return n 
    else:

        return fibo(n-1)+fibo(n-2)

for i in range(n):
    print(i,"=",fibo(i))


#due to problem of over lapping it processing very slow...
# ...to overcome this problem we use
#  dynamic programming(DP)