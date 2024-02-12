# Zdefiniować funkcję, która pobiera jako pojedynczy parametr liczbę całkowitą, oblicza i
# zwraca wartość silni (dla tej liczby) powiększoną o wartość 100 ( wartość silni jest
# powiększona ). W funkcji main pobieramy od użytkownika liczbę całkowitą , przekazujemy do
# funkcji i wywołujemy funkcję odbieramy i wyświetlamy wartość zwróconą przez funkcję.


def zwrocSilnie(liczba):
    silnia = 1
    while liczba >= 1:
        silnia = silnia * liczba
        liczba = liczba - 1
    return silnia + 100

if __name__ == '__main__':
    liczba = int(input("Podaj liczbe, ktorej silnie chcesz policzyc: "))

    zwroconaSilnia = zwrocSilnie(liczba)

    print(zwroconaSilnia)