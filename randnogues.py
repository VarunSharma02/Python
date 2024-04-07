import random
target_number = random.randint(1, 100)
while True:
 user_guess = int(input("Guess the number (1-100): "))
 if user_guess < target_number:
  print(f"Too low. Try again. Your no.{user_guess} & Random no.{target_number}")
 elif user_guess > target_number:
  print(f"Too high. Try again. Your no.{user_guess} & Random no.{target_number}")
 else:
  print("Congratulations! You guessed the number.")
 break   

        
