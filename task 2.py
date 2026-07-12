import tkinter as tk
from tkinter import messagebox
import random

BG = "#101820"
CARD = "#1c2731"
ACCENT = "#00e0a4"
ACCENT_HOVER = "#33ffc4"
DANGER = "#ff5c5c"
TEXT = "#f0f0f0"
SUBTEXT = "#8a97a3"

secret_number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    try:
        guess = int(entry_guess.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a whole number.")
        return

    attempts += 1
    if guess < secret_number:
        feedback_label.config(text="⬆  Too Low! Try higher", fg="#ffb84d")
    elif guess > secret_number:
        feedback_label.config(text="⬇  Too High! Try lower", fg="#ffb84d")
    else:
        feedback_label.config(text=f"🎉 Correct! {attempts} attempts", fg=ACCENT)

    attempts_label.config(text=f"Attempts: {attempts}")
    entry_guess.delete(0, tk.END)

def restart_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    feedback_label.config(text="Guess a number between 1–100", fg=SUBTEXT)
    attempts_label.config(text="Attempts: 0")
    entry_guess.delete(0, tk.END)

def on_enter(e): guess_btn.config(bg=ACCENT_HOVER)
def on_leave(e): guess_btn.config(bg=ACCENT)

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x420")
root.configure(bg=BG)
root.resizable(False, False)

tk.Label(root, text="🎯 Guess the Number", font=("Segoe UI", 20, "bold"),
         bg=BG, fg=TEXT).pack(pady=(35, 5))
tk.Label(root, text="Range: 1 - 100", font=("Segoe UI", 10), bg=BG, fg=SUBTEXT).pack()

card = tk.Frame(root, bg=CARD, padx=25, pady=25)
card.pack(pady=25, padx=35, fill="both")

feedback_label = tk.Label(card, text="Guess a number between 1–100", font=("Segoe UI", 12),
                           bg=CARD, fg=SUBTEXT, wraplength=280)
feedback_label.pack(pady=(0, 15))

entry_guess = tk.Entry(card, font=("Segoe UI", 16), bg="#26323d", fg=TEXT,
                        insertbackground=TEXT, relief="flat", justify="center")
entry_guess.pack(fill="x", ipady=8)

guess_btn = tk.Button(card, text="Guess", command=check_guess, bg=ACCENT, fg="#101820",
                       font=("Segoe UI", 12, "bold"), relief="flat", cursor="hand2",
                       activebackground=ACCENT_HOVER)
guess_btn.pack(fill="x", ipady=10, pady=(15, 5))
guess_btn.bind("<Enter>", on_enter)
guess_btn.bind("<Leave>", on_leave)

attempts_label = tk.Label(card, text="Attempts: 0", font=("Segoe UI", 10), bg=CARD, fg=SUBTEXT)
attempts_label.pack(pady=(10, 0))

restart_btn = tk.Button(root, text="↻ New Game", command=restart_game, bg=BG, fg=DANGER,
                         font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2",
                         activebackground=BG, activeforeground="#ff8080", bd=0)
restart_btn.pack(pady=5)

root.mainloop()