number = int(input("Geef een getal: "))
count = number
print(number)
while count > 1:
    if number % (count-1) == 0:
        print(count-1)
    count -= 1