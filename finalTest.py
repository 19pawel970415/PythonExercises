def zwrocSilnie(liczba):
    silnia = 1
    while liczba >= 1:
        silnia = silnia * liczba
        liczba = liczba - 1
    return silnia + 10

if __name__ == '__main__':
    liczba = int(input("Podaj liczbe, ktorej silnie powiekszona o 10 chcesz policzyc: "))

    zwroconaSilnia = zwrocSilnie(liczba)

    print(zwroconaSilnia)

def zwrocTrzyCyfParzPierwszaMniejszaOdTrzeciej(liczby):

    trzyCyfParzPierwszaMniejszaOdTrzeciej = []

    for liczba in liczby:

        if liczba >= 0:
            if len(str(liczba)) == 3 and liczba % 2 == 0:
                b = str(liczba)[0]
                c = str(liczba)[2]
                bInt = int(b)
                cInt = int(c)
                if bInt < cInt:
                    trzyCyfParzPierwszaMniejszaOdTrzeciej.append(liczba)

        else:
            if len(str(liczba)) == 4 and liczba % 2 == 0:
                b = str(liczba)[1]
                c = str(liczba)[3]
                bInt = int(b)
                cInt = int(c)
                if bInt < cInt:
                    trzyCyfParzPierwszaMniejszaOdTrzeciej.append(liczba)

    return trzyCyfParzPierwszaMniejszaOdTrzeciej

if __name__ == '__main__':
    dlCiagu = int(input("Podaj dlugosc ciagu liczb: "))

    liczby = []

    for _ in range(dlCiagu):
        x = int(input("Podaj liczbe: "))
        liczby.append(x)

    result = zwrocTrzyCyfParzPierwszaMniejszaOdTrzeciej(liczby)

    print(result)

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
            if len(str(liczba)) == 3:
                f2.write(str(liczba) + "\n")
        else:
            if len(str(liczba)) == 4:
                f2.write(str(liczba) + "\n")

    f1.close()
    f2.close()

if __name__ == '__main__':
    nazwaPliku1 = input("Podaj nzawe pliku: ")
    nazwaPliku2 = input("Podaj nzawe pliku: ")

    zapiszDoPliku(nazwaPliku1, nazwaPliku2)

class Person:
  def __init__(self, age, name):
    self.age = age
    self.name = name

  def myfunction(self):
    print(self.name)
    self.age = self.age + 100
    return self.age


if __name__ == '__main__':
    p1 = Person(25, "Paul")
    age = p1.myfunction()
    print(age)

class DuzaLiczba(Exception):

    komunikat = "Jakas liczba w ciagu jest wieksza od 10"
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
            if x > 10:
                raise DuzaLiczba("Jakas liczba w ciagu jest wieksza od 10")
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