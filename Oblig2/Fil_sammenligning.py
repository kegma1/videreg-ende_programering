

def main():
    file_a = input("Enter path to first file: ")
    file_b = input("Enter path to seconde file: ")

    with open(file_a, 'r', encoding='utf-8') as f1:
        words1 = set(f1.read().split())
        
    with open(file_b, 'r', encoding='utf-8') as f2:
        words2 = set(f2.read().split())

    n_both = len(words1 & words2)
    both = words1 | words2
    common = words1 & words2
    unique1 = words1 - words2
    unique2 = words2 - words1
    either = (words1 | words2) - common

    print(f"Antall unike ord i begge filer: {n_both}\n")
    print(f"Alle unike ord i begge filer: {both}\n")
    print(f"Felles ord i begge filer: {common}\n")
    print(f"Unike ord i første fil: {unique1}\n")
    print(f"Unike ord i andre fil: {unique2}\n")
    print(f"Unike ord i enten første eller andre fil: {either}\n")

main()