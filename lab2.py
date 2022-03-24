# Zad1
sporty = ['Koszykówka', 'Snowboarding', 'Szachy', 'Piłka nożna', 'Piłka siatkowa', 'Piłka ręczna']
print(sporty)
sporty.reverse()
print(sporty)
sporty.extend(('Kajakarstwo', 'Boks', 'Szermierka', 'Tenis'))
print(sporty)
# Zad2
slownik = {"FAQ": "frequently asked questions", "DIY": "do it yourself", "IMO": "in my opinion", "BTW": "by the way",
           "BRB": "be right back", "ASAP": "as soon as possible"}
print(slownik)
# Zad3
slownik = {"Val":"Valorant", "LOL":"League of Legends", "Fort":"Fortnite", "GTA V":"Grand Theft Auto V",
"LA":"Lost Ark", "RL":"Rocket League", "CSGO":"Counter-Strike: Global Offensive", "Wiedźmin":"Wiedźmin 3: Dziki Gon"}
print(slownik)
print(len(slownik))
# Zad4
zdanie = input("podaj przykładowe zdanie: ")
print(zdanie.count("a"))
# Zad5
import sys as system
system.stdout.write("Podaj dowolną liczbę całkowitą a: ")
a = int(system.stdin.readline())
system.stdout.write("Podaj dowolną liczbę całkowitą b: ")
b = int(system.stdin.readline())
system.stdout.write("Podaj dowolną liczbę całkowitą c: ")
c = int(system.stdin.readline())
wynik = (a**b + c)
system.stdout.write(str(wynik))
# Zad6
a = input("podaj liczbę całkowitą a: ")
b = input("podaj liczbę całkowitą b: ")
c = input("podaj liczbę całkowitą c: ")

if a>b:
    if a>c:
        max=a
    else:
        max=c
else:
    if b>c:
        max=b
    else:
        max=c
print(max)
# Zad7
liczby = [2, 4, 6, 8, 10, 12.5, 15.5, 18.8, 19.3, 20.01]
wynik = []
print(liczby)

for x in liczby:
   wynik.append(x ** 2)

print("Liczby podniesione do kwadratu:")
print(wynik)
# Zad8
liczby = []

for x in range (0, 10):
    liczba = input("Podaj liczbę:")
    if int(liczba) % 2 == 0:
        liczby.append(liczba)

print(liczby)
# Zad9
import math
a = int(input("Podaj liczbę: "))

try:
    wynik = math.sqrt(a)
    print("Pierwiastek z "+ str(a) +" wynosi "+ str(wynik))
except ValueError:
    print("Podaj liczbę nieujemną!!!")
