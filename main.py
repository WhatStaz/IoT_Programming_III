#opwarming
a = int(input("a:"))
b = int(input("b:"))

c = a + b
d = a / b
e = a % b
a += 1
b += 1
f = a + b

print(c, d, e, f)

#numbers
import math
#variabele straal
r = int(input("a:"))

#omtrek
omtrek = 2*math.pi*r

#oppervlakte
opp = math.pi*r*r

print("Omtrek: ", str(omtrek), "\n", "Oppervlakte: ", opp)

#Strings

a = "The ‘Python library’ contains several different kinds of components.It contains data types that would normally be considered part of the ‘core’ of a language, such as numbers and lists. For these types, the Python language core defines the form of literals and places some constraints on their semantics, but does not fully define the semantics. (On the other hand, the language core does define syntactic properties like the spelling and priorities of operators.)"
print(a.count("core"))

#Lists + Lists challenges
gehele_getallen = [1, 2, 3]

gehele_getallen[1] = 23

print(gehele_getallen)


def lookup( name ):
    number = gehele_getallen.index(name)
    print(number)
    return

gehele_getallen = ["John", "Willy", "Bernard", "Paul", "Jozefien"]

name = input("Wie zoek je: ")
lookup(name)






