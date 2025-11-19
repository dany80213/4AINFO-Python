from marsmap import MarsMap
from Exceptions import RoverCollisionError,CommandNotFound,InvalidCommandError

class Rover:
    def __init__(self,x,y,direction,map : MarsMap):
        if not isinstance(x,int):
            raise TypeError("the coordinate  x must be a tuple")
        if not isinstance(y,int):
            raise TypeError("the coordinate  y must be a tuple")
        if not isinstance(map,MarsMap):
            raise TypeError("the map must be a MarsMap Object")
        if not isinstance(direction,str):
            raise TypeError("The direction must be a string")
        self.__x = x
        self.__y = y
        self.__direction = direction
        self.__map = map
        self.__directions = ["N","E","S","W","N","E","S","W"]

    
    @property
    def x(self):
        return self.__x
    @property 
    def y(self):
        return self.__y
    @property
    def direction(self):
        return self.__direction

    def turn_right(self):
            position = self.__directions.index(self.__direction)
            self.__direction = self.__directions[position+1]
    
    def turn_left(self):
            position = self.__directions.index(self.__direction)
            self.__direction = self.__directions[position-1]

    def move(self):
        new_pos = ()
        if self.__direction == "N":
            new_pos = (self.__x-1,self.__y)
        elif self.__direction == "W":
            new_pos = (self.__x,self.__y -1)
        elif self.__direction == "S":
            new_pos = (self.__x+1,self.__y)
        elif self.__direction == "E":
            new_pos = (self.__x,self.__y+1)

        if not self.__map.is_valid_position(new_pos[0],new_pos[1]):
            raise RoverCollisionError("Rover Collided")
        
        self.__x = new_pos[0]
        self.__y = new_pos[1]
    
    def scan(self):
        if self.__map.is_sample(self.__x,self.y):
            self.__map.collect_sample(self.__x,self.__y)
            return True
        else:
            return False
    
    def execute_commands(self,command_string : str) -> bool:
        commands = []
        if "," in command_string:  
            commands = command_string.split(",")
            for command in commands: 
                if command not in ['M','T_DX','T_SX','S']:
                    raise InvalidCommandError("Command given not valid")
            for command in commands:
                    if command == "M":
                        self.move()
                    elif command == "T_DX":
                        self.turn_right()
                    elif command == "T_SX":
                        self.turn_left()
                    elif command == "S":
                        self.scan()
                        
            return True
                
        else:
            if command_string == "M":
                self.move()
            elif command_string == "T_DX":
                self.turn_right()
            elif command_string == "T_SX":
                self.turn_left()
            elif command_string == "S":
                self.scan()
            else:
                raise InvalidCommandError("Command given not valid")
            return True




            
        