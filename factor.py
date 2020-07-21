x=int(input())
z=[]
for i in range(1,x+1):
    if x%i==0:
        z.append(i)
l=len(z)*2-1
a=[0 for i in range(l)]
b=[a for i in range(l)]
m=l
count=0
vcount=l-1
for k in range(len(z)):
    for i in range(count,vcount+1):
        for j in range(count,vcount+1):
            if i==count or j==count or i==vcount or j==vcount:
                b[i][j]=1
                print("1",end='')
            else:
                b[i][j]=0
                print("*",end='')

    count+=1
    vcount-=1
    print(b)
    print(" ")
