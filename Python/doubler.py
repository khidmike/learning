# Displays the explosive value that comes from doubling income each day

def main():
    start = float(input("Starting wage: "))

    for i in range(32):
        print(start)
        start = start * 2

main()
