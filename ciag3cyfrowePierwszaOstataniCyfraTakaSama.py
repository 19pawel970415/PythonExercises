# Opracować skrypt, który pobiera od użytkownika ciąg liczb i wyświetla tylko liczby trzycyfrowe,
# których pierwsza cyfra jest taka sama jak ostatnia (trzecia)

dlCiagu = int(input("Podaj dlugosc ciagu liczb: "))

liczby = []

for _ in range(dlCiagu):
    x = int(input("Podaj liczbe: "))
    liczby.append(x)

for liczba in liczby:
    if liczba >= 0:
        if len(str(liczba)) == 3 and str(liczba)[0] == str(liczba)[2]:
            print("Liczba parzysta: ", liczba)
    else:
        if len(str(liczba)) == 4 and str(liczba)[1] == str(liczba)[3]:
            print("Liczba parzysta: ", liczba)