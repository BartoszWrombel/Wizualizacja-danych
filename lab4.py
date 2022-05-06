import numpy as np
# Zad1
a = np.arange(0,45, 3)
print(a)

# Zad2
b = np.array([1.5, 2.6, 4.1, 6.7, 21.7, 32.3, 37.8])
print(b)
c = b.astype('int64')
print(c)

# Zad3
def funkcja(n):
    d = np.arange(1, (n * n) + 1)
    mat = d.reshape(n, n)
    return print(mat)


n = int(input("Podaj n: "))
funkcja(n)

# Zad4
def generuj(podstawa, liczba):
    e=np.logspace(1, liczba, num=liczba, base=podstawa, dtype="int64")
    return print(e)


generuj(2,4)

# Zad5
def funkcja5(dlugosc):
    a=np.arange(1, dlugosc)
    b=np.diag(a[::-1])
    return print(b)


funkcja5(10)

# Zad6
# kolumna:waga, wiersz:arbuz, ukos:bór
wiersz1="JDGZW"
wiersz2="RBTIA"
wiersz3="EYÓOG"
wiersz4="ARBUZ"
wiersz5="PHKLT"
npwiersz1=np.array(list(wiersz1))
npwiersz2=np.array(list(wiersz2))
npwiersz3=np.array(list(wiersz3))
npwiersz4=np.array(list(wiersz4)[::-1])
npwiersz5=np.array(list(wiersz5))
wykreslanka=np.array([npwiersz1, npwiersz2, npwiersz3, npwiersz4, npwiersz5])

print(wykreslanka)

