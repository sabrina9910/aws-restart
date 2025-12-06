"""Obiettivo: Usare dizionari per contare occorrenze.
Consegna:
Creare una lista voti contenente: ["A", "B", "A", "C", "B", "A", "D", "B", "C", "A"]
Creare un dizionario vuoto conteggio
Iterare sulla lista voti e contare quante volte appare ogni voto nel dizionario
Stampare il dizionario finale
Suggerimento: Usare conteggio.get(voto, 0) per gestire chiavi mancanti.

Output Atteso:
Conteggio voti: {'A': 4, 'B': 3, 'C': 2, 'D': 1}


"""

voti = ["A", "B", "A", "C", "B", "A", "D", "B", "C", "A"]
conteggio = dict()
for voto in voti:
    conteggio[voto] = conteggio.get(voto, 0) + 1
print(conteggio)