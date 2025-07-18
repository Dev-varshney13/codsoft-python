import tkinter as tk
import random
import sys

# ===== Logic Functions Shared Between CLI and GUI =====

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

# ===== Console Version =====

def get_user_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid input. Please try again.")

def play_console():
    user_score = 0
    computer_score = 0
    round_num = 1

    print("Welcome to Rock-Paper-Scissors (Console Version)!")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to play.\n")

    while True:
        print(f"\n--- Round {round_num} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("\nThanks for playing!")
            break
        round_num += 1

# ===== GUI Version =====

class RPSGame:
    def __init__(self, master):
        self.master = master
        master.title("Rock Paper Scissors")
        master.geometry("400x400")
        master.configure(bg="#b0b0b0")

        self.user_score = 0
        self.computer_score = 0

        # Labels
        self._create_labels()

        # Buttons
        self._create_buttons()

    def _create_labels(self):
        # Title
        self._create_shadowed_label("Choose Rock, Paper, or Scissors:", 40, ("Arial", 14, "bold"), "#222", "#888888")

        # Result
        self.result_label = self._create_shadowed_label("", 90, ("Arial", 12, "bold"), "#222", "#888888")

        # Score
        self.score_label = self._create_shadowed_label("Score - You: 0 | Computer: 0", 140, ("Arial", 12, "bold"), "#010100", "#888888")

    def _create_shadowed_label(self, text, y, font, fg, shadow_color):
        shadow = tk.Label(self.master, text=text, font=font, bg=shadow_color, fg=fg)
        shadow.place(relx=0.5, y=y+3, anchor="center")
        label = tk.Label(self.master, text=text, font=font, bg="#b0b0b0", fg=fg)
        label.place(relx=0.5, y=y, anchor="center")
        return label

    def _create_buttons(self):
        metallic_btns = {
            "Rock": {"bg": "#a7a7ad", "fg": "#fff", "shadow": "#888888"},
            "Paper": {"bg": "#d3d3d3", "fg": "#222", "shadow": "#888888"},
            "Scissors": {"bg": "#d4af37", "fg": "#fff", "shadow": "#b8860b"},
        }

        btn_y = 210
        btn_spacing = 120
        btn_names = ["Rock", "Paper", "Scissors"]
        btns_center = 200

        for idx, choice in enumerate(btn_names):
            offset = (idx - 1) * btn_spacing
            shadow = tk.Button(
                self.master, text=choice, width=12, font=("Arial", 12, "bold"),
                bg=metallic_btns[choice]["shadow"], fg=metallic_btns[choice]["fg"],
                bd=4, relief="ridge", state="disabled"
            )
            shadow.place(x=btns_center + offset + 3, y=btn_y + 3, anchor="center")

            btn = tk.Button(
                self.master, text=choice, width=12, font=("Arial", 12, "bold"),
                bg=metallic_btns[choice]["bg"], fg=metallic_btns[choice]["fg"],
                activebackground="#c0c0c0", activeforeground="#222",
                bd=4, relief="ridge",
                command=lambda c=choice.lower(): self.play_round(c)
            )
            btn.place(x=btns_center + offset, y=btn_y, anchor="center")

        # Quit button
        self._create_quit_button()

    def _create_quit_button(self):
        shadow = tk.Button(self.master, text="Quit", state="disabled",
                           bg="#8a8a8a", fg="#fff", font=("Arial", 12, "bold"),
                           bd=4, relief="ridge")
        shadow.place(relx=0.5, y=323, anchor="center")

        quit_btn = tk.Button(self.master, text="Quit", command=self.master.quit,
                             bg="#d4af37", fg="#fff", font=("Arial", 12, "bold"),
                             activebackground="#b8860b", activeforeground="#fff",
                             bd=4, relief="ridge")
        quit_btn.place(relx=0.5, y=320, anchor="center")

    def play_round(self, user_choice):
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        result_text = f"You chose: {user_choice.capitalize()} | Computer chose: {computer_choice.capitalize()}\n"
        if winner == "tie":
            result_text += "It's a tie!"
        elif winner == "user":
            self.user_score += 1
            result_text += "You win this round!"
        else:
            self.computer_score += 1
            result_text += "Computer wins this round!"

        self.result_label.config(text=result_text)
        self.score_label.config(text=f"Score - You: {self.user_score} | Computer: {self.computer_score}")

# ===== Mode Selector =====

def main():
    root = tk.Tk()
    app = RPSGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
