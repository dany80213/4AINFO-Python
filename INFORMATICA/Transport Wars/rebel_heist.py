import random
from spaceships import SupplyDrone, RebelHacker

# --- 1. SETUP SCIAME ---
print("--- GENERAZIONE SCIAME ---")
swarm = []
for i in range(200):
    credits = random.randint(500, 5000) # Crediti
    time = random.randint(5, 40)    # Minuti per l'hack
    # Nota: ID fittizio nel nome
    drone = SupplyDrone(f"Drone-{i:02d}", credits, time) 
    swarm.append(drone)

print(f"Sciame intercettato: {len(swarm)} droni.")
print("Tempo disponibile: 60 minuti.\n")

# --- 2. RIBELLI IN AZIONE ---
rebels = RebelHacker()

# Eseguiamo la rapina ottimizzata
stolen_drones, total_credits = rebels.optimize_heist(swarm, 60)

# --- 3. REPORT ---
print("--- RAPPORTO MISSIONE ---")
time_spent = 0
for drone in stolen_drones:
    eff = drone.value / drone.hack_time
    print(f"✅ Hacked {drone.name}: {drone.value} cr | {drone.hack_time} min | Eff: {eff:.1f}")
    time_spent += drone.hack_time

print("-" * 30)
print(f"💰 TOTALE RUBATO: {total_credits} Crediti")
print(f"⏱️ TEMPO USATO: {time_spent} / 60 minuti") # Non considera lo skil_level 
print(f"📦 DRONI VIOLATI: {len(stolen_drones)} su {len(swarm)}")