# Zdefiniować funkcję, która pobiera jako parametry dwie nazwy plików. W swoim kodzie funkcja
# wczytuje zawartość pliku (ma to być pojedyncza liczba) podanego jako pierwszy parametr,
# wypisuje zawartość tego pliku, oblicza wypisuje i zapisuje do pliku podanego jako drugi parametr
# wartość silni dla liczby wczytanej z pliku. W "funkcji main" wywołujemy tę funkcję

def zapiszDoPliku(fileName1, fileName2):
    f1 = open('c://temp//' + fileName1, 'r')
    f2 = open('c://temp//' + fileName2, 'w')

    liczba = f1.readline()

    liczbaInt = int(liczba)

    print(liczbaInt)

    silnia = 1
    while liczbaInt >= 1:
        silnia = silnia * liczbaInt
        liczbaInt = liczbaInt - 1

    f2.write(str(silnia))

    f1.close()
    f2.close()

if __name__ == '__main__':
    nazwaPliku1 = input("Podaj nzawe pliku: ")
    nazwaPliku2 = input("Podaj nzawe pliku: ")

    zapiszDoPliku(nazwaPliku1, nazwaPliku2)
