import random
from colorama import Fore, Style, init

init(autoreset=True)


class Dado:
    def lancia(self):
        return random.randint(1, 6)


def tira_dadi(quanti):
    dado = Dado()
    risultati = []
    for _ in range(quanti):
        risultati.append(dado.lancia())
    return risultati


def combattimento_singolo(dadi_att, dadi_dif):
    att = tira_dadi(dadi_att)
    dif = tira_dadi(dadi_dif)
    att.sort(reverse=True)
    dif.sort(reverse=True)

    print(Fore.RED + "\nLancio attaccante:", att)
    print(Fore.BLUE + "Lancio difensore :", dif)

    confronti = min(len(att), len(dif))
    perse_att = 0
    perse_dif = 0

    for i in range(confronti):
        if att[i] > dif[i]:
            perse_dif += 1
        else:
            perse_att += 1

    print(
        Fore.YELLOW +
        f"Risultato turno -> perde attaccante: {perse_att} | perde difensore: {perse_dif}"
    )

    return perse_att, perse_dif


def clamp(x, minimo, massimo):
    if x < minimo:
        return minimo
    if x > massimo:
        return massimo
    return x


def combattimento_automatico(truppe_att, truppe_dif):
    print(Style.BRIGHT + "\n=== COMBATTIMENTO AUTOMATICO ===")
    print(
        "Truppe iniziali ->",
        Fore.RED + f"Attaccante: {truppe_att}",
        "|",
        Fore.BLUE + f"Difensore: {truppe_dif}"
    )

    turno = 1
    while truppe_dif > 0 and truppe_att > 1:
        dadi_att = clamp(truppe_att - 1, 1, 3)
        dadi_dif = clamp(truppe_dif, 1, 3)

        print(Style.BRIGHT + f"\n--- Turno {turno} ---")
        print(
            "Dadi ->",
            Fore.RED + f"Attaccante: {dadi_att}",
            "|",
            Fore.BLUE + f"Difensore: {dadi_dif}"
        )

        perse_att, perse_dif = combattimento_singolo(dadi_att, dadi_dif)

        truppe_att -= perse_att
        truppe_dif -= perse_dif

        print(
            Fore.RED + f"Truppe attaccante: {truppe_att}",
            "|",
            Fore.BLUE + f"Truppe difensore: {truppe_dif}"
        )

        turno += 1

    print(Style.BRIGHT + "\n=== FINE COMBATTIMENTO ===")
    if truppe_dif == 0:
        print(Fore.GREEN + "VITTORIA ATTACCANTE (difensore senza truppe)")
    else:
        print(Fore.CYAN + "VITTORIA DIFENSORE (attaccante con una sola armata)")



if __name__ == "__main__":
    print(Style.BRIGHT + "RISIKO - Simulazione lancio dadi")

    scelta = input("1) Combattimento singolo  2) Combattimento automatico : ")

    if scelta == "1":
        a = int(input("Quante truppe attaccano? (1-3): "))
        d = int(input("Quante truppe difendono? (1-3): "))

        a = clamp(a, 1, 3)
        d = clamp(d, 1, 3)

        combattimento_singolo(a, d)

    else:
        tr_att = int(input("Truppe TOTALI attaccante: "))
        tr_dif = int(input("Truppe TOTALI difensore : "))

        combattimento_automatico(tr_att, tr_dif)