#factorial----------------------------------------------------------------
#function-----------------------------------------
# def factorial_iter(n):
#     product=1
#     for i in range(n):
#         product=product*(i+1)
#     return product
# f=factorial_iter(3)

#recursive----------------------------------------
# n!=1*2*3*4.....(n-1)!*n
#   =fact(n-1)*n    ------formula

def fact_rec(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact_rec(n-1) #(formula used)

f=fact_rec(4)
print(f)




