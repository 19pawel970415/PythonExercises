# Zdefiniować funkcję, która pobiera jako parametry dwie nazwy plików. W swoim kodzie funkcja
# wczytuje zawartość pliku (ma to być ciąg liczb) podanego jako pierwszy parametr, wypisuje
# zawartość tego pliku i zapisuje do pliku podanego jako drugi parametr listę zawierającą tylko liczby
# nieparzyste. W "funkcji main" wywołujemy tę funkcję

def zapiszDoPliku(fileName1, fileName2):
    f1 = open('c://temp//' + fileName1, 'r')
    f2 = open('c://temp//' + fileName2, 'w')

    liczby = f1.readlines()

    liczbyNieparzyste = []

    for liczba in liczby:
        print(liczba)
        if int(liczba) % 2 != 0:
            f2.write(liczba + "\n")

    f1.close()
    f2.close()



if __name__ == '__main__':
    nazwaPliku1 = input("Podaj nzawe pliku: ")
    nazwaPliku2 = input("Podaj nzawe pliku: ")

    zapiszDoPliku(nazwaPliku1, nazwaPliku2)
