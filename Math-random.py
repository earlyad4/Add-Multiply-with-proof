import tkinter as tk
from random import randint

def generate_numbers():
    """Generate two random two-digit numbers and display them."""
    num1 = randint(10, 99)
    num2 = randint(10, 99)
    num_label.config(text=f"Number 1: {num1}\nNumber 2: {num2}")
    result_label.config(text="Result: ")
    multiplication_box.delete(1.0, tk.END)

def add_numbers():
    """Add the displayed numbers and show the result."""
    text = num_label.cget("text")
    num1 = int(text.split("\n")[0].split(": ")[1])
    num2 = int(text.split("\n")[1].split(": ")[1])
    result = num1 + num2
    result_label.config(text=f"Result: {result}")
    multiplication_box.delete(1.0, tk.END)

def multiply_numbers():
    """Multiply the displayed numbers with a step-by-step breakdown."""
    text = num_label.cget("text")
    num1 = int(text.split("\n")[0].split(": ")[1])
    num2 = int(text.split("\n")[1].split(": ")[1])
    result = num1 * num2

    # Break into tens and units
    num1_units, num1_tens = num1 % 10, num1 // 10
    num2_units, num2_tens = num2 % 10, num2 // 10

    # Partial products
    step1 = num1_units * num2_units
    step2 = (num1_tens * num2_units) + (num1_units * num2_tens)
    step3 = num1_tens * num2_tens
    step4 = step1 + (step2 * 10) + (step3 * 100)

    # Display final result
    result_label.config(text=f"Result: {result}")

    # Show proof of work
    multiplication_box.delete(1.0, tk.END)
    proof_of_work = f"Step 1: Units × Units → {num1_units} * {num2_units} = {step1}\n"
    proof_of_work += f"Step 2: Cross multiply tens/units → ({num1_tens}*{num2_units}) + ({num1_units}*{num2_tens}) = {step2}\n"
    proof_of_work += f"Step 3: Tens × Tens → {num1_tens} * {num2_tens} = {step3}\n"
    proof_of_work += f"Step 4: Combine partial results = {step1} + ({step2}*10) + ({step3}*100) = {step4}\n\n"
    proof_of_work += f"Final Result: {result}"
    multiplication_box.insert(tk.END, proof_of_work)

# --- GUI Setup ---
root = tk.Tk()
root.title("Random Number Adder & Multiplier")

generate_button = tk.Button(root, text="Generate Numbers", command=generate_numbers)
generate_button.pack(pady=10)

num_label = tk.Label(root, text="Number 1: \nNumber 2: ")
num_label.pack(pady=10)

add_button = tk.Button(root, text="Add Numbers", command=add_numbers)
add_button.pack(pady=10)

multiply_button = tk.Button(root, text="Multiply Numbers", command=multiply_numbers)
multiply_button.pack(pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

multiplication_box = tk.Text(root, height=10, width=50)
multiplication_box.pack(pady=10)

root.mainloop()
