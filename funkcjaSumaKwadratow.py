# Zdefiniować funkcję, która pobiera jako pojedynczy parametr ciąg liczb i zwraca sumę
# kwadratów liczb tego ciągu. W "funkcji main" pobieramy od użytkownika ciąg liczb, przekazujemy
# do funkcji (wywołujemy funkcję), odbieramy i wyświetlamy wartość zwróconą przez funkcję

def zwrocSumeKwadratow(liczby):
    kwadraty = []
    for y in liczby:
        y = y * y
        kwadraty.append(y)
    suma = 0
    for z in kwadraty:
        suma = suma + z

    return suma


if __name__ == '__main__':
    dlCiagu = int(input("Podaj dlugosc ciagu liczb: "))

    liczby = []

    for _ in range(dlCiagu):
        x = int(input("Podaj liczbe: "))
        liczby.append(x)

    sumaKwadratow = zwrocSumeKwadratow(liczby)

    print(sumaKwadratow)