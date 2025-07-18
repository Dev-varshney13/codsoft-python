from tkinter import Tk, Button, Entry, StringVar, messagebox, Frame

# Arithmetic Operation Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

def calculate(operation, num1, num2):
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        return divide(num1, num2)
    else:
        raise ValueError("Invalid operation")

# GUI Class
class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")
        master.resizable(False, False)
        master.configure(bg="#b0b0b0")  # Metallic silver background

        self.expression = ""
        self.input_text = StringVar()

        # Entry field
        self.input_frame = Frame(master, bg="#b0b0b0")
        self.input_frame.pack(pady=10)
        self.input_field = Entry(
            self.input_frame,
            textvariable=self.input_text,
            font=('Arial', 18, 'bold'),
            bd=5,
            relief='ridge',
            justify='right',
            width=20,
            bg="#e5e4e2",
            fg="#222"
        )
        self.input_field.grid(row=0, column=0)
        self.input_field.bind("<Key>", self.on_key_press)

        # Buttons
        self.btns_frame = Frame(master, bg="#b0b0b0")
        self.btns_frame.pack()

        button_colors = {
            '/': "#a7a7ad",
            '*': "#a7a7ad",
            '-': "#a7a7ad",
            '+': "#a7a7ad",
            '=': "#d4af37",
            'C': "#8a8a8a",
            '⌫': "#8a8a8a",
        }
        default_bg = "#d3d3d3"
        default_fg = "#222"

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('⌫', 5, 1)
        ]

        for (text, row, col) in buttons:
            btn = Button(
                self.btns_frame,
                text=text,
                width=5,
                height=2,
                font=('Arial', 14, 'bold'),
                bd=2,
                relief='ridge',
                bg=button_colors.get(text, default_bg),
                fg="#fff" if text in button_colors and text != '=' else default_fg,
                activebackground="#c0c0c0",
                activeforeground="#222",
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")

        for i in range(4):
            self.btns_frame.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.input_text.set("")
        elif char == '⌫':
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif char == '=':
            self.calculate()
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

    def on_key_press(self, event):
        key = event.char
        if key in '0123456789.+-*/':
            self.expression += key
            self.input_text.set(self.expression)
            return "break"
        elif key == '\r':
            self.calculate()
            return "break"
        elif key == '\x08':
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
            return "break"

    def calculate(self):
        try:
            # Manually parse and compute basic binary expressions
            for op in ['+', '-', '*', '/']:
                if op in self.expression:
                    parts = self.expression.split(op)
                    if len(parts) == 2:
                        num1, num2 = float(parts[0]), float(parts[1])
                        result = calculate(op, num1, num2)
                        self.input_text.set(str(result))
                        self.expression = str(result)
                        return
            # Fallback to eval for complex expressions
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Cannot divide by zero")
            self.input_text.set("")
            self.expression = ""
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            self.input_text.set("")
            self.expression = ""

# Main Program
if __name__ == "__main__":
    root = Tk()
    calculator = CalculatorGUI(root)
    root.mainloop()
