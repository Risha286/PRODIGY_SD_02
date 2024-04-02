import tkinter as tk
from tkinter import messagebox
import requests

class GuessingGameGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Guessing Game")
        self.geometry("300x150")

        self.label = tk.Label(self, text="Welcome to the Guessing Game!")
        self.label.pack(pady=10)

        self.button = tk.Button(self, text="Start Game", command=self.start_game)
        self.button.pack(pady=5)

    def start_game(self):
        # Request to start the game from the backend
        response = requests.post('http://localhost:5000/start_game')
        data = response.json()
        secret_number = data['secret_number']

        # Open a new window for the game
        game_window = tk.Toplevel(self)
        game_window.title("Guessing Game")
        game_window.geometry("300x150")

        # Game logic
        def check_guess():
            guess = int(guess_entry.get())
            payload = {'guess': guess, 'secret_number': secret_number}
            response = requests.post('http://localhost:5000/check_guess', json=payload)
            result = response.json()['result']
            if result == 'low':
                messagebox.showinfo("Result", "Too low! Try again.")
            elif result == 'high':
                messagebox.showinfo("Result", "Too high! Try again.")
            else:
                messagebox.showinfo("Result", f"Congratulations! You guessed the number {secret_number} correctly!")

        guess_label = tk.Label(game_window, text="Enter your guess (1-100):")
        guess_label.pack(pady=5)
        guess_entry = tk.Entry(game_window)
        guess_entry.pack(pady=5)
        guess_button = tk.Button(game_window, text="Guess", command=check_guess)
        guess_button.pack(pady=5)

if __name__ == "__main__":
    app = GuessingGameGUI()
    app.mainloop()
