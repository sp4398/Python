# #without using function
# marks=[67,75,81,68]
# percentage1=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
# print(percentage1)


# # using function
# marks=[67,75,81,68]
# percentage2=(sum(marks)/400)*100
# print(percentage2)


def percent(marks):
    p=(sum(marks)/400)*100
    return p

marks1=[67,75,81,68]
percentage1=percent(marks1)

marks2=[88,79,56,91]
percentage2=percent(marks2)

print(percentage1,percentage2)
