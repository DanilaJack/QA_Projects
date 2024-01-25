import tkinter as tk

current_expression = ""

def appended_symbol(symbol):
    global current_expression
    current_expression += str(symbol)
    result.delete(1.0, 'end')
    result.insert(1.0, current_expression)


def evaluate_calculation():
    global current_expression
    try:
        current_expression = str(eval(current_expression))
        result.delete(1.0, 'end')
        result.insert(1.0, current_expression)
    except:
        clear_field()
        result.insert(1.0, "Error")


def clear_field():
    global current_expression
    current_expression = ""
    result.delete(1.0, 'end')



window = tk.Tk()
window.geometry("300x275")
window.title("Calculator")
window.configure(bg="green")

result = tk.Text(window, height=2, width=16, font=("Arial", 24))
result.grid(columnspan=5)


btn_1 = tk.Button(window, text="1", command=lambda: appended_symbol(1), width=5, font=("Arial", 14), bg="pink")
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(window, text="2", command=lambda: appended_symbol(2), width=5, font=("Arial", 14), bg="blue")
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(window, text="3", command=lambda: appended_symbol(3), width=5, font=("Arial", 14), bg="red")
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(window, text="4", command=lambda: appended_symbol(4), width=5, font=("Arial", 14), bg="brown")
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(window, text="5", command=lambda: appended_symbol(5), width=5, font=("Arial", 14), bg="maroon2")
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(window, text="6", command=lambda: appended_symbol(6), width=5, font=("Arial", 14), bg="yellow")
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(window, text="7", command=lambda: appended_symbol(7), width=5, font=("Arial", 14), bg="orange")
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(window, text="8", command=lambda: appended_symbol(8), width=5, font=("Arial", 14), bg="white")
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(window, text="9", command=lambda: appended_symbol(9), width=5, font=("Arial", 14), bg="purple")
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(window, text="0", command=lambda: appended_symbol(0), width=5, font=("Arial", 14), bg="gray")
btn_0.grid(row=5, column=2)
btn_plus = tk.Button(window, text="+", command=lambda: appended_symbol("+"), width=5, font=("Arial", 14), bg="silver")
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(window, text="-", command=lambda: appended_symbol("-"), width=5, font=("Arial", 14), bg="coral")
btn_minus.grid(row=3, column=4)
btn_mul = tk.Button(window, text="*", command=lambda: appended_symbol("*"), width=5, font=("Arial", 14), bg="aqua")
btn_mul.grid(row=4, column=4)
btn_div = tk.Button(window, text="/", command=lambda: appended_symbol("/"), width=5, font=("Arial", 14), bg="lawngreen")
btn_div.grid(row=5, column=4)
btn_open_par = tk.Button(window, text="(", command=lambda: appended_symbol("("), width=5, font=("Arial", 14), bg="crimson")
btn_open_par.grid(row=5, column=1)
btn_close_par = tk.Button(window, text=")", command=lambda: appended_symbol(")"), width=5, font=("Arial", 14), bg="darkorchid1")
btn_close_par.grid(row=5, column=3)
btn_equals = tk.Button(window, text="=", command=evaluate_calculation, width=12, font=("Arial", 14), bg="lightblue1")
btn_equals.grid(row=6, column=3, columnspan=2)
btn_clear = tk.Button(window, text="C", command=clear_field, width=12, font=("Arial", 14), bg="darkseagreen")
btn_clear.grid(row=6, column=1, columnspan=2)

window.mainloop()



