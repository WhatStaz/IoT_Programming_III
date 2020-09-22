import random

students = ["John","Karl","Olaf","Zacharia","Elke","Jean-luc","Jean-jean","Kevin","Sidney"]
students.sort()

groep1 = students[0:4]
groep2 = students[4:8]
groep3 = students[8:]

student_over = len(groep3)
aantal = len(students)//4

print("Groep 1: ", groep1, "\nGroep 2: ", groep2, "\nGroep 3: ", groep3, "\nAantal groepen: ", str(aantal), "\nStudenten over: ", str(student_over), "\nRandom student:", random.choice(students))


