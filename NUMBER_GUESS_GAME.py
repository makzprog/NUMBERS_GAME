import random

class Numbersgame:
    def __init__(self, min_range=1, max_range=100, max_attempts=10):
        self.min_range = min_range
        self.max_range = max_range
        self.max_attempts = max_attempts

    #Function to choose range
    def choose_range(self):
        try:
            min_range = int(input("Choose the minimum value (positive integer): "))
            max_range = int(input("Choose the maximum value (positive integer): "))
        except ValueError:
            print("Invalid input. Please enter integers.")
            return

        if min_range > 0 and max_range > 0 and min_range < max_range:
            self.min_range = min_range
            self.max_range = max_range
        else:
            print("Invalid range. Minimum must be < maximum and both > 0.")
    
    #Function to get guess
    def get_guess(self):
        while True:
            try:
                guess = int(input(f"Guess a number between {self.min_range} and {self.max_range}: "))
            except ValueError:
                print("Not a number. Try again.")
                continue

            if self.min_range <= guess <= self.max_range:
                return guess
            print("Out of range. Try again.")

    #Function to check guess
    def check_guess(self, guess, secret_number):
        if guess == secret_number:
            return "Correct"
        elif guess < secret_number:
            return "Too Low!"
        else:
            return "Too High!"
        
    #function to start game
    def playgame(self):
        attempts = 0
        secret_number = random.randint(self.min_range, self.max_range)
        # print(f"(debug) secret is {secret_number}")  # uncomment if you want to test

        while attempts < self.max_attempts:
            attempts += 1
            guess = self.get_guess()     # <-- call via self
            result = self.check_guess(guess, secret_number)
            print(result)
            if result == "Correct":
                print(f"You win in {attempts} attempts!")
                self.display_score(attempts)
                return

        print(f"Out of attempts. The number was {secret_number}.")
        
    def display_score(self, attempts):
        all_scores = []
        
        for score in all_scores:
            a
            
        
        while history <= 10:
            print(history)

# Example:
game = Numbersgame()
game.choose_range()
game.playgame()
