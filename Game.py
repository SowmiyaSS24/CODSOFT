import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play(choice):
    global user_score, computer_score
    computer_choice = get_computer_choice()
    result = determine_winner(choice, computer_choice)
    
    if "win" in result:
        user_score += 1
    elif "lose" in result:
        computer_score += 1
    
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")
    result_label.config(text="")

def exit_game():
    root.destroy()

# Initialize scores
user_score = 0
computer_score = 0

# Create GUI
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 12), bg="#f0f0f0")
label.pack()

buttons_frame = tk.Frame(root, bg="#f0f0f0")
buttons_frame.pack()

rock_button = tk.Button(buttons_frame, text="Rock", command=lambda: play("rock"), width=10, bg="#ff9999")
rock_button.grid(row=0, column=0, padx=5, pady=5)

paper_button = tk.Button(buttons_frame, text="Paper", command=lambda: play("paper"), width=10, bg="#99ccff")
paper_button.grid(row=0, column=1, padx=5, pady=5)

scissors_button = tk.Button(buttons_frame, text="Scissors", command=lambda: play("scissors"), width=10, bg="#99ff99")
scissors_button.grid(row=0, column=2, padx=5, pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
result_label.pack()

score_label = tk.Label(root, text=f"Score - You: {user_score} | Computer: {computer_score}", font=("Arial", 12), bg="#f0f0f0")
score_label.pack()

reset_button = tk.Button(root, text="Reset", command=reset_game, width=10, bg="#ffcc66")
reset_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=exit_game, width=10, bg="#ff6666")
exit_button.pack(pady=5)

root.mainloop()
