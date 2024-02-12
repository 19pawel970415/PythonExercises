# Zdefiniować funkcję, która pobiera jako parametry dwie nazwy plików. W swoim kodzie
# funkcja wczytuje zawartość pliku (ma to być ciąg liczb) podanego jako pierwszy parametr,
# wypisuje zawartość tego pliku i zapisuje do pliku podanego jako drugi parametr sumę kwadratów
# liczb wczytanego ciągu. W "funkcji main" wywołujemy tę funkcję

def writeFromFileToFile(fileName1, fileName2):
    f1 = open('c://temp//' + fileName1, 'r')
    f2 = open('c://temp//' + fileName2, 'w')

    liczby = f1.readlines()

    liczbyInt = []

    for z in liczby:
        print(z)
        liczbyInt.append(int(z))

    kwadraty = []
    for y in liczbyInt:
        y = y * y
        kwadraty.append(y)
    suma = 0
    for z in kwadraty:
        suma = suma + z

    f2.write(str(suma))

    f1.close()
    f2.close()


if __name__ == '__main__':
    fileName1 = input("Podaj nazwe pliku 1\n")
    fileName2 = input("Podaj nazwe pliku 2\n")

    writeFromFileToFile(fileName1, fileName2)