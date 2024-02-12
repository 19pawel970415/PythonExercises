# Zdefiniować funkcję, która pobiera jako parametry dwie nazwy plików. W swoim kodzie funkcja
# wczytuje zawartość pliku (ma to być ciąg liczb) podanego jako pierwszy parametr, wypisuje
# zawartość tego pliku i zapisuje do pliku podanego jako drugi parametr listę liczb czterocyfrowych
# parzystych i takich, dla których trzecia cyfra jest większa od czwartej. W "funkcji main"wywołujemy tę funkcję

def zapiszDoPliku(fileName1, fileName2):
    f1 = open('c://temp//' + fileName1, 'r')
    f2 = open('c://temp//' + fileName2, 'w')

    liczby = f1.readlines()
    liczbyInt = []

    for liczba in liczby:
        liczbyInt.append(int(liczba))

    for liczba in liczbyInt:
        print(liczba)

    for liczba in liczbyInt:

        if liczba >= 0:
            if len(str(liczba)) == 4 and liczba % 2 == 0:
                a = str(liczba)[2]
                b = str(liczba)[3]
                aInt = int(a)
                bInt = int(b)
                if aInt > bInt:
                    f2.write(str(liczba) + "\n")
        else:
            if len(str(liczba)) == 5 and liczba % 2 == 0:
                a = str(liczba)[3]
                b = str(liczba)[4]
                aInt = int(a)
                bInt = int(b)
                if aInt > bInt:
                    f2.write(str(liczba) + "\n")

    f1.close()
    f2.close()

if __name__ == '__main__':
    nazwaPliku1 = input("Podaj nzawe pliku: ")
    nazwaPliku2 = input("Podaj nzawe pliku: ")

    zapiszDoPliku(nazwaPliku1, nazwaPliku2)
