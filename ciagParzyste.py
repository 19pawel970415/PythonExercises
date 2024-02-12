# Opracować skrypt, który pobiera od użytkownika ciąg liczb i wyświetla tylko liczby parzyste

dlCiagu = int(input("Podaj dlugosc ciagu liczb: "))

liczby = []

for _ in range(dlCiagu):
    x = int(input("Podaj liczbe: "))
    liczby.append(x)

for liczba in liczby:
    if liczba % 2 == 0:
        print("Liczba parzysta: ", liczba)