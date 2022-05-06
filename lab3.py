# Zad1
a = [1-x for x in range(1, 11)]
b = [4**i for i in range(8)]
c = [x for x in b if x % 2 == 0]
print(a)
print(b)
print(c)
# Zad2
import random

random.seed()

lista1 = []

for i in range(10):
    lista1.append(random.randint(1, 100))
print(lista1)
lista2 = [i for i in lista1 if i % 2 == 0]
print(lista2)
# Zad3
produkty = {"butelka wody":"szt", "pomarańcze":"kg", "gruszki":"kg", "chleb":"szt", "butelka mleka":"szt"}
produktyszt = {x:y for x, y in produkty.items() if y == "szt"}
print(produkty)
print(produktyszt)
# Zad4
def tp(a, b, c):
    if (a**2)+(b**2)==(c**2):
        return "Trójkąt jest prostokątny"
    else:
        return "Trójkąt nie jest prostokątny"


a = int(input("Podaj pierwszą przyprostokątną: "))
b = int(input("Podaj drugą przyprostokątną: "))
c = int(input("Podaj przeciwprostokątną: "))
print(tp(a, b, c))
# Zad5
def PoleTrapezu(a=1, b=1, h=1):
    wynik = ((a+b)*h)/2
    return wynik


a = int(input("Podaj pierwszą podstawę trapezu: "))
b = int(input("Podaj drugą podstawę trapezu: "))
h = int(input("Podaj wysokość trapezu: "))

print("Pole trapezu wynosi ", PoleTrapezu(a, b, h))
print(PoleTrapezu(10, 20))
print(PoleTrapezu())
# Zad6
def ciag(a=1, b=4, ile=10):
    iloczyn = 1
    for x in range(ile):
        iloczyn *= (a * (b ** x))
    return iloczyn


print(ciag(1, 4, 5))
# Zad7
def ciag(*liczby):
    if len(liczby) != 0:
        a = liczby[0]
        b = liczby[1]
        ile = liczby[2]
    else:
        a = 1
        b = 4
        ile = 10

    iloczyn = 1
    for x in range(ile):
        iloczyn *= (a * (b ** x))
    return iloczyn


print(ciag(1, 4, 5))
print(ciag())
# Zad8
def zakupy(**produkty):
    print("Wszystkich produktów jest", len(produkty))
    print("Wartość tych produktów wynosi", sum(produkty.values()))


zakupy(czekolada=5, gruszka=10, mleko=20.5, chleb=3)
# Zad9
from ciagi import *

print("n-ty wyraz ciągu arytmetycznego dla a1=20, n=10, r=3 wynosi", arytmetyczne.n_ty_wyraz(20, 10, 3))
print("suma n pierwszych wyrazów ciągu arytmetycznego dla a1=1, an=10, n=20 wynosi", arytmetyczne.suma(1, 10, 20))
print("n-ty wyraz ciągu geometrycznego dla a1=5, q=3, n=4 wynosi", geometryczne.n_ty_wyraz(5, 3, 4))
print("suma n pierwszych wyrazów ciągu geometrycznego dla a1=1, q=2, n=3 wynosi", geometryczne.suma(1, 2, 3))
# Zad10
liczby = [x for x in range(101) if x % 4 == 0]
print(liczby)

with open("liczby.txt", "w") as plik:
    plik.writelines(str(liczby))

# Zad11
with open("liczby.txt", "r") as plik:
    for linia in plik:
        print(linia)

