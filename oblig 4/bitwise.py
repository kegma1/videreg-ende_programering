import tkinter as tk


class App:
    def __init__(self):
        window = tk.Tk()       
        window.title("bitwise operasjoner")
        window.resizable(False,False)

        ## First number
        tk.Label(window, text="First number, range 0 - 255").grid(row=0, column=0)
        self.first_num = tk.IntVar(window, 0)
        self.first_num_box = tk.Entry(window, textvariable=self.first_num)
        self.first_num_display = tk.Label(window, text="00000000")
        self.first_num_box.bind("<FocusOut>", lambda x: update_display(self.first_num, self.first_num_display))

        self.first_num_box.grid(row=0, column=1)
        self.first_num_display.grid(row=0, column=2)

        ## Second number
        tk.Label(window, text="Second number, range 0 - 255").grid(row=1, column=0)
        self.second_num = tk.IntVar(window, 0)
        self.second_num_box = tk.Entry(window, textvariable=self.second_num)
        self.second_num_display = tk.Label(window, text="00000000")
        self.second_num_box.bind("<FocusOut>", lambda x: update_display(self.second_num, self.second_num_display))

        self.second_num_box.grid(row=1, column=1)
        self.second_num_display.grid(row=1, column=2)

        ## Your answer
        tk.Label(window, text="Your answer").grid(row=2, columnspan=1)
        self.user_answer = tk.StringVar(window, "00000000")
        self.answer_box = tk.Entry(window, textvariable=self.user_answer, justify="center")
        self.answer_box.grid(row=2, column=2)

        ## Correct answer
        tk.Label(window, text="Correct answer").grid(row=3, columnspan=1)
        self.correct_display = tk.Label(window, text="xxxxxxxx")
        self.correct_display.grid(row=3, column=2)

        ## Choose operation
        operators = ["AND", "OR", "OCOMP", "XOR", "SHIFTLEFT", "SHIFTRIGHT"]
        self.operator = tk.StringVar(window, "AND")
        self.operation_menue = tk.OptionMenu(window, self.operator, *operators)
        self.operation_menue.grid(row=2, column=4)

        ## Check button
        tk.Button(window, text="Check", command=self.ine).grid(row=2, column=6)

        window.columnconfigure(3, minsize=30)
        window.columnconfigure(5, minsize=30)
        window.columnconfigure(7, minsize=30)
        window.rowconfigure(5, minsize=10)

        window.mainloop()  

    def ine(self):
        num_1 = self.first_num.get()
        num_2 = self.second_num.get()
        try:
            user_answer = int(self.user_answer.get(), 2)
            if user_answer < 0 or user_answer > 255: 
                print("too big/small")
                return
        except:
            print("not an int")
            return
        
        operator = self.operator.get()
        correct_answer = ""
        if operator == "AND":
            correct_answer = decToBin(num_1 & num_2)
        elif operator == "OR":
            correct_answer = decToBin(num_1 | num_2)
        elif operator == "OCOMP":
            correct_answer = decToBin(~num_1 + 256)
        elif operator == "XOR":
            correct_answer = decToBin(num_1 ^ num_2)
        elif operator == "SHIFTLEFT":
            correct_answer = decToBin(num_1 << num_2)
        elif operator == "SHIFTRIGHT":
            correct_answer = decToBin(num_1 >> num_2)
        
        self.correct_display.config(text=correct_answer)

        if correct_answer == decToBin(user_answer):
            self.answer_box.config(background="green")
        else:
            self.answer_box.config(background="red")

def update_display(var, display):
    try:
        value = var.get()
        if 0 <= value <= 255:
            display.config(text=decToBin(value))
        else:
            display.config(text="xxxxxxxx")
    except:
        display.config(text="xxxxxxxx")
        

def decToBin(num: int, padding=8) -> str: # inspiration fra https://www.cuemath.com/numbers/decimal-to-binary/
    if num == 0:
        return "" + "0" * padding # add padding to make number 8 bit
    else:
        return decToBin(num // 2, padding - 1) + str(num % 2)

App()
