# #1 maxiumum no. find
# def maximum(num1,num2,num3):
#     if (num1>num2):
#         if (num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if (num2>num3):
#             return num2
#         else:
#             return num3
# m=maximum(34,45,6)
# print(m)

# #2 farh to celcius
# def farh(cel):
#     return (cel *(9/5))+32
# c=30
# f=farh(c)
# print("fahrenheit temp is "+str(f))


# #3 print multiple line in one line
# print("Saurav",end=" ")
# print("Loves",end=" ")
# print("Haripriya",end=" ")


# #4 sum of first n natural number
# from typing import no_type_check


# def natural_no(n):
#     for i in range(n):
#         s=sum(n-1)+n
#     return s

# t=natural_no(5)
# print(t)

# #5 star
# n=3
# for i in range(n):
#     print("*"*(n-i))

# #6 inch to cms

# def inch(cms):
#     return cms*2.54
# i=1
# c=inch(i)
# print(c)

# #7 remove a given word & strip it at same time

# def remove(string,word):
#     newStr=string.replace(word,"")           
#     return newStr.strip()

# str="saurav is good"
# n=remove(str,"saurav")
# print(n)


# #8 print table
# print("\U0001F618")
# print("\U0001F618")
# print("\U0001F618")
# print("\U0001F618")
# print("\U0001F618")
# print("\U0001F618")
# print("\U0001F618")
# print("\U0001F618")


# x=5
# def add():
#     x=3
#     x=x+3
#     print(x)

# add()
# print(x)

def printinc(n):
    if n==1:
        return n

    print(n)
    printinc(n-1)
    print(n)

printinc(5)


