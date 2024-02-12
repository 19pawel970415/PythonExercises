# Opracować skrypt, który pobiera od użytkownika współczynniki wielomianu oraz pewien punkt
# na prostej liczb rzeczywistych i oblicza wartość wielomianu w tym punkcie

iloscWsp = int(input("Podaj ilosc wspolczynnikow wielomianu: "))

wspolczynniki = []

for _ in range(iloscWsp):
    x = int(input("Podaj wspolczynnik wielomianu: "))
    wspolczynniki.append(x)

punkt = int(input("Podaj punkt na prostej: "))

suma = 0
p = 0

for wspolczynnik in wspolczynniki:
    suma = suma + (wspolczynnik * pow(punkt, p))
    p = p + 1

print(suma)