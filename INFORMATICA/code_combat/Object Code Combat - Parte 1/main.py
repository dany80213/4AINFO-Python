from player import Player
from random import randint,choice
import time 


if __name__ == "__main__" :
    p1 = Player("Name1",100,randint(1,20),randint(1,20))
    p2 = Player("Name2",100,randint(1,20),randint(1,20))
    turno = 0
    players = [p1,p2]
    print("=== SIMULAZIONE COMBATTIMENTO ===")

    for p in players:
        print(f"{p.name}: Forza={p.strength}, Destrezza={p.dexterity}")
        p.equip(choice(p.get_weapons()))
        print(f"🗡️ {p.name} equipaggia: {p.weapon}")

    print("=== INIZIO COMBATTIMENTO ===")

    while p1.is_alive() and p2.is_alive():
        time.sleep(3)
        turno +=1
        print(f"--- Turno {turno} ---")
        players[(turno-1) % 2].attack(players[turno % 2])
    if p1.health == p2.health:
        print(f"🤝 Pareggio!")
    else:
        winner = p1 if p1.health > 0 else p2
        print("=== FINE COMBATTIMENTO ===")
        print(f"🏆 {winner.name} vince il combattimento! {winner}")
                



