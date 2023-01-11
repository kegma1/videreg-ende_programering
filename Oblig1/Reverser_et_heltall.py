
def main():
    user_input = int(input("Enter a positive integer: "))
    reverse_display(user_input)

def reverse_display(value):
    if value < 10:
        print(value)
    else:
        print(value % 10, end="")
        reverse_display(value // 10)


main()