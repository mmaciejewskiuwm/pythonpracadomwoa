from pakiety import ciagarytm
from pakiety import ciaggeo
# # Zadanie 1
#
# zbior1=[1-x for x in range(1,11)]
# print(zbior1)
#
# zbior2=[4**x for x in range(0,8)]
# print(zbior2)
#
# zbior3=[x for x in zadanieB if x%2==0]
# print(zbior3)


# 2
#
# import random
# lista1 = [random.randint(1,30) for x in range(0,10)]
# print(lista1)
#
# parzyste = [x for x in lista1 if x%2==0]
# print(parzyste)

# 3
#
# produkty = {'ziemniaki':'kg',"czekolada":'sztuki', 'mleko':'litry',"baterie":'sztuki',"loudy":'sztuki'}
# reczy = {a:b for (a,b) in produkty.items() if b == 'sztuki'}
# print(rzeczy)

# # Zadanie 4
#
# import math
# def czy_prosto(a,b,c):
# # C JEST NAJWIEKSZE #
#     if (c>a)&(c>b):
#         if((a**2)+(b**2)==(c**2)):
#             return ('Trojkat jest prostokatny.\n')
#         else:
#             return ('Trojkat nie jest prostokatny.\n')
# # A JEST NAJWIEKSZE #
#     elif(a > b) & (a > c):
#         if ((b ** 2) + (c ** 2) == (a ** 2)):
#             return ('Trojkat jest prostokatny.\n')
#         else:
#             return ('Trojkat nie jest prostokatny.\n')
# # B JEST NAJWIEKSZE #
#     elif (b > a) & (b > c):
#         if ((a ** 2) + (c ** 2) == (b ** 2)):
#             return ('Trojkat jest prostokatny.\n')
#         else:
#             return ('Trojkat nie jest prostokatny.\n')
#     else:
#         return ('Trojkat nie jest prostokatny.\n')
# ######################################################################
# print(czy_prosto(3,4,5))

# 5
#
# import math
# def pole_trapezu(a=2, b=10, h=3):
#     return ( (a+b)*h / 2 )
# print(pole_trapezu())

# 6
#
# import math
# def ciagXD(a=1, b=4, ile=10):
#     zadanie6 = [a+(b*x) for x in range(ile)]
#     print(zadanie6)
#     iloczyn_wyrazow_ciagu=1
#     for x in range(ile):
#         iloczyn_wyrazow_ciagu *= zadanie6[x]
#     return iloczyn_wyrazow_ciagu
# print(ciagXD())

# 7
#
# import math
# def ciagXD(* liczby):
#     if len(liczby)==0:
#         return 0
#     else:
#         zadanie7 = [x for x in liczby]
#         print(zadanie7)
#         iloczyn_wyrazow_ciagu = 1
#         for x in liczby:
#             iloczyn_wyrazow_ciagu *= x
#         return iloczyn_wyrazow_ciagu
# print(ciagXD(1,5,9,13))
#zad 8 jeszce nie zrobione
# def zakupy(** kwota):
#     for cos in kwota:
#         print("ilosc przedmiotow ", len(str(cos)))
#         print(kwota)
# zakupy(kwota="2zyla",produkty=['monka','sciera'])
#zad 9
# ciagarytm.arytmetyczny()
# ciaggeo.geometryczny()
