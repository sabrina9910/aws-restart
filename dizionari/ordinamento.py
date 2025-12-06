"""Obiettivo: Ordinare liste e verificare esistenza elementi.
Consegna:
Creare una lista prezzi contenente: [45.5, 12.0, 78.3, 23.1, 56.7]
Creare una copia ordinata della lista (usando sorted())
Trovare il prezzo minimo e massimo
Verificare se 23.1 è nella lista
Contare quanti prezzi sono maggiori di 50

Output Atteso:
Prezzi originali: [45.5, 12.0, 78.3, 23.1, 56.7]
Prezzi ordinati: [12.0, 23.1, 45.5, 56.7, 78.3]
Minimo: 12.0
Massimo: 78.3
23.1 presente: True
Prezzi > 50: 2
"""

prezzi = [45.5, 12.0, 78.3, 23.1, 56.7]
prezzi_ordinati = sorted(prezzi)
prezzo_min = min
prezzo_max = max 
presente = 23.1 in prezzi
maggiori_50 = sum(1 for p in prezzi if p > 50)

print("Prezzi originali",prezzi)
print("Prezzi ordinati",prezzi_ordinati)
print("Prezzo minimo:", min(prezzi))
print("Prezzo massimo:", max(prezzi))
print("23.1 è presente?",presente)
print("Quanti prezzi sono maggiori di 50?",maggiori_50)