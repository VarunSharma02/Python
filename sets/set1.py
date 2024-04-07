thisset={"a1", "a2", "a3",}
print(thisset) #sets are unordered
print(type(thisset))

s1={"s1","s2","s3","s3","s4","s5","s1","s4"}
print(s1) #sets print the unique values

mySet=set(("a1","a2","a3","a4"))
print(mySet) 
print(type(mySet))

myData={1,2,3,4,5,6,7,8,9,10}
for x in myData:
    print(x, end=" ") 

print()    

my1={"1","2","3","4","5","6","7","8","9"}
for x in my1:
    print(x, end=" ")
print()    

print("================================")    

myData.add(26)
print(myData)
print("================================")  

my2={1,2,3,4,5}
my3={6,7,8,9,10}
my2.update(my3)
print(my2)
print("================================")  
d1={26,37,78}
d2={45,54,65}
d1.update(d2)
print(d1)
print("================================")  

d1.remove(78)
print(d1)
print("================================")  
d1.discard(65)
print(d1)
print("================================")  

d1.pop() # it will randomly delete the item from the set
print(d1)
print("================================")  

d1.clear()
print(d1)
print("================================")  

myS={1,2,3,4,6,8}
del myS
print(myS)

