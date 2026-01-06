from exceptions import InsufficientFuelError, MaxLoadExceededError
from typing import final

class Spaceship:
    def __init__(self,name):
        self.name = name
        self.fuel = 100
    

    def fly(self,distance):
        if distance // 10 > self.fuel:
            raise InsufficientFuelError("The fuel is not enough, can't make it to the destination")
        
        else:
            print(f"{self.name} percorre {distance} anni luce")
            self.fuel -= distance // 10

    @final
    def dock(self):
        print(f"{self.name} esegue la procedura di attracco standard.")



class CargoShip(Spaceship):
    def __init__(self, name, max_load):
        super().__init__(name)
        self.__max_load = max_load
        self.__current_load = 0
    
    def load(self,amount):
        if self.__current_load + amount > self.__max_load:
            raise MaxLoadExceededError("Max Load Exceeded")
        else:
            self.__current_load += amount
        
    
    def fly(self,distance):
        try:
            super().fly(distance)
            self.fuel -= distance // 10 
        except InsufficientFuelError as e:
            print(f"Error: {e}")

@final
class ExplorationProbe(Spaceship):
    def __init__(self, name):
        super().__init__(name)

    def fly(self,distance):
        if distance >= 100:
            super().fly(distance)
    
    def scan(self):
        print(f"{self.name} scansiona l'area.")


class SupplyDrone(Spaceship):
    def __init__(self, name,value,hack_time):
        super().__init__(name)
        self.value = value
        self.hack_time = hack_time


class RebelHacker:
    def __init__(self,skill_level = 1):
        if skill_level <= 5:
            self.skill_level = skill_level
        
    def manual_sort(self,drones):
        for _ in range(len(drones)):
            changed = False
            for i in range(len(drones)-1):
                if drones[i].value / drones[i].hack_time < drones[i+1].value / drones[i+1].hack_time:
                    drones[i],drones[i+1] = drones[i+1],drones[i]
                    changed = True
                
            if not changed:
                break

    def optimize_heist(self,drones,time_limit):
        self.manual_sort(drones)
        stolen_drones = list()
        total = 0
        for drone in drones:
            T_real = drone.hack_time * (1 - 0.10 * self.skill_level)
            if T_real <= time_limit:
                stolen_drones.append(drone)
                total += drone.value
                time_limit -= T_real

        return stolen_drones,total


            



        
    


