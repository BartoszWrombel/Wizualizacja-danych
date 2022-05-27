import numpy as np
# # Zad1
# a = np.arange(0,45, 3)
# print(a)
#
# # Zad2
# b = np.array([1.5, 2.6, 4.1, 6.7, 21.7, 32.3, 37.8])
# print(b)
# c = b.astype('int64')
# print(c)
#
# # Zad3
# def funkcja(n):
#     d = np.arange(1, (n * n) + 1).reshape(n, n)
#     return print(d)
#
#
# n = int(input("Podaj n: "))
# funkcja(n)
#
# # Zad4
# def generuj(podstawa, liczba):
#     e=np.logspace(1, liczba, num=liczba, base=podstawa, dtype="int64")
#     return print(e)
#
#
# generuj(2,4)
#
# # Zad5
# def funkcja5(dlugosc):
#     a = np.arange(1, dlugosc+1)
#     b = np.diag(a[::-1])
#     return print(b)
#
#
# funkcja5(10)
#
# # Zad6
# # kolumna:waga, wiersz:arbuz, ukos:bór
# wiersz1="JDGZW"
# wiersz2="RBTIA"
# wiersz3="EYÓOG"
# wiersz4="ARBUZ"
# wiersz5="PHKLT"
# npwiersz1=np.array(list(wiersz1))
# npwiersz2=np.array(list(wiersz2))
# npwiersz3=np.array(list(wiersz3))
# npwiersz4=np.array(list(wiersz4)[::-1])
# npwiersz5=np.array(list(wiersz5))
# wykreslanka=np.array([npwiersz1, npwiersz2, npwiersz3, npwiersz4, npwiersz5])
#
# print(wykreslanka)

# NWRTS
# # zad7
# # def macierz(n):
# #     mac = np.zeros((n, n), dtype='int32')
# #     mac += np.diag([2 for _ in range(n)])
# #     for i in range(1, n):
# #         mac += np.diag([2+(2*i) for _ in range(n-i)], k=i)
# #         mac += np.diag([2+(2*i) for _ in range(n-i)], k=-i)
# #     print(mac)
# #
# # macierz(3)
# #
# # zad8
# # def podziel(tab, kierunek='poziomo'):
# #     print(tab)
# #     if kierunek == 'poziomo':
# #         # nieparzysta liczba wierszy
# #         if tab.shape[0] % 2 != 0:
# #             print("Tablica posiada nieprzystą liczbę wierszy")
# #             return
# #         p1 = tab[0:int(tab.shape[0]/2), :]
# #         p2 = tab[int(tab.shape[0]/2):, :]
# #         print("***** część 1 *****")
# #         print(p1)
# #         print("***** część 2 *****")
# #         print(p2)
# #     elif kierunek == "pionowo":
# #         if tab.shape[1] % 2 != 0:
# #             print("Tablica posiada nieprzystą liczbę kolumn")
# #             return
# #         p1 = tab[:, 0:int(tab.shape[1]/2)]
# #         p2 = tab[:, int(tab.shape[1] / 2):]
# #         print("***** część 1 *****")
# #         print(p1)
# #         print("***** część 2 *****")
# #         print(p2)
# #
# #
# # podziel(np.arange(36).reshape((6,6)), kierunek='pionowo')
# #
# # zad9
# # def fib(n):
# #     if n == 0:
# #         return 0
# #     elif n == 1:
# #         return 1
# #     elif n > 1:
# #         return fib(n-1) + fib(n-2)
# #
# # macierz = np.ones(25, dtype='int32')
# # print(macierz)
# # for a in range(0, 25, 1):
# #     element = fib(a)
# #     macierz[a] = element
# # print(macierz)
# # macierz = macierz.reshape((5, 5))
# # print(macierz)
