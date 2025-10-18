import random

#Define Class
class Numbersgame():
    def __init__(self, min_range=1, max_range=100):
        self.min_range = min_range
        self.max_range = max_range
    
    #Let the user choose the range        
    def choose_range(self):
        min_range = int(input("Please choose the minimum values for the number range before the game starts. "))
        max_range = int(input("Please choose the maximum values for the number range before the game starts. "))
        
        
        try:
            if min_range > 0 and max_range > 0:
                self.min_range = int(min_range)
                self.max_range = int(max_range)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
    def get_guess(self):  
        while True:
            try:
                guess = int(input(f"Guess a number between {self.min_range} and {self.max_range}: "))
                if self.min_range <= guess <= self.max_range:
                    return guess
                else:
                    print("Invalid input. Please enter a number within the specified range.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

            
    def check_guess(self, guess, secret_number):
        secret_number = random.randint(self.min_range, self.max_range)
        if guess == secret_number:
            return "Correct"
        elif guess <= secret_number:
            return "Too Low!"
        else:
            return "Too high"
    
    def startgame()
