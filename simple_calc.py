import tkinter as tk

# Function to update expression in the entry field
def update_expression(value):
    entry_field.insert(tk.END, value)

# Function to calculate and display the result
def calculate():
    try:
        result = eval(entry_field.get())
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, str(result))
    except Exception:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "Error")

# Function to clear the input field
def clear():
    entry_field.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="black")

# Define input field
entry_field = tk.Entry(root, width=40, borderwidth=5, font=('Arial', 18))
entry_field.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Define layout and properties for buttons
button_params = {'padx': 20, 'pady': 20, 'font': ('Arial', 18), 'bg': 'gray'}

# Button configuration
buttons = {
    '7': (1, 0), '8': (1, 1), '9': (1, 2), '/': (1, 3),
    '4': (2, 0), '5': (2, 1), '6': (2, 2), '*': (2, 3),
    '1': (3, 0), '2': (3, 1), '3': (3, 2), '-': (3, 3),
    '0': (4, 0), 'C': (4, 1), '=': (4, 2), '+': (4, 3)
}

# Loop to create buttons with commands
for text, (row, col) in buttons.items():
    cmd = calculate if text == '=' else clear if text == 'C' else lambda t=text: update_expression(t)
    btn = tk.Button(root, text=text, command=cmd, **button_params)
    btn.grid(row=row, column=col, sticky="nsew")

# Configure grid to make buttons expand
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Start the main loop
root.mainloop()