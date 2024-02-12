# Zdefiniować funkcję, która pobiera jako parametry dwie nazwy plików. W swoim kodzie funkcja
# wczytuje zawartość pliku (słownik zawierający nazwy miast oraz ilość mieszkańców w miastach)
# podanego jako pierwszy parametr, wypisuje zawartość tego pliku i zapisuje do pliku podanego jako
# drugi parametr nowy słownik zawierający nazwy miast (wraz z ilością mieszkańców), w których
# liczba mieszkańców przekracza 300 000. W "funkcji main" wywołujemy tę funkcję.

def writeFromFileToFile(fileName1, fileName2):
    f1 = open('c://temp//' + fileName1, 'r')
    f2 = open('c://temp//' + fileName2, 'w')

    miastaPopulacja = f1.readlines()

    for miastoPopulacja in miastaPopulacja:
        print(miastoPopulacja)

    miastaPopulacjaLista = []

    for miastoPopulacja in miastaPopulacja:
        x = miastoPopulacja.split()
        miastaPopulacjaLista.append(x)

    final = []
    counter = 1
    for miastoPopulacjaLista in miastaPopulacjaLista:
        for x in miastoPopulacjaLista:
            if counter % 2 == 0:
                if int(x) > 300000 :
                    final.append(miastoPopulacjaLista)
            counter = counter + 1

    for y in final:
        f2.write(f"{y}" + "\n")

    f1.close()
    f2.close()


if __name__ == '__main__':
    fileName1 = input("Podaj nazwe pliku 1\n")
    fileName2 = input("Podaj nazwe pliku 2\n")

    writeFromFileToFile(fileName1, fileName2)
