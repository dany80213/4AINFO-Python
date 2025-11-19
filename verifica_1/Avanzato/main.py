import json
from marsmap import MarsMap
from rover import Rover
from Exceptions import InvalidCommandError,RoverCollisionError,SampleNotFound
# Assicurati di importare le tue classi qui

if __name__ == "__main__":
    
    # Elenco dei file di livello da eseguire
    levels_to_run = [
        "livello_1.json",
        "livello_2.json",
        "livello_3.json",
        "livello_4.json",
        "livello_5.json",
        "livello_6.json"
    ]

    print("=== AVVIO SIMULATORE ROVER MARZIANO ===")

    for level_file in levels_to_run:
        print(f"\n--- Processo Livello: {level_file} ---")
        
        # Variabile placeholder per i dati
        data = {}
        
        try:
            
            # --- 1. LETTURA FILE ---
            #       'level_file' in lettura e caricare 
            #       i dati JSON nella variabile 'data'.
            
            with open(level_file, "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            print(f"ERRORE: File '{level_file}' non trovato.")
            continue

        
        # --- 2. SIMULAZIONE (da non modificare) ---
        # Questa parte funzionerà solo se hai
        # completato il 'pass' precedente e caricato 'data'.
        
        try:
            print(f"Caricamento: {data['level_name']}")

            # Creazione Mappa
            map_size = data["map_size"]
            map_1 = MarsMap(map_size[0], map_size[1])

            # Popolamento Mappa
            for obs in data["obstacles"]:
                map_1.add_obstacle(obs[0], obs[1])
            for s in data["samples"]:
                map_1.add_sample(s[0], s[1])

            # Creazione Rover
            rover_start = data["rover_start"]
            rover_1 = Rover(rover_start["x"], rover_start["y"], rover_start["dir"], map_1)
            print(f"Rover creato a ({rover_1.x}, {rover_1.y}) dir: {rover_1.direction}")

            # Esecuzione Comandi
            commands = data["commands"]
            print(f"Esecuzione: {commands}")
            
            # La funzione 'execute_commands' gestirà internamente
            # la stampa degli errori (Collision, InvalidCommand)
            success = rover_1.execute_commands(commands)
            
            # Risultato
            print(f"Esito finale: {success}")
            print(f"Posizione finale: ({rover_1.x}, {rover_1.y}) dir: {rover_1.direction}")
        
        except KeyError as e:
            print(f"ERRORE: Dati mancanti nel file JSON (chiave non trovata: {e}).")
            
        except SampleNotFound as  e:
            print(f"Errore {e} ")
        except InvalidCommandError as e:
            print(f"Errore {e} ")
        except RoverCollisionError as e :
            print(f"Errore {e} ")
        except ValueError as e:
            print(f"Errore {e} ")
        except TypeError as e:
            print(f"Errore {e} ")
        except Exception as e:
            print(f"Errore {e} ")
            
            print(f"ERRORE durante l'esecuzione del livello: {e}")


    print("\n=== SIMULAZIONE COMPLETATA ===")