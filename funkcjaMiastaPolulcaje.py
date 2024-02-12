# Zdefiniować funkcję, która pobiera jako pojedynczy parametr słownik zawierający nazwy miast
# oraz ilość mieszkańców w miastach. Funkcja zwraca nowy słownik zawierający nazwy miast (wraz
# z ilością mieszkańców), w których liczba mieszkańców przekracza 300 000. W "funkcji main"
# pobieramy od użytkownika ciąg nazw miast wraz z ilością mieszkańców, przekazujemy do funkcji
# (wywołujemy funkcję), odbieramy i wyświetlamy słownik zwrócony przez funkcję

def zwrocMiastaPowyzej300000(miastaPopulacja):
    result = {}
    for x, y in miastaPopulacja.items():
        if y > 300000:
            result[x] = y
    return result


if __name__ == '__main__':
    dlCiagu = int(input("Podaj ile miast chcesz wpisac: "))

    miastaPopulacja = {}

    for _ in range(dlCiagu):
        miasto = input("Podaj nazwe miasta: ")
        populacja = int(input("Podaj populacje miasta: "))

        miastaPopulacja[miasto] = populacja

    zwroconeMiastaPowyzej300000 = zwrocMiastaPowyzej300000(miastaPopulacja)

    print(zwroconeMiastaPowyzej300000)


