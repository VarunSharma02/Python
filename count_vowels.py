sentence=input("Enter a sentence")
vowels="aeiouAEIOU"
vowels_count=0
for char in sentence:
    if char in vowels:
        vowels_count+=1
print("Number of vowels",vowels_count)        