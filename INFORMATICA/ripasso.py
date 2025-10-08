#ES.1
sconto = 10
value = float(input("Quanto hai speso? "))

while value <= 0:
    value = float(input("inserisci un valore positivo e > di 0"))

if value > 500:
    sconto = 20

prezzo_scontato = value - ((sconto* value)/100)

print(f"con una spesa di {value}€, viene applicato uno sconto del {sconto}% con un prezzo scontato finale di {prezzo_scontato}€")

    





prezzo_scontato_2 = (value if value <= 300 else 300) - ((10* (value if value <= 300 else 300))/100)
print(prezzo_scontato_2)
if value > 300:
    discount = value - 300
    prezzo_scontato_2 -= ((20 * discount)/100)

print(f"con una spesa di {value}€, viene applicato uno sconto del 10 %  per i primi 300€ e successivamente uno sconto del 20% sulla parte eccedente con un prezzo scontato finale di {prezzo_scontato_2}€")

if prezzo_scontato > prezzo_scontato_2:
    print(f"Se compri nel negozio 1, risparmi {prezzo_scontato_2 - prezzo_scontato}€")

else:
    print(f"Se compri nel negozio 2, risparmi {prezzo_scontato - prezzo_scontato_2}€")