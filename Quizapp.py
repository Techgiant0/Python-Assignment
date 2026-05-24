import tkinter as tk
from tkinter import messagebox
import time

# -----------------------------
# QUIZ QUESTIONS
# -----------------------------
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["6", "7", "8", "9"],
        "answer": "8"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "Who created Python?",
        "options": [
            "Guido van Rossum",
            "Elon Musk",
            "Mark Zuckerberg",
            "Bill Gates"
        ],
        "answer": "Guido van Rossum"
    }
]

# -----------------------------
# MAIN WINDOW
# -----------------------------
root = tk.Tk()
root.title("Quiz App")
root.geometry("700x500")
root.config(bg="#f0f0f0")

# -----------------------------
# VARIABLES
# -----------------------------
current_question = 0
score = 0
selected_option = tk.StringVar()

start_time = time.time()

# -----------------------------
# TITLE
# -----------------------------
title_label = tk.Label(
    root,
    text="Quiz App",
    font=("Arial", 28, "bold"),
    bg="#f0f0f0",
    fg="#1e293b"
)
title_label.pack(pady=20)

# -----------------------------
# QUESTION FRAME
# -----------------------------
question_frame = tk.Frame(
    root,
    bg="white",
    bd=2,
    relief="solid",
    padx=20,
    pady=20
)
question_frame.pack(padx=20, pady=10, fill="both", expand=True)

# QUESTION LABEL
question_label = tk.Label(
    question_frame,
    text="",
    font=("Arial", 18),
    wraplength=600,
    justify="left",
    bg="white"
)
question_label.pack(pady=20)

# -----------------------------
# OPTION BUTTONS
# -----------------------------
option_buttons = []

for i in range(4):
    btn = tk.Radiobutton(
        question_frame,
        text="",
        variable=selected_option,
        value="",
        font=("Arial", 14),
        bg="white",
        anchor="w",
        padx=10
    )
    btn.pack(fill="x", pady=5)
    option_buttons.append(btn)

# -----------------------------
# SCORE LABEL
# -----------------------------
score_label = tk.Label(
    root,
    text="Score: 0",
    font=("Arial", 14),
    bg="#f0f0f0"
)
score_label.pack(pady=5)

# -----------------------------
# TIMER LABEL
# -----------------------------
timer_label = tk.Label(
    root,
    text="Time: 0s",
    font=("Arial", 14),
    bg="#f0f0f0"
)
timer_label.pack()

# -----------------------------
# FUNCTIONS
# -----------------------------
def load_question():
    """Load current question and options"""

    selected_option.set("")

    question_data = questions[current_question]

    question_label.config(
        text=f"Q{current_question + 1}. "
             f"{question_data['question']}"
    )

    for i, option in enumerate(question_data["options"]):
        option_buttons[i].config(
            text=option,
            value=option
        )

def next_question():
    """Check answer and move to next question"""

    global current_question
    global score

    selected = selected_option.get()

    if selected == "":
        messagebox.showwarning(
            "Warning",
            "Please select an answer."
        )
        return

    correct_answer = questions[current_question]["answer"]

    # CHECK ANSWER
    if selected == correct_answer:
        score += 1

    score_label.config(text=f"Score: {score}")

    current_question += 1

    # LOAD NEXT QUESTION
    if current_question < len(questions):
        load_question()
    else:
        show_result()

def show_result():
    """Display final result"""

    end_time = time.time()
    total_time = round(end_time - start_time)

    percentage = (score / len(questions)) * 100

    # PERFORMANCE MESSAGE
    if percentage >= 80:
        performance = "Excellent!"
    elif percentage >= 50:
        performance = "Good Job!"
    else:
        performance = "Needs Improvement"

    messagebox.showinfo(
        "Quiz Finished",
        f"Final Score: {score}/{len(questions)}\n\n"
        f"Percentage: {percentage:.0f}%\n\n"
        f"Time Taken: {total_time} seconds\n\n"
        f"Performance: {performance}"
    )

    root.destroy()

def update_timer():
    """Update timer every second"""

    elapsed_time = round(time.time() - start_time)

    timer_label.config(
        text=f"Time: {elapsed_time}s"
    )

    root.after(1000, update_timer)

# -----------------------------
# NEXT BUTTON
# -----------------------------
next_button = tk.Button(
    root,
    text="Next Question",
    font=("Arial", 14, "bold"),
    bg="#2563eb",
    fg="white",
    padx=20,
    pady=10,
    command=next_question
)
next_button.pack(pady=20)

# -----------------------------
# START APP
# -----------------------------
load_question()
update_timer()

root.mainloop()