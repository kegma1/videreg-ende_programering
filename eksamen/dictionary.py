def main():
    file_path = input("Enter a filename: ")
    dictionary = {}
    with open(file_path, "r") as f:
        contents = f.read().strip().split()
        for word in contents:
            initial = word[0]
            if initial not in dictionary:
                dictionary[initial] = set()
            dictionary[initial].add(word)

    for initial, words in sorted(dictionary.items()):
        print(initial)
        for word in words:
            print(f"    {word}")  
main()