from player import Player
from potion import Potion
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
        p.potions = Potion("Healing Draught", "heal", 10)
        p.potions = Potion("Healing Draught", "heal",10)
        p.potions = Potion("Ogre Tonic", "buff_str", 2, 3) if p.strength >= p.dexterity else Potion("Cat’s Grace", "buff_dex", 2,3)
        p.weapon = choice(p.get_weapons())
        print(f"🗡️ {p.name} equipaggia: {p.weapon}")

    print("=== INIZIO COMBATTIMENTO ===")

    while p1.is_alive() and p2.is_alive():
        time.sleep(3)
        turno +=1
        print(f"--- Turno {turno} ---")
        players[(turno-1) % 2].should_use_potion(players[turno % 2])
        players[(turno-1) % 2].attack(players[turno % 2])
        p1.tick_buffs()
        p2.tick_buffs()
    if p1.health == p2.health:
        print(f"🤝 Pareggio!")
    else:
        winner = p1 if p1.health > 0 else p2
        print("=== FINE COMBATTIMENTO ===")
        print(f"🏆 {winner.name} vince il combattimento! {winner}")
                



