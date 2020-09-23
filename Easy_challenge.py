number1 = int(input("Geef een getal: "))
number2 = int(input("Geef een ander getal: "))

count1 = 1
count2 = 1

while count1 < number1 and count2 < number2:
    if number1 % (count1) == 0 and number2 % (count2) == 0:
        if count1 == count2:
            print(count1, count2)
    count1 += 1
    count2 += 1
