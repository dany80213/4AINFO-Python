class Studente:
    def __init__(self,nome,cognome,codice_fiscale,matricola):
        self.nome  = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.matricola = matricola

    def __str__(self):
        return f"{self.nome} {self.cognome} {self.codice_fiscale} {self.matricola}"
    


# Triangolo.py
from math import sqrt


class Triangolo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_valido(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return False
        return (self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.b + self.c > self.a)

    def tipo_lati(self):
        if not self.is_valido():
            return "Non valido"

        if self.a == self.b and self.b == self.c:
            return "Equilatero"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "Isoscele"
        else:
            return "Scaleno"

    def is_rettangolo(self):
        if not self.is_valido():
            return False
        if self.a * self.a + self.b * self.b == self.c * self.c:
            return True
        if self.a * self.a + self.c * self.c == self.b * self.b:
            return True
        if self.b * self.b + self.c * self.c == self.a * self.a:
            return True
        return False

    def tipo_completo(self):
        tipo = self.tipo_lati()
        if tipo == "Non valido":
            return tipo
        if self.is_rettangolo():
            return tipo + " (Rettangolo)"
        return tipo
    def perimetro(self):
        if not self.is_valido():
            return None
        return self.a + self.b + self.c

    def area(self):
        if not self.is_valido():
            return None
        p = self.perimetro() / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def numero_diagonali(self):
        if not self.is_valido():
            return None
        return 0

    def diagonali(self):
        if not self.is_valido():
            return None
        return []
    def mostra_risultati(self):
        print("=== TRIANGOLO ===")
        print("Lati:", self.a, self.b, self.c)
        print("Valido:", self.is_valido())
        print("Tipo:", self.tipo_completo())

        if self.is_valido():
            print("Perimetro:", self.perimetro())
            print("Area:", self.area())
            print("Numero diagonali:", self.numero_diagonali())
            print("Diagonali:", self.diagonali())
        else:
            print("Calcoli non disponibili")



if __name__ == "__main__":
    triangoli = [
        Triangolo(3, 3, 3),   # equilatero
        Triangolo(5, 5, 8),   # isoscele
        Triangolo(3, 4, 5),   # scaleno rettangolo
        Triangolo(1, 2, 10)   # non valido
    ]

    for t in triangoli:
        t.mostra_risultati()
        print()