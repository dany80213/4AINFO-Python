from spaceships import Spaceship,CargoShip,ExplorationProbe,SupplyDrone

class FleetManager:
    def __init__(self):
        self.fleet = list()

    def add_ship(self,ship):
        if not isinstance(ship,(Spaceship,CargoShip,ExplorationProbe,SupplyDrone)):
            raise TypeError(f"Incorrect type of ship")
        self.fleet.append(ship)

    def get_total_drone_value(self):
        total = 0
        for ship in self.fleet:
            if isinstance(ship,SupplyDrone):
                total += ship.value
        return total
    
    def get_optimal_ship(self,distance):
        if not self.fleet:
            raise ValueError("Fleet is empty. Cannot determine the optimal ship.")
        optimal_ship = None
        min_value = float('inf')
        value = 0
        for ship in self.fleet:
            if isinstance(ship,CargoShip):
                value = (distance // 10) * 2
            elif isinstance(ship,ExplorationProbe):
                if distance >= 100:
                    value = distance // 10
                else:
                    value = 0 
            if value < min_value:
                min_value = value
                optimal_ship = ship
        return optimal_ship

