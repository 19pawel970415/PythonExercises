# Zdefiniować funkcję, która pobiera jako pojedynczy parametr ciąg liczb i zwraca listę
# zawierającą tylko liczby nieparzyste. W "funkcji main" pobieramy od użytkownika ciąg liczb,
# przekazujemy do funkcji (wywołujemy funkcję), odbieramy i wyświetlamy listę zwróconą przez
# funkcję.

def drukNieparz(liczby):
    liczbyNieparzyste = []
    for liczba in liczby:
        if liczba % 2 != 0:
            liczbyNieparzyste.append(liczba)
    return liczbyNieparzyste

if __name__ == '__main__':
    dlCiagu = int(input("Podaj dlugosc ciagu liczb: "))

    liczby = []

    for _ in range(dlCiagu):
        x = int(input("Podaj liczbe: "))
        liczby.append(x)

    zwroconeLiczbyNieparzyste = drukNieparz(liczby)

    for zwroconaLiczbaNieparzysta in zwroconeLiczbyNieparzyste:
        print(zwroconaLiczbaNieparzysta)