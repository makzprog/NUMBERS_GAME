import random
from typing import List, Optional, Tuple

class NumberGenerator:
    """
    Responsible ONLY for configuration and generation of the secret number.
    It does not handle user input or game rules.
    """
    def __init__(self, min_range: int = 1, max_range: int = 100):
        self._min_range = min_range
        self._max_range = max_range
        self._current_secret: Optional[int] = None

    @property
    def min_range(self) -> int:
        return self._min_range

    @property
    def max_range(self) -> int:
        return self._max_range

    def set_range(self, min_val: int, max_val: int) -> None:
        if min_val < 1 or max_val <= min_val:
            raise ValueError("Invalid range. Min must be >= 1 and Min < Max.")
        self._min_range = min_val
        self._max_range = max_val

    def generate(self) -> int:
        """Generates and stores a new secret number."""
        self._current_secret = random.randint(self._min_range, self._max_range)
        return self._current_secret

    def check_guess(self, guess: int) -> str:
        """Compares a guess against the current secret."""
        if self._current_secret is None:
            raise ValueError("Secret number not generated yet.")
        
        if guess == self._current_secret:
            return "CORRECT"
        elif guess < self._current_secret:
            return "TOO_LOW"
        else:
            return "TOO_HIGH"


class ScoreBoard:
    """
    Responsible ONLY for tracking scores and statistics.
    """
    def __init__(self):
        self._scores: List[int] = []

    def add_score(self, attempts: int) -> None:
        self._scores.append(attempts)

    def get_best_score(self) -> Optional[int]:
        return min(self._scores) if self._scores else None


class ConsoleUI:
    """
    Responsible ONLY for Input/Output. 
    This isolates print/input statements, making it easier to switch to a GUI later.    """

    def get_integer_input(self, prompt: str = "", min_range: Optional[int] = None, max_range: Optional[int] = None) -> int:
        while True:
            try:
                if prompt:
                    value = int(input(prompt + " "))
                else:
                    value = int(input(f"Guess a number between {min_range} and {max_range}: "))
                return value
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def get_range_input(self) -> Tuple[int, int]:
        print("--- Configure Game Range ---")
        while True:
            try:
                min_val = int(input("Choose the minimum value (positive integer): "))
                max_val = int(input("Choose the maximum value (positive integer): "))
                if min_val < 1 or max_val <= min_val:
                    print("Invalid range. Minimum must be >= 1 and less than maximum.")
                    continue
                return min_val, max_val
            except ValueError:
                print("Invalid input. Please enter integers only.")

    def ask_replay(self) -> bool:
        choice = input("Play again? (y/n): ").lower()
        return choice == 'y'


class GameEngine:
    """
    The Controller: Coordinates the NumberGenerator, ScoreBoard, and UI.
    """
    def __init__(self, generator: NumberGenerator, ui: ConsoleUI):
        self.generator = generator
        self.ui = ui
        self.scoreboard = ScoreBoard()
        self.max_attempts = 10

    def _setup_round(self):
        """Allows user to configure range before the round starts."""
        valid_range = False
        while not valid_range:
            try:
                min_val, max_val = self.ui.get_range_input()
                self.generator.set_range(min_val, max_val)
                valid_range = True
            except ValueError as e:
                print(f"Error: {e}")

    def _play_round(self):
        self.generator.generate()
        attempts = 0
        min_r = self.generator.min_range
        max_r = self.generator.max_range
        
        while attempts < self.max_attempts:
            attempts += 1
            guess = self.ui.get_integer_input(f"Attempt {attempts}/{self.max_attempts} - Enter guess: ")

            # Input validation logic
            if guess < min_r or guess > max_r:
                print(f"Warning: Guess must be between {min_r} and {max_r}.")
                continue

            # Check Logic
            result = self.generator.check_guess(guess)
            
            if result == "CORRECT":
                print(f"🎉 Correct! You won in {attempts} attempts")
                self.scoreboard.add_score(attempts)
                best = self.scoreboard.get_best_score()
                if best is not None:
                    print(f"🏆 Best Score: {best} attempts")
                return
            elif result == "TOO_LOW":
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        print("❌ Out of attempts! Game Over.")

    def run(self):
        """Main Game Loop"""
        print("Welcome to the Number Guessing Game!")
        
        while True:
            self._setup_round()
            self._play_round()
            
            if not self.ui.ask_replay():
                print("Thanks for playing! Goodbye.")
                break
