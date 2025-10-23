# UI - THIS WAS GENERATED WITH AI 

import random
import tkinter as tk
from tkinter import messagebox

class NumbersGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Guess the Number Arcade 🎲")
        self.root.geometry("520x560")
        self.root.configure(bg="#0a0a0a")

        self.min_range = 1
        self.max_range = 100
        self.max_attempts = 10
        self.attempts = 0
        self.secret_number = None
        self.all_scores = []

        # Outer frame with neon border
        self.main_frame = tk.Frame(
            root, bg="#111111", highlightthickness=3, highlightbackground="#00ff99"
        )
        self.main_frame.pack(pady=25, padx=25, fill="both", expand=True)

        # Title
        self.title_label = tk.Label(
            self.main_frame,
            text="🎯 GUESS THE NUMBER 🎯",
            font=("Consolas", 26, "bold"),
            fg="#00ff99",
            bg="#111111"
        )
        self.title_label.pack(pady=25)

        # Range selection frame
        range_frame = tk.Frame(self.main_frame, bg="#111111")
        range_frame.pack(pady=10)

        tk.Label(
            range_frame, text="Min:", font=("Consolas", 16),
            bg="#111111", fg="#00e5ff"
        ).grid(row=0, column=0, padx=5)
        self.min_entry = tk.Entry(
            range_frame, font=("Consolas", 16), width=6, justify="center",
            bg="#000000", fg="#00ff99", insertbackground="#00ff99"
        )
        self.min_entry.insert(0, "1")
        self.min_entry.grid(row=0, column=1, padx=5)

        tk.Label(
            range_frame, text="Max:", font=("Consolas", 16),
            bg="#111111", fg="#00e5ff"
        ).grid(row=0, column=2, padx=5)
        self.max_entry = tk.Entry(
            range_frame, font=("Consolas", 16), width=6, justify="center",
            bg="#000000", fg="#00ff99", insertbackground="#00ff99"
        )
        self.max_entry.insert(0, "100")
        self.max_entry.grid(row=0, column=3, padx=5)

        # Start button
        self.start_button = tk.Button(
            self.main_frame, text="▶ START GAME", font=("Consolas", 18, "bold"),
            bg="#00ff99", fg="#000000", width=14, command=self.start_game,
            activebackground="#00e5ff", activeforeground="#000000"
        )
        self.start_button.pack(pady=20)

        # Info label
        self.info_label = tk.Label(
            self.main_frame, text="Press START to begin!",
            font=("Consolas", 18), fg="#ff4081", bg="#111111"
        )
        self.info_label.pack(pady=15)

        # Guess entry
        self.guess_entry = tk.Entry(
            self.main_frame, font=("Consolas", 28), width=5, justify="center",
            bg="#000000", fg="#00e5ff", insertbackground="#00ff99", state="disabled"
        )
        self.guess_entry.pack(pady=10)

        # Guess button
        self.guess_button = tk.Button(
            self.main_frame, text="PRESS GUESS ", font=("Consolas", 20, "bold"),
            bg="#00e5ff", fg="#000000", width=14, command=self.make_guess,
            state="disabled", activebackground="#00ff99", activeforeground="#000000"
        )
        self.guess_button.pack(pady=15)

        # Score label
        self.score_label = tk.Label(
            self.main_frame, text="🏆 Best score: N/A",
            font=("Consolas", 16), fg="#00ff99", bg="#111111"
        )
        self.score_label.pack(pady=5)

        # Play again button
        self.play_again_button = tk.Button(
            self.main_frame, text="↻ PLAY AGAIN", font=("Consolas", 18, "bold"),
            bg="#ff4081", fg="#ffffff", width=14, command=self.reset_game,
            state="disabled", activebackground="#ff80ab"
        )
        self.play_again_button.pack(pady=15)

        # Footer
        self.footer_label = tk.Label(
            self.main_frame, text="Use your intuition, Player One...",
            font=("Consolas", 12, "italic"), fg="#888", bg="#111111"
        )
        self.footer_label.pack(side="bottom", pady=10)

    def start_game(self):
        try:
            self.min_range = int(self.min_entry.get())
            self.max_range = int(self.max_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers.")
            return

        if self.min_range >= self.max_range or self.min_range < 0:
            messagebox.showerror("Error", "Minimum must be less than maximum and positive.")
            return

        self.attempts = 0
        self.secret_number = random.randint(self.min_range, self.max_range)
        self.info_label.config(
            text=f"Guess a number between {self.min_range} and {self.max_range}"
        )
        self.guess_entry.config(state="normal")
        self.guess_button.config(state="normal")
        self.start_button.config(state="disabled")
        self.play_again_button.config(state="disabled")
        self.guess_entry.delete(0, tk.END)

    def make_guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            messagebox.showwarning("Invalid", "Please type a number.")
            return

        if not (self.min_range <= guess <= self.max_range):
            messagebox.showinfo("Range Error", f"Stay between {self.min_range} and {self.max_range}.")
            return

        self.attempts += 1

        if guess == self.secret_number:
            messagebox.showinfo("🎉 WINNER!", f"You guessed it in {self.attempts} tries!")
            self.all_scores.append(self.attempts)
            self.update_best_score()
            self.end_round()
        elif guess < self.secret_number:
            self.info_label.config(text="📉 Too low! Try higher...")
        else:
            self.info_label.config(text="📈 Too high! Try lower...")

        if self.attempts >= self.max_attempts and guess != self.secret_number:
            messagebox.showinfo("💀 Game Over", f"No more tries! The number was {self.secret_number}.")
            self.end_round()

        self.guess_entry.delete(0, tk.END)

    def update_best_score(self):
        best = min(self.all_scores)
        self.score_label.config(text=f"🏆 Best score: {best} tries")

    def end_round(self):
        self.guess_entry.config(state="disabled")
        self.guess_button.config(state="disabled")
        self.play_again_button.config(state="normal")
        self.info_label.config(text="Round over. Play again?")

    def reset_game(self):
        self.start_button.config(state="normal")
        self.play_again_button.config(state="disabled")
        self.info_label.config(text="Press START to begin!")
        self.guess_entry.config(state="disabled")
        self.guess_button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumbersGameGUI(root)
    root.mainloop()
