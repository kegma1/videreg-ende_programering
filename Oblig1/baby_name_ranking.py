import urllib.request

def main():
    year = input("Enter the year: ")
    
    gender = input("Enter the gender: ")
    name = input("Enter the name: ")
    
    data_for_year = urllib.request.urlopen(f"https://liveexample.pearsoncmg.com/data/babynameranking{year}.txt").readlines()

    rank = find_rank(data_for_year, name, gender).strip()

    if rank != None:
        gender_str = "Girl" if gender == "F" else "Boy"
        print(f"{gender_str} name {name} is ranked #{rank} in year {year}")
    else:
        print("not found")
            
def find_rank(data, name, gender):
    for row in data:
        cols = row.decode().split("\t")

        if gender == "M" and cols[1] == name:
            return cols[0]
        elif gender == "F" and cols[3] == name:
            return cols[0]

    return None

main()