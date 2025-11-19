from Exceptions import SampleNotFound

def matrix(rows, cols, fill=0):
    return [[fill for _ in range(cols)] for _ in range(rows)]

class MarsMap:
    def __init__(self,rows,cols):
        self.__map = matrix(rows,cols)
        self.__obstacles = list()
        self.__samples = list()

    def add_obstacle(self,x,y):
        if x > len(self.__map[0]) and y > len(self.__map):
            raise IndexError(f"The obstacle must be within the range  {len(self.__map[0])}x{len(self.__map)}")
        if not  isinstance(x,int) and isinstance(y,int):
            raise ValueError("the coordinates of the obstacle must be integers")
        self.__obstacles.append((x,y))
        
    def add_sample(self,x,y):
        if x > len(self.__map[0]) and y > len(self.__map):
            raise IndexError(f"The sample must be within the range  {len(self.__map[0])}x{len(self.__map)}")
        if not  isinstance(x,int) and isinstance(y,int):
            raise ValueError("the coordinates of the sample  must be integers")
        self.__samples.append((x,y))
    
    def is_valid_position(self,x,y):
        if x > len(self.__map[0]) or y > len(self.__map):
            return False
        elif (x,y) in self.__obstacles:
            return False
        else:
            return True
    
    def is_sample(self,x,y):
        if (x,y) in self.__samples:
            return True
        else:
            return False
        
    def collect_sample(self,x,y):
        if not (x,y) in self.__samples:
            raise SampleNotFound("Sample not found")
        self.__samples.remove((x,y))
    


