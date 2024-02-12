# Zdefiniować klasę, która ma dwa pola inicjalizowane w konstruktorze oraz jedną metodę.
# Metoda wypisuje zawartość drugiego pola klasy oraz dodaje wartość 20 do pierwszego pola
# klasy i następnie zwraca wartość pierwszego pola. W funkcji main tworzymy obiekt tej klasy i
# wywołujemy metodę wypisując na ekranie wartość zwróconą przez metodę.


class Person:
  def __init__(self, age, name):
    self.age = age
    self.name = name

  def myfunction(self):
    print(self.name)
    self.age = self.age + 20
    return self.age


if __name__ == '__main__':
    p1 = Person(20, "Nina")
    age = p1.myfunction()
    print(age)