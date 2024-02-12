# Zdefiniować funkcję, która pobiera jako parametry dwie liczby i działanie, które trzeba
# wykonać na tych liczbach. Działanie można przekazać w dowolny sposób. Funkcja zwraca wynik
# działania.
# W "funkcji main" pobieramy od użytkownika potrzebne dane, przekazujemy do funkcji
# (wywołujemy funkcję), odbieramy i wyświetlamy wartość zwróconą przez funkcję.

def wynikDzial(a, b, d):
    dzialanie = d

    if dzialanie == 1:
        return a + b
    if dzialanie == 2:
        return a - b
    if dzialanie == 3:
        return a * b
    if dzialanie == 4:
        return a / b
    if dzialanie == 5:
        return a ** b

if __name__ == '__main__':
    a = int(input("Podaj liczbe a\n"))
    b = int(input("Podaj liczbe b\n"))
    d = int(input("Podaj działanie jakie ma zostać wykonane:\n1. a + b\n2. a - b\n3. a * b\n4. a / b\n5. a ^ b\n"))

    wynik = wynikDzial(a, b, d)
    print(wynik)