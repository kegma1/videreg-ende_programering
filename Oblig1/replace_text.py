import os


def main():
    filename = input("Enter a filename: ")
    old_str = input("Enter the old string to be replaced: ")
    new_str = input("Enter the new string to replace the old string: ")

    if not os.path.isfile(filename):
        print(f"'{filename}' is not a valid path")
        return

    with open(filename, "r") as f:
        data = f.read()
        data = data.replace(old_str, new_str)
    with open(filename, "w") as f:
        f.write(data)
    print("Done")        

                    

main()