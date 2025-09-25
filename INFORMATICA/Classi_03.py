from math import sqrt

class Punto: 
    def __init__(self,x:int,y:int):
        self.coordinata_x = x
        self.coordinata_y = y
    
    def distanza_origine(self):
        return sqrt(self.coordinata_x**2 + self.coordinata_y**2)
    
    def distanza(self,altro_punto):
        return sqrt((self.coordinata_x - altro_punto.coordinata_x)**2 + (self.coordinata_y - altro_punto.coordinata_y)**2)
    
    def visualizza(self):
        print(f"({self.coordinata_x},{self.coordinata_y})")
    
class Rettangolo:
    def __init__ (self,p1,p2):
        self.punto1 = (p1.coordinata_x,p1.coordinata_y)
        self.punto2 = (p2.coordinata_x,p2.coordinata_y)
    
    def base(self):
        return abs(self.punto1[0]- self.punto2[0])
    
    def altezza(self):
        return abs(self.punto1[1]- self.punto2[1])
    
    def area(self):
        return self.base() * self.altezza()
    
    def contiene(self,p):
        if (p.coordinata_x >= min(self.punto1[0],self.punto2[0]) and (p.coordinata_x <= max(self.punto1[0],self.punto2[0])) and
            (p.coordinata_y >= min(self.punto1[1],self.punto2[1]) and (p.coordinata_y <= max(self.punto1[1],self.punto2[1])))):
            return True
        return False
    

# p1 = Punto(2,3)
# p2 = Punto(5,7)
# print(p1.distanza_origine())
# print(p1.distanza(p2))
# p1.visualizza()
# rettangolo = Rettangolo(p1,p2)
# print(rettangolo.base())
# print(rettangolo.altezza())
# print(rettangolo.area())
# print(rettangolo.contiene(Punto(1,4)))