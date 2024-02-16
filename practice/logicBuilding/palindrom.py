#x=1213
#str_x=str(x)
#tr_x=str_x[::-1]
#if str_x==str(x):
 #   print(x,"is palindrome")
#else:
#    print(x,"is not a palindrome")



num=1213
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if temp==rev:
    print("yes")
else:
    print("no")