import matplotlib.pyplot as plt


def writeFromFileToFile(fileName1, fileName2):
    f1 = open('c://temp//' + fileName1, 'r')
    f2 = open('c://temp//' + fileName2, 'w')

    stacjeCisnienie = f1.readlines()

    for stacjaCisnienie in stacjeCisnienie:
        print(stacjaCisnienie)

    stacjeCisnienieLista = []
    stacjeCisnienieSlownik = {}

    for stacjaCisnienie in stacjeCisnienie:
        x = stacjaCisnienie.split()
        stacjeCisnienieLista.append(x)

    counter = 1
    sum = 0
    for stacjaCisnienieLista in stacjeCisnienieLista:
        for x in stacjaCisnienieLista:
            if counter % 2 == 0:
                sum = sum + float(x)
                cisnienie = x
            else:
                stacja = x
            counter = counter + 1
        stacjeCisnienieSlownik[stacja] = float(cisnienie)

    counter = counter - 1
    counterP = counter / 2
    avg = sum / counterP

    print("Do pliku zostanie zapisane: Srednia z " + f"{int(counterP)}" + " stacji wynosi " + f"{avg}" + " hektopaskali.")

    f2.write("Srednia z " + f"{int(counterP)}" + " stacji wynosi " + f"{avg}" + " hektopaskali.")

    t = "Avg"

    stacjeCisnienieSlownik[t] = avg

    data = stacjeCisnienieSlownik
    stacje = list(data.keys())
    cisnienia = list(data.values())
    fig = plt.figure(figsize=(10, 5))
    plt.bar(stacje, cisnienia, color='maroon',
            width=0.4)

    plt.ylim(850, 1100)
    plt.xlabel("Id Stacji synoptycznej")
    plt.ylabel("Cisnienie")
    plt.title("Cisnienie w stacjach synoptycznych")
    plt.show()

    f1.close()
    f2.close()


if __name__ == '__main__':
    fileName1 = input("Podaj nazwe pliku 1\n")
    fileName2 = input("Podaj nazwe pliku 2\n")

    writeFromFileToFile(fileName1, fileName2)