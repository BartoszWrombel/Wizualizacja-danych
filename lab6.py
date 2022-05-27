import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pandas wprowadzenie
# Zadanie1
xlsx = pd.ExcelFile('datasets/imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)

# Zadanie2
# print(df[df['Liczba']>1000])
# print(df[df['Imie']=='BARTOSZ'])
# print(df['Liczba'].sum())
# print(df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]['Liczba'].sum())
#
# print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).first())
#
# print("Chłopcy")
# print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
#                                                                                    ascending=False).iloc[0])
# print("Dziewczynki")
# print(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
#                                                                                    ascending=False).iloc[0])

# Zadanie3
# df2 = pd.read_csv('datasets/zamowienia.csv', header=0, sep=';', decimal='.')
# print(df2)
# print(df2['Sprzedawca'].unique())
# print(df2.sort_values('Utarg', ascending=False).head(5))
# print(df2.groupby('Sprzedawca').agg({'Utarg':['count']}))
# print(df2.groupby('Kraj').agg({'Utarg': ['sum']}))
# print(df2.groupby('Kraj').agg({'Utarg': ['count']}))
# print(df2[(df2['Data zamowienia'] >= '2005-01-01') & (df2['Data zamowienia'] <= '2005-12-31') &
#             (df2['Kraj'] == 'Polska')].agg({'Utarg':['sum']}))
# print(df2[(df2['Data zamowienia'] >= '2004-01-01') & (df2['Data zamowienia'] <= '2004-12-31')].
# agg({'Utarg':['mean']}))

# r2004 = df2[(df2['Data zamowienia'] >= '2004-01-01') & (df2['Data zamowienia'] <= '2004-12-31')].\
#     agg({'Utarg': ['mean']})
# r2005 = df2[(df2['Data zamowienia'] >= '2005-01-01') & (df2['Data zamowienia'] <= '2005-12-31') &
#             (df2['Kraj'] == 'Polska')].agg({'Utarg': ['sum']})
# r2004.to_csv('zamowienia_2004.csv', index=False)
# r2005.to_csv('zamowienia_2005.csv', index=False)

# # Pandas wykresy
# xlsx = pd.ExcelFile('datasets/imiona.xlsx')
# df3 = pd.read_excel(xlsx, header=0)
# # print(df3)
# # Zadanie1
# grupa = df3.groupby('Rok').agg({'Liczba': ['sum']})
# rok = df3['Rok'].unique()
# w1 = grupa.plot()
# w1.set_xticks(rok)
# w1.set_xlabel('Rok')
# w1.set_ylabel('Liczba urodzonych dzieci')
# w1.tick_params(axis='x', labelrotation=30)
# w1.set_title('Liczba urodzonych dzieci w poszczególnych latach')
# w1.legend()
# plt.subplots_adjust(left=0.15, bottom=0.15)
# plt.show()
# # Zadanie2
# grupa2 = df3.groupby('Plec').agg({'Liczba': ['sum']})
# w2 = grupa2.plot.bar()
# w2.set_ylabel('Liczba urodzeń')
# w2.set_title('Liczba urodzonych chłopców i dziewczynek')
# w2.legend()
# w2.tick_params(axis='x', labelrotation=0)
# plt.show()
# # Zadanie3
# grupa3 = df3[df3['Rok'] > 2012].groupby('Plec').agg({'Liczba': ['sum']})
# w3 = grupa3.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20)
# plt.show()
# # Zadanie4
# df4 = pd.read_csv('datasets/zamowienia.csv', header=0, sep=';', decimal='.')
# grupa4 = df4.groupby('Sprzedawca').size()
# w4 = grupa4.plot.bar(ylabel='Ilość zamówień', title='Ilość złożonych zamówień przez poszczególnych sprzedawców')
# plt.subplots_adjust(bottom=0.2)
# plt.show()
