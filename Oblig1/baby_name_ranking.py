import urllib.request

def main():
    year = input("Enter the year: ")
    if int(year) < 2001 or int(year) > 2010:
        print("Only 2001-2010 is supported")
        return
    gender = input("Enter the gender: ").upper()
    if not (gender == "F" or gender == "M"):
        print("Your gender in invalid, only 'F' or 'M'")
        return
    name = input("Enter the name: ")
    
    data_for_year = urllib.request.urlopen(f"https://liveexample.pearsoncmg.com/data/babynameranking{year}.txt").readlines()

    rank = find_rank(data_for_year, name, gender)

    if rank != None:
        gender_str = "Girl" if gender == "F" else "Boy"
        print(f"{gender_str} name {name} is ranked #{rank.strip()} in year {year}")
    else:
        print("not found")
            
def find_rank(data, name, gender):
    for row in data:
        cols = row.decode().split("\t")

        if gender == "M" and cols[1].strip() == name:
            return cols[0]
        elif gender == "F" and cols[3].strip() == name:
            return cols[0]

    return None

main()