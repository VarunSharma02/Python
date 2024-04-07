t7=("S1","S2","S3","S4","S5","S6","S7")
print(t7[2])
print(t7[3:])
print(t7[:6])
print(t7[-4:-1]) 

if "S3" in t7:
    print("found")

print(t7.count("S3"))  
print(t7.index("S3"))  
t8=("S1","S2","S3","S4","S5","S6","S7","S3","S2")
a1=list(t8)
a1.append("S11")
a2=tuple(a1)
print(a2)

student=("S1","S2","S3")
(Data1, Data2, Data3)=student
print(Data1)


