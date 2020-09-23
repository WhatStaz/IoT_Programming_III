number = int(input("geef een getal: "))
count = number - 1
total = 0
if number >= 0:
    while count > 0 and count < number:
        total += count
        count -= 1
        print("Uitvoer: ", str(total))

