from player import Player
from potion import Potion
from random import randint, choice


if __name__ == "__main__" :
    p1 = Player("Name1", 100, randint(1, 20), randint(1, 20))
    p2 = Player("Name2", 100, randint(1, 20), randint(1, 20))
    turno = 0
    players = [p1, p2]

    print("=== SIMULAZIONE COMBATTIMENTO ===")

    for p in players:
        print(f"{p.name}: Forza={p.strength}, Destrezza={p.dexterity}")

        try:
            p.potions = Potion("Healing Draught", "heal", 10)
            p.potions = Potion("Healing Draught", "heal", 10)
            p.potions = (
                Potion("Ogre Tonic", "buff_str", 2, 3)
                if p.strength >= p.dexterity
                else Potion("Cat’s Grace", "buff_dex", 2, 3)
            )
        except (TypeError, ValueError) as e:
            raise RuntimeError(f"Errore durante l'assegnazione delle pozioni a {p.name}: {e}")

        weapons = p.get_weapons()
        if not weapons:
            raise RuntimeError(f"Nessuna arma disponibile per {p.name}. Controlla weapon.json e le stats.")
        
        try:
            p.weapon = choice(weapons)
        except IndexError:
            raise RuntimeError(f"Impossibile scegliere un'arma per {p.name}: lista vuota.")
        
        print(f"🗡️ {p.name} equipaggia: {p.weapon}")

    print("=== INIZIO COMBATTIMENTO ===")

    while p1.is_alive() and p2.is_alive():
        turno += 1
        print(f"--- Turno {turno} ---")

        attaccante = players[(turno - 1) % 2]
        difensore = players[turno % 2]
        attaccante.should_use_potion(difensore)
        attaccante.attack(difensore)
        
        p1.tick_buffs()
        p2.tick_buffs()

    if p1.health == p2.health:
        print(f"🤝 Pareggio!")
    else:
        winner = p1 if p1.health > 0 else p2
        print("=== FINE COMBATTIMENTO ===")
        print(f"🏆 {winner.name} vince il combattimento! {winner}")
