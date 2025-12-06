import random

number_of_tries = 0
secret_number = random.randint(1, 10)
guess_limit = 3

while number_of_tries < guess_limit:
    guess = int(input("guess a number between 1 and 10: "))
    number_of_tries += 1  
    if guess == secret_number:
        print("You win")
        break
    else:          
        print(f"Wrong guess. Try again.")
        
