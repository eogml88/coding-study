# # standard solution
# *A,=map(int,open(0).read().split())
# n=A[0];A=A[1:];B=[]
# def D(i,c):
#     t,p=B[i];m=0
#     for j in range(i+1,n):
#         if j>i+t-1:
#             d=D(j,c)
#             if d>m:m=d
#     return c+p+m
# for i in range(n):
#     t,p=A[2*i:2*i+2]
#     if t<=n-i:B+=[[t,p]]
#     else:B+=[[0,0]]
# n,c,d=len(B),0,0
# for i in range(n):
#     d=D(i,0)
#     if d>c:c=d
# print(c)

# the best solution
n,*a=map(int,open(r:=0).read().split());d=[0]*30
for s in range(n):t,p=a[2*s:2*s+2];d[s+t]=max(d[s+t],r+p);r=max(r,d[s+1])
print(r)