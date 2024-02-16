def paren(op,cl,res):
    if op==0 and cl==0:
        print(res)
        return
    if op!=0:
        paren(op-1,cl,res+"(")
    if cl>op:
        paren(op,cl-1,res+")")

n=int(input())
paren(n,n,"")