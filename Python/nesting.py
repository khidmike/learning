# Demo of nested looping

def main():

    arr1 = ["red", "brown", "white"]
    arr2 = ["hyena", "jackal", "parrot", "wolf", "quokka"]
    arr3 = ["run", "skip"]

    for i in arr1:
        for j in arr2:
            for k in arr3:
                print(i +" "+ j +" "+ k)

main()
