"""
Esercizio 3.1: Lista di Dizionari
File: lista_dizionari.py
Obiettivo: Gestire una lista di dizionari (simile a un database).
Consegna:
Creare una lista prodotti contenente 4 dizionari, ognuno con chiavi "nome", "prezzo", "quantita":
{"nome": "Laptop", "prezzo": 899.99, "quantita": 5}
{"nome": "Mouse", "prezzo": 25.50, "quantita": 50}
{"nome": "Tastiera", "prezzo": 75.00, "quantita": 30}
{"nome": "Monitor", "prezzo": 299.99, "quantita": 15}
Iterare sulla lista e stampare solo i prodotti con prezzo superiore a 100
Calcolare il valore totale dell'inventario (prezzo × quantità per ogni prodotto)

Output Atteso:
Prodotti > 100€:
- Laptop: €899.99
- Monitor: €299.99

Valore totale inventario: €11224.20
"""
lista_prodotti = [
    {"nome": "Laptop", "prezzo": 899.99, "quantita": 5},
    {"nome": "Mouse", "prezzo": 25.50, "quantita": 50},
    {"nome": "Tastiera", "prezzo": 75.00, "quantita": 30},
    {"nome": "Monitor", "prezzo": 299.99, "quantita": 15}
]

for prodotto in lista_prodotti:
    if prodotto["prezzo"] > 100:
        print(f"- {prodotto['nome']} ({prodotto['prezzo']} €)")

valore_totale = sum(prodotto["prezzo"] * prodotto["quantita"] for prodotto in lista_prodotti)

print("\nValore totale dell'inventario:", valore_totale, "€")