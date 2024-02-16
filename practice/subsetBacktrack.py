def solve(ip,op,idx):
    if idx==len(ip):
        print(''.join(op))
        return
    solve(ip,op,idx+1)
    op.append(ip[idx])
    solve(ip,op,idx+1)
    op.pop()
ip=input()
op=[]
solve(ip,op,0)