import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Zadanie1
# x = np.arange(1, 21)
# plt.plot(x, 1/x, label='f(x) = 1/x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Wykres funkcji f(x) dla x [1, 20]')
# plt.axis([1, 20, 0, 1])
# plt.legend()
# plt.show()

# Zadanie2
# x = np.arange(1, 21)
# plt.plot(x, 1/x, 'g>:', label='f(x) = 1/x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Wykres funkcji f(x) dla x [1, 20]')
# plt.axis([0, 20, 0, 1])
# plt.legend()
# plt.show()

# Zadanie3
# x = np.arange(0, 31, 0.1)
# plt.plot(x, np.sin(x), 'b', label='sin(x)')
# plt.plot(x, np.cos(x), 'r', label='cos(x)')
# plt.xlabel('x')
# plt.ylabel('sinx(x) cos(x)')
# plt.title('Wykres funkcji sin(x), cos(x)')
# plt.legend(loc='upper right')
# plt.show()

# Zadanie4
# df2 = pd.read_csv('iris.data', header=0, sep=',', decimal='.')
# print(df2)
# c = np.random.randint(0, 50, len(df2.index))
# s = np.abs(df2['sepal length']- df2['sepal width'])
#
# plt.scatter(df2['sepal length'], df2['sepal width'], c=c, s=s)
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')
# plt.show()

# # Zadanie5
# xlsx = pd.ExcelFile('datasets/imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)
# # wykres1
# grupa = df.groupby('Plec')
# x = list(grupa.groups.keys())
# y = list(grupa.agg('Liczba').sum())
#
# plt.subplot(1, 3, 1)
# plt.bar(x=x, height=y, color=['red', 'green'] )
# plt.xlabel('Płeć')
# plt.ylabel('Liczba urodzonych dzieci')
#
# # wykres2
# x = df['Rok'].unique()
# y1 = df[(df['Plec'] == 'K')].groupby('Rok').agg({'Liczba': ['sum']}).values
# y2 = df[(df['Plec'] == 'M')].groupby('Rok').agg({'Liczba': ['sum']}).values
#
# plt.subplot(1, 3, 2)
# plt.plot(x, y1, label='Kobiety', color='red')
# plt.plot(x, y2, label='Mężczyźni', color='green')
# plt.xlabel('Rok')
#
# # # wykres3
# x = df['Rok'].unique()
# y = df.groupby('Rok').agg('Liczba').sum()
#
# plt.subplot(1, 3, 3)
# plt.bar(x, y)
# plt.xlabel('Rok')
#
# plt.subplots_adjust(wspace=0.6)
# plt.show()

# Zadanie6

df3 = pd.read_csv('datasets/zamowienia.csv', header=0, sep=';', decimal='.')
print(df3)
grupa = df3.groupby('Sprzedawca').agg('Utarg').sum()
print(grupa)
e = [0.0 for n in range(len(grupa.index))]
e[np.random.randint(0, len(grupa.index))] = 0.3
wedges, texts, autotext = plt.pie(x=grupa, labels=grupa.index, autopct=lambda pct: "{:.2f}%".format(pct),
                                  textprops=dict(color='black'), explode=e, shadow=True)
plt.title('Procentowy udział zarobków sprzedawców')
plt.show()


