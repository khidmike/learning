# When supplied with a four-digit year, outputs that year's Gregorian epact

def main():

    year = int(input("Type in a year in format YYYY to calculate Gregorian epact: "))
    C = year // 100
    epact = (8 + (C//4) - C + ((8*C + 13) // 25) + 11*(year%19))%30

    print(epact)
    print()

main()
