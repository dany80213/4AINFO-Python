from spaceships import Spaceship, CargoShip, ExplorationProbe

print("--- 1. TEST CARGO ---")
# Deve accettare nome e carico massimo
cargo = CargoShip("Nostromo", 1000) 
cargo.load(500)
# Deve consumare il doppio: 100 ly = 10 base + 10 extra = 20 fuel
cargo.fly(100) 
print(f"Fuel residuo cargo: {cargo.fuel} (Atteso: 80)")

print("\n--- 2. TEST PROBE ---")
probe = ExplorationProbe("Wall-E")
# Distanza < 100: Consumo 0
probe.fly(80)
print(f"Fuel residuo probe: {probe.fuel} (Atteso: 100)")
probe.scan()

# Test Sicurezza (Decommenta per vedere l'errore se hai usato @final correttamente)
class HackProbe(ExplorationProbe):
    pass