
def main():
    num = int(input("enter a nummber: "))
    nanpa = ""
    while num > 0:
        if num >= 100:
            nanpa += "ale "
            num -= 100
        elif num >= 20:
            nanpa += "mute "
            num -= 20
        elif num >= 5:
            nanpa += "luka "
            num -= 5
        elif num >= 2:
            nanpa += "tu "
            num -= 2
        elif num >= 1:
            nanpa += "wan "
            num -= 1
    print(nanpa)

main()