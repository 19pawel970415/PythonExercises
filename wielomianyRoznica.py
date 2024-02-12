# Opracować skrypt, który pobiera od użytkownika współczynniki dwóch wielomianów, wypisuje
# te wielomiany na ekranie oraz oblicza i wypisuje na ekranie różnicę tych wielomianów.

iloscWsp1 = int(input("Podaj ilosc wspolczynnikow 1. wielomianu: "))

wspolczynniki1 = []

for _ in range(iloscWsp1):
    x = int(input("Podaj wspolczynnik 1. wielomianu: "))
    wspolczynniki1.append(x)

iloscWsp2 = int(input("Podaj ilosc wspolczynnikow 2. wielomianu: "))

wspolczynniki2 = []

for _ in range(iloscWsp2):
    x = int(input("Podaj wspolczynnik 2. wielomianu: "))
    wspolczynniki2.append(x)

for wspolczynnik1 in wspolczynniki1:
    print(wspolczynnik1, end=" ")

print()

for wspolczynnik2 in wspolczynniki2:
    print(wspolczynnik2, end=" ")

print()

if iloscWsp2 > iloscWsp1:
    for x in range(0, iloscWsp1):
        wspolczynniki2[x] = wspolczynniki2[x] - wspolczynniki1[x]
    for wspolczynnik2 in wspolczynniki2:
        print(wspolczynnik2, end=" ")
else:
    for x in range(0, iloscWsp2):
        wspolczynniki1[x] = wspolczynniki1[x] - wspolczynniki2[x]
    for wspolczynnik1 in wspolczynniki1:
        print(wspolczynnik1, end=" ")