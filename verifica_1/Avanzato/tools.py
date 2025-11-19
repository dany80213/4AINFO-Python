class Collection:
    def __init__(self):
        self.__items = []

    def add(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.__items:
            raise ValueError("Collection empty")
        return self.__items.pop()

    def __len__(self):
        return len(self.__items)

    def __str__(self):
        return "\n".join(str(i) for i in self.__items)
    
    # def __str__(self):
    # return "\n".join(str(x) for x in self._ClassName__items)
    def __iadd__(self, card):
        self.add(card)
        return self   #mano += carta
    
    def __eq__(self, other):
        return self.value == other.value #Carta1 == #Carta2

    def __lt__(self, other):
        return self.value < other.value #Carta1 > Carta2
    
    def safe(fn, *args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            return f"Errore: {e}"    #safe(func,param1,param2)

@property
def attr(self):
    return self._attr

@attr.setter
def attr(self, value):
    self._attr = value



def matrix(rows, cols, fill=0):
    return [[fill for _ in range(cols)] for _ in range(rows)]