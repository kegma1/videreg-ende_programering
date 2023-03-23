
def main():
    stack = []
    expr = input("Enter an expresion: ")
    for c in expr.split(" "):
        if c.isnumeric():
            stack.append(int(c))
        elif c == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif c == "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif c == "*":
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif c == "/":
            b = stack.pop()
            a = stack.pop()
            stack.append(a // b)
        else:
            pass
    
    print(stack)
main()