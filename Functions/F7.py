# Problem Statement:
# Create a function that accepts a dictionary and 
#a key-value pair, and adds the pair to the dictionary

def add_to_dict(d,key,value):
    d[key] = value
    return d
my_dict={'a':'1','b':'2'}
key='c'
value='3'
print(add_to_dict(my_dict,key ,value))
