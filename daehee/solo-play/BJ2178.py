# standard solution - time-out
*A,=open(0).read().split()
m,n=map(int,A[:2]);A=A[2:]
M=[[0]*n for _ in range(m)]
D=[[0,-1],[-1,0],[0,1],[1,0]]
def B(r,c):
    Q=[[r,c]]
    while Q:
        (r,c),Q=Q[0],Q[1:]
        k=m*n
        for d in D:
            u,v=r+d[0],c+d[1]
            if -1<u<m and -1<v<n:
                if A[u][v]=='1':
                    if M[u][v]:
                        if M[u][v]<k:k=M[u][v]
                    else:Q+=[[u,v]]
        M[r][c]=k+1 if r+c else 1
for r in range(m):
    for c in range(n):
        if A[r][c]=='1':B(r,c)
print(M[-1][-1])
# print(*M,sep='\n')