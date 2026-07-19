import tkinter as tk
from tkinter import messagebox
import random

# Color Palette (Plum & Blush theme)
BG = "#190019"          # Near-black Plum
CARD = "#2B124C"        # Deep Indigo
TEXT_MAIN = "#FBE4D8"   # Warm Ivory
TEXT_MUTED = "#DFB6B2"  # Soft Blush
ACCENT = "#522B5B"      # Muted Mauve
ACCENT_HOVER = "#854F6C" # Dusty Rose-Mauve (hover)

secret_number = random.randint(1, 100)
attempts = 0

def check_guess(event=None):
    global attempts
    try:
        guess = int(entry_guess.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a whole number.")
        return
    attempts += 1
    if guess < secret_number:
        feedback_label.config(text="▲  Too Low! Aim Higher.", fg=TEXT_MUTED)
    elif guess > secret_number:
        feedback_label.config(text="▼  Too High! Aim Lower.", fg=TEXT_MUTED)
    else:
        feedback_label.config(text=f"✔ Correct! Solved in {attempts} attempts", fg=TEXT_MAIN)
    attempts_label.config(text=f"Attempts: {attempts}")
    entry_guess.delete(0, tk.END)

def restart_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    feedback_label.config(text="Guess a number between 1–100", fg=TEXT_MUTED)
    attempts_label.config(text="Attempts: 0")
    entry_guess.delete(0, tk.END)

def on_enter(e): guess_btn.config(bg=ACCENT_HOVER)
def on_leave(e): guess_btn.config(bg=ACCENT)

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x500")
root.configure(bg=BG)
root.resizable(False, False)

tk.Label(root, text="G U E S S  T H E  N U M B E R", font=("Georgia", 14, "bold"),
         bg=BG, fg=TEXT_MAIN).pack(pady=(40, 5))
tk.Label(root, text="R A N G E :  1  -  1 0 0", font=("Segoe UI Semibold", 9),
         bg=BG, fg=TEXT_MUTED).pack()

card = tk.Frame(root, bg=CARD, padx=30, pady=30, highlightthickness=1, highlightbackground="#3D1F55")
card.pack(pady=25, padx=35, fill="both")

feedback_label = tk.Label(card, text="Guess a number between 1–100", font=("Segoe UI", 11),
                           bg=CARD, fg=TEXT_MUTED, wraplength=280)
feedback_label.pack(pady=(0, 20))

entry_guess = tk.Entry(card, font=("Segoe UI", 18), bg=BG, fg=TEXT_MAIN,
                        insertbackground=TEXT_MAIN, relief="flat", justify="center",
                        highlightthickness=1, highlightbackground=ACCENT)
entry_guess.pack(fill="x", ipady=6)
entry_guess.bind('<Return>', check_guess)   # Enter key triggers the check
entry_guess.focus()

guess_btn = tk.Button(card, text="SUBMIT", command=check_guess, bg=ACCENT, fg=TEXT_MAIN,
                       font=("Segoe UI", 11, "bold"), relief="flat", cursor="hand2",
                       activebackground=ACCENT_HOVER, activeforeground=TEXT_MAIN)
guess_btn.pack(fill="x", ipady=8, pady=(20, 5))
guess_btn.bind("<Enter>", on_enter)
guess_btn.bind("<Leave>", on_leave)

attempts_label = tk.Label(card, text="Attempts: 0", font=("Segoe UI", 10), bg=CARD, fg=TEXT_MUTED)
attempts_label.pack(pady=(15, 0))

restart_btn = tk.Button(root, text="Reset Engine", command=restart_game, bg=BG, fg=TEXT_MUTED,
                         font=("Segoe UI", 9, "underline"), relief="flat", cursor="hand2",
                         activebackground=BG, activeforeground=TEXT_MAIN, bd=0)
restart_btn.pack(pady=5)

root.mainloop()