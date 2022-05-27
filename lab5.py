import numpy as np

# Zad1
a = np.arange(3)
b = np.arange(3, 6)
print(a)
print(b)
c = a*b
print(c)

# # Zad2
# c = np.arange(9).reshape(3, 3)
# d = np.arange(16).reshape(4, 4)
# print(c)
# print(d)
# print("Minimalne wartości dla każdego rzędu: Macierz 3x3", c.min(axis=1))
# print("Macierzy 4x4", d.min(axis=1))
# print("Minimalne wartości dla każdej kolumny: Macierz 3x3 ", c.min(axis=0))
# print("Macierzy 4x4", d.min(axis=0))

# # Zad3
# e = np.arange(3)
# f = np.arange(3, 6)
# print(e)
# print(f)
# print(e.dot(f))

# # Zad4
# g = np.array([10, 20, 30])
# h = np.array([1.5, 2.7, 22.22])
# print(g)
# print(h)
# print(g*h)

# # Zad5
# i = np.arange(6).reshape(2, 3)
# print(i)
# a = np.sin(i)
# print(a)
#
# # Zad6
# j = np.arange(6, 12).reshape(2, 3)
# print(j)
# b = np.cos(j)
# print(b)
#
# # Zad7
# c = a+b
# print(c)

# # Zad8
# k = np.arange(9).reshape(3, 3)
# print(k)
# for a in k:
#     print(a)
#     print("")

# # Zad9
# l = np.arange(9).reshape(3, 3)
# print(l)
# for b in l.flat:
#     print(b)
#     print("")

# # Zad10
# m = np.arange(81).reshape(9, 9)
# n = m.reshape(1, 81)
# o = m.reshape(81, 1)
# p = m.reshape(3, 27)
# r = m.reshape(27, 3)
# print(m)
# print(n)
# print(o)
# print(p)
# print(r)
# # iloczyn rzędów i kolumn musi dać liczbę elementów macierzy

# # Zad11
# n = np.arange(12).reshape(3, 4)
# print(n)
# o = np.arange(12).reshape(4, 3)
# print(o)
# p = np.arange(12).reshape(2, 6)
# print(p)
# print(n.flat[0:])
# print(o.flat[0:])
# print(p.flat[0:])
# n1 = n.ravel()
# o1 = o.ravel()
# p1 = p.ravel()
# print(n1, o1, p1)
# # tak

