# Zad.1
a = 'ala ma kota'
b = 'fela ma psa'
c = 10
d = 5
e = 67.6
f = 99.9
g = 3 + 4j
h = 10 + 5j
print(a)
print(b)
print(c, d)
print(e, f)
print(g, h)
# Zad.2
a = int(input("podaj liczbę całkowitą a: "))
b = int(input("podaj liczbę całkowitą b: "))
dod = a+b
ode = a-b
mno = a*b
dzie = a/b

print(a,"+",b,"=",dod)
print(a,"-",b,"=",ode)
print(a,"*",b,"=",mno)
print(a,"/",b,"=",dzie)
# Zad.3
a = 5
print(a)
a += 1
print(a)
a -= 1
print(a)
a *= 2
print(a)
a /= 2
print(a)
a **= 2
print(a)
a %= 2
print(a)
# Zad.4
import math

print("e^10=",math.pow(math.e,10))
print(math.pow(math.log(5+math.sin(8) ** 2),1/6))
print(math.floor(3.55))
print(math.ceil(4.80))
# Zad.5
a = 'BARTOSZ'
b = 'WROMBEL'
print(a.capitalize(), b.capitalize())
# Zad.6
txt = "la la la la la la la na na na na na \n la la na na la la la la la na na na na na"
print(txt.count("la"))
# Zad.7
txt= "ala ma kota"
print(txt[1], txt[10])
# Zad.8
txt = "la la la la la la la na na na na na \n la la na na la la la la la na na na na na"
print(txt.split( ))
# Zad.9
a = "Adam"
b = 5.6
c = hex(16)
d = 16
print("{0:s}, {1:f}, {2:s}, {3:X}" .format(a, b, c, d))
