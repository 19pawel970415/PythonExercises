# Opracować skrypt, który pobiera od użytkownika ciąg liczb i wyświetla tylko liczby
# czterocyfrowe, których suma pierwszej i ostatniej (czwartej) cyfry jest parzysta

dlCiagu = int(input("Podaj dlugosc ciagu liczb: "))

liczby = []

for _ in range(dlCiagu):
    x = int(input("Podaj liczbe: "))
    liczby.append(x)

for liczba in liczby:

    if liczba >= 0:
        if len(str(liczba)) == 4:
            a = str(liczba)[0]
            b = str(liczba)[3]
            aInt = int(a)
            bInt = int(b)
            suma = aInt + bInt
            if suma % 2 == 0:
                print(liczba)
    else:
        if len(str(liczba)) == 5:
            a = str(liczba)[1]
            b = str(liczba)[4]
            aInt = int(a)
            bInt = int(b)
            suma = aInt + bInt
            if suma % 2 == 0:
                print(liczba)
