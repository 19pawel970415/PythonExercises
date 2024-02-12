# Opracować skrypt, który pobiera od użytkownika nazwy miast oraz ilość mieszkańców w
# miastach i wyświetla nazwy miast (wraz z ilością mieszkańców), w których liczba mieszkańców
# przekracza 300 000

dlCiagu = int(input("Podaj ile miast chcesz wpisac: "))

miastaPopulacja = {}

for _ in range(dlCiagu):
    miasto = input("Podaj nazwe miasta: ")
    populacja = int(input("Podaj populacje miasta: "))

    miastaPopulacja[miasto] = populacja

for x, y in miastaPopulacja.items():
    if y > 300000:
        print(x, y)