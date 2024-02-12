# Zdefiniować funkcję ,która pobiera jako pojedynczy parametr ciąg liczb i zwraca listę liczb
# trzycyfrowych, parzystych i takich, dla których druga cyfra jest mniejsza od trzeciej. W funkcji
# main pobieramy od użytkownika ciąg liczb, przekazujemy do funkcji (wywołujemy funkcje)
# odbieramy i wyświetlamy listę zwrócona przez funkcję.


def zwrocTrzyCyfParzDrugaMniejszaOdTrzeciej(liczby):

    trzyCyfParzDrugaMniejszaOdTrzeciej = []

    for liczba in liczby:

        if liczba >= 0:
            if len(str(liczba)) == 3 and liczba % 2 == 0:
                b = str(liczba)[1]
                c = str(liczba)[2]
                bInt = int(b)
                cInt = int(c)
                if bInt < cInt:
                    trzyCyfParzDrugaMniejszaOdTrzeciej.append(liczba)

        else:
            if len(str(liczba)) == 4 and liczba % 2 == 0:
                b = str(liczba)[2]
                c = str(liczba)[3]
                bInt = int(b)
                cInt = int(c)
                if bInt < cInt:
                    trzyCyfParzDrugaMniejszaOdTrzeciej.append(liczba)

    return trzyCyfParzDrugaMniejszaOdTrzeciej

if __name__ == '__main__':
    dlCiagu = int(input("Podaj dlugosc ciagu liczb: "))

    liczby = []

    for _ in range(dlCiagu):
        x = int(input("Podaj liczbe: "))
        liczby.append(x)

    result = zwrocTrzyCyfParzDrugaMniejszaOdTrzeciej(liczby)

    print(result)