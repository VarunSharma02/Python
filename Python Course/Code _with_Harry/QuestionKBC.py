questions = [
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which is the most populated country?", "India", "French", "China",
    "USA", "None", 1
  ],
  [
    "Which is the most spoken language of the world?", "Python", "French", "Hindi",
    "English", "None", 4
  ],
  [
    "What is the capital of India?", "Lucknow", "Delhi", "New Delhi",
    "Moradabad", "None", 3
  ],
  [
    "What is the currency of Canada?", "Dollar", "Canadian Dollar", "Russian Dollar",
    "Euro", "None", 2
  ],
  [
    "Which language is user friendly and easily to interprete?", "Python", "French", "JavaScript",
    "Php", "None", 1
  ],
  [
    "Who is the Prime Minister of India?", "Rahul", "Priyanka", "Modi",
    "Yogi", "None", 3
  ],
  [
    "Which platfrom name has been changed to X?", "Insta", "Fb", "Snap",
    "Twitter", "None", 4
  ],
  [
    "How many fathers do you have?", "2", "3", "1",
    "0", "None", 1
  ],
  [
    "what is the name of the national bird of India?", "Peacock", "Sparrow", "Hen",
    "Parrot", "None", 1
  ],
  [
    "What is the currency of India?", "Python", "French", "Dinar",
    "Rupee", "None", 
  ],
  [
    "Who is known as the father of India?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"{question[0]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")


 