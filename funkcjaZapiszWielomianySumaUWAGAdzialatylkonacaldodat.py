# Zdefiniować funkcję, która pobiera z pliku podanego jako pierwszy parametr:
# -współczynniki dwóch wielomianów,
# wyświetla wartości wczytane z pliku,oblicza wyświetla i zapisuje do pliku podanego jako drugi parametr sumę tych wielomianów.
# W "funkcji main" wywołujemy tę funkcję

def writeFromFileToFile(fileName1, fileName2):
    f1 = open('c://temp//' + fileName1, 'r')
    f2 = open('c://temp//' + fileName2, 'w')

    wspolczynnikiWLiscie = f1.readlines()

    for wspolczynnikWLiscie in wspolczynnikiWLiscie:
        print(wspolczynnikWLiscie, end='')

    wspolczynniki1 = []
    wspolczynniki2 = []
    counter = 1

    for wspolczynnikWLiscie in wspolczynnikiWLiscie:
        if (counter == 1):
            for x in wspolczynnikWLiscie:
                wspolczynniki1.append(x)
            counter = counter + 1
        else:
            for x in wspolczynnikWLiscie:
                wspolczynniki2.append(x)

    wspolczynniki1Float = []
    wspolczynniki2Float = []

    counter = 1
    for x in wspolczynniki1:
        if (counter % 2 != 0):
            wspolczynniki1Float.append(float(x))
        counter = counter + 1

    counter = 1
    for x in wspolczynniki2:
        if (counter % 2 != 0):
            wspolczynniki2Float.append(float(x))
        counter = counter + 1

    a = len(wspolczynniki1Float)
    b = len(wspolczynniki2Float)

    print()

    if a > b:
        for x in range(0, len(wspolczynniki2Float)):
            wspolczynniki1Float[x] = wspolczynniki1Float[x] + wspolczynniki2Float[x]
            print(f"{wspolczynniki1Float[x]}" + " ", end='')
            f2.write(f"{wspolczynniki1Float[x]}" + " ")

        N = len(wspolczynniki1Float) - len(wspolczynniki2Float)

        res = wspolczynniki1Float[-N:]

        for x in res:
            print(f"{x}" + " ", end='')
            f2.write(f"{x}" + " ")
    else:
        for x in range(0, len(wspolczynniki1Float)):
            wspolczynniki2Float[x] = wspolczynniki1Float[x] + wspolczynniki2Float[x]
            print(f"{wspolczynniki2Float[x]}" + " ", end='')
            f2.write(f"{wspolczynniki2Float[x]}" + " ")

        N = len(wspolczynniki2Float) - len(wspolczynniki1Float)

        res = wspolczynniki2Float[-N:]

        for x in res:
            print(f"{x}" + " ", end='')
            f2.write(f"{x}" + " ")

    f1.close()
    f2.close()


if __name__ == '__main__':
    fileName1 = input("Podaj nazwe pliku 1\n")
    fileName2 = input("Podaj nazwe pliku 2\n")

    writeFromFileToFile(fileName1, fileName2)
