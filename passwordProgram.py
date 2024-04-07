user=input("Enter any code containing number,alphabet,digit,special char,space")
alphabet,digit,space,specialchar=0,0,0,0
for i in user:
    if i.isalpha():
        alphabet+=1
    elif i.isspace():
        space+=1
    elif i.isdigit():
        digit+=1 
    else: 
        specialchar+=1
print(f"Space:{space}")
print(f"Alphabet:{alphabet}")
print(f"Digit:{digit}")
print(f"Special Character:{specialchar}")                   
 


      


      
      