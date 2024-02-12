# Zdefiniować klasę wyjątku DużaLiczba, która dziedziczy po klasie Exception. Konstruktor klasy
# jako parametr przyjmuje tekst wypisywany, kiedy generowany jest wyjątek. Zdefiniować
# funkcję, która pobiera jako pojedynczy parametr nazwę pliku. W swoim kodzie funkcja
# wczytuje zawartość pliku podanego jako parametr i wypisuje zawartość tego pliku (ciąg liczb).
# Jeżeli jakakolwiek liczba z pliku jest większa od 20, to generujemy wyjątek DużaLiczba. W
# funkcji main wywołujemy tę funkcję i w klauzuli except obsługujemy wyjątek DużaLiczba.


class DuzaLiczba(Exception):

    komunikat = "Liczba jest wieksza od 20"
    def __init__(self, komunikat):
        self.komunikat = komunikat

def writeToFile(fileName):
    f = open('c://temp//' + fileName, 'r')

    liczby = f.readlines()

    liczbyInt = [int(x) for x in liczby]

    for x in liczbyInt:
        print(x)

    for x in liczbyInt:
        try:
            if x > 20:
                raise DuzaLiczba("Jakas liczba w ciagu jest wieksza od 20")
        except DuzaLiczba as wyj:
            print("Wystapienie wyjatku: DuzaLiczba")
            print(wyj)

    f.close()


if __name__ == '__main__':

    try:
        fileName = input("Podaj nazwe pliku\n")
        writeToFile(fileName)
    except (FileNotFoundError):
        print("Podany plik nie istnieje")