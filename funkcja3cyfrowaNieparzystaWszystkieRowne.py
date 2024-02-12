# Zdefiniować funkcję, która pobiera jako pojedynczy parametr ciąg liczb i zwraca listę liczb
# trzycyfrowych nieparzystych i takich, dla których wszystkie cyfry są takie same.
# W "funkcji main"pobieramy od użytkownika ciąg liczb, przekazujemy do funkcji (wywołujemy funkcję), odbieramy
# i wyświetlamy listę zwróconą przez funkcję

def zwrocTrzyCyfNieparzWszystkieCyfTakieSame(liczby):

    trzyCyfNieparzWszystkieCyfTakieSame = []

    for liczba in liczby:

        if liczba >= 0:
            if len(str(liczba)) == 3 and liczba % 2 != 0:
                a = str(liczba)[0]
                b = str(liczba)[1]
                c = str(liczba)[2]
                aInt = int(a)
                bInt = int(b)
                cInt = int(c)
                if aInt == bInt == cInt:
                    trzyCyfNieparzWszystkieCyfTakieSame.append(liczba)

        else:
            if len(str(liczba)) == 4 and liczba % 2 != 0:
                a = str(liczba)[1]
                b = str(liczba)[2]
                c = str(liczba)[3]
                aInt = int(a)
                bInt = int(b)
                cInt = int(c)
                if aInt == bInt == cInt:
                    trzyCyfNieparzWszystkieCyfTakieSame.append(liczba)

    return trzyCyfNieparzWszystkieCyfTakieSame

if __name__ == '__main__':
    dlCiagu = int(input("Podaj dlugosc ciagu liczb: "))

    liczby = []

    for _ in range(dlCiagu):
        x = int(input("Podaj liczbe: "))
        liczby.append(x)

    result = zwrocTrzyCyfNieparzWszystkieCyfTakieSame(liczby)

    print(result)
