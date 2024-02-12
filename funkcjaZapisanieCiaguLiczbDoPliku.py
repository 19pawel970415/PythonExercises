# Zdefiniować funkcję, która pobiera jako pojedynczy parametr nazwę pliku, w swoim kodzie
# pobiera od użytkownika ciąg liczb i zapisuje ten ciąg do pliku o podanej nazwie

def zapiszDoPliku(fileName):
    f = open('c://temp//' + fileName, 'w')

    d = int(input("Podaj dlugosc ciagu liczb: "))
    for _ in range(d):
        x = input("Podaj wyraz ciagu: ")
        f.write(x)

    f.close()

if __name__ == '__main__':
    fileName = input("Podaj nzawe pliku: ")
    zapiszDoPliku(fileName)