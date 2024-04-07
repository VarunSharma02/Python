s=[]   
sum=0
while True:
    n=int((input()))
    if n<=1000 and n>=-1000:
        sum+=n
        s.append(n)
    if sum<0:
        s.pop(-1)
        break
for i in s:
    print(i)