from tkinter import *

window = Tk()
stack = []

# calculator display
myInput = Entry(window, width = 40)
myInput.grid(row = 0, columnspan = 4)

# class for Number Keys
class Numbers:
    def __init__(self, n):
        self.num = Button(window, text = n, padx = 25, pady = 20, command = lambda: self.printNum(n))

    def printNum(self, n):
        myInput.insert(len(myInput.get()), n)

# generate Number Keys using Numbers Class
numButs = []
numButs.append(Numbers(0))
numButs[0].num.grid(row = 4, column = 0)

for i in range(1, 10):
    numButs.append(Numbers(i))
    #display numbers as on calculator keypad
    numButs[i].num.grid(row = 3 - int((i - 1) / 3), column = ((i - 1) % 3))

# class for Operator Keys
class Operations:
    def __init__(self, op):
        self.opr = Button(window, text = op, padx = 25, pady = 20, command = lambda: self.saveOp(op))

    def saveOp(self, op):
        stack.append(int(myInput.get()))
        stack.append(op)
        if len(stack) == 4:
            performOp()
        myInput.delete(0, END)

# generate Operator Keys using Operations Class
operators = ['+', '-', 'x', '/']

for i in range(0, 4):
    operators[i] = Operations(operators[i])
    operators[i].opr.grid(row = (i + 1), column = 3)

# perform operations
def performOp():
    a, b = stack.pop(0), stack.pop(1)
    match stack.pop(0):
        case '+': stack.insert(0, a + b)
        case '-': stack.insert(0, a - b)
        case 'x': stack.insert(0, a * b)
        case '/': stack.insert(0, a / b)
        case _: print("Error")

# equals to (=) key function
def answer_equals():
    stack.append(int(myInput.get()))
    myInput.delete(0, END)
    performOp()
    myInput.insert(0, stack[0])

# equals to (=) key definition
equalsTo = Button(window, text = "=", padx = 25, pady = 20, command = answer_equals)
equalsTo.grid(row = 4, column = 1)

window.resizable(False,False)
window.mainloop()