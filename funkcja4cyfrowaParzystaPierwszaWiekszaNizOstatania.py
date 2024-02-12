#  Zdefiniować funkcję, która pobiera jako pojedynczy parametr ciąg liczb i zwraca listę liczb
# czterocyfrowych parzystych i takich, dla których pierwsza cyfra jest większa od czwartej. W
# "funkcji main" pobieramy od użytkownika ciąg liczb, przekazujemy do funkcji (wywołujemy
# funkcję), odbieramy i wyświetlamy listę zwróconą przez funkcję.

def zwrocCzteroCyfParzPierwwszaWiekszaNizOstatnia(liczby):

    czteroCyfParzPierwwszaWiekszaNizOstatnia = []

    for liczba in liczby:

        if liczba >= 0:
            if len(str(liczba)) == 4 and liczba % 2 == 0:
                a = str(liczba)[0]
                b = str(liczba)[3]
                aInt = int(a)
                bInt = int(b)
                if aInt > bInt:
                    czteroCyfParzPierwwszaWiekszaNizOstatnia.append(liczba)

        else:
            if len(str(liczba)) == 5 and liczba % 2 == 0:
                a = str(liczba)[1]
                b = str(liczba)[4]
                aInt = int(a)
                bInt = int(b)
                if aInt > bInt:
                    czteroCyfParzPierwwszaWiekszaNizOstatnia.append(liczba)

    return czteroCyfParzPierwwszaWiekszaNizOstatnia

if __name__ == '__main__':
    dlCiagu = int(input("Podaj dlugosc ciagu liczb: "))

    liczby = []

    for _ in range(dlCiagu):
        x = int(input("Podaj liczbe: "))
        liczby.append(x)

    result = zwrocCzteroCyfParzPierwwszaWiekszaNizOstatnia(liczby)

    print(result)
