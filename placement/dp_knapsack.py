n=int(input())
w=int(input())
wt=list(map(int,input().split()))

val=list(map(int,input().split()))

dp=[[-1 for i in range(w+1)] for j in range(n+1)]

def knapsack(wt,val,w,n,dp):
    if w==0 or n==0:
        dp[n][w]=0
        return dp[n][w]
    if dp[n][w]!=-1:
        return dp[n][w]
    if wt[n-1]>w:
        
        return knapsack(wt,val,w,n-1,dp)
        
    else:
        dp[n][w]=max(val[n-1]+knapsack(wt,val,w-wt[n-1],n-1,dp),knapsack(wt,val,w,n-1,dp))
        return dp[n][w]
    
print(knapsack(wt,val,w,n,dp))