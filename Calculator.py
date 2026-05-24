import tkinter as tk

# --- Logic ---
def button_click(value):
    current = display_var.get()
    if value == "C":
        display_var.set("")
    elif value == "=":
        try:
            result = eval(current)
            display_var.set(result)
        except Exception:
            display_var.set("Error")
    elif value == "⌫":
        display_var.set(current[:-1])
    else:
        display_var.set(current + str(value))

# --- Window ---
root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

# --- Display ---
display_var = tk.StringVar()
display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Segoe UI", 28),
    bd=0,
    relief="flat",
    justify="right",
    bg="#2a2a3d",
    fg="#cdd6f4",
    insertbackground="#cdd6f4",
    readonlybackground="#2a2a3d",
)
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=16, pady=(16, 8), ipady=16)

# --- Button layout ---
buttons = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["00", "0", ".", "="],
]

# Color themes per button type
def get_colors(val):
    if val == "=":
        return "#cba6f7", "#1e1e2e"       # purple, dark text
    elif val in ("C", "⌫"):
        return "#f38ba8", "#1e1e2e"       # red
    elif val in ("/", "*", "-", "+", "%"):
        return "#fab387", "#1e1e2e"       # orange
    else:
        return "#313244", "#cdd6f4"       # dark, light text

for r, row in enumerate(buttons):
    for c, val in enumerate(row):
        bg, fg = get_colors(val)
        btn = tk.Button(
            root,
            text=val,
            font=("Segoe UI", 18, "bold"),
            width=4,
            height=2,
            bg=bg,
            fg=fg,
            activebackground=fg,
            activeforeground=bg,
            bd=0,
            relief="flat",
            cursor="hand2",
            command=lambda v=val: button_click(v),
        )
        btn.grid(row=r + 1, column=c, padx=6, pady=6)

# --- Grid weight ---
for i in range(4):
    root.columnconfigure(i, weight=1)

root.mainloop()
