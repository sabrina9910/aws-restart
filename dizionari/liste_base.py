"""
Obiettivo: Familiarizzare con i metodi base delle liste.

Consegna:
Creare una lista server contenente: ["web01", "db01", "cache01"]
Aggiungere "backup01" alla fine
Inserire "proxy01" all'inizio (indice 0)
Rimuovere "cache01"
Stampare la lista finale e la sua lunghezza

Output Atteso:
['proxy01', 'web01', 'db01', 'backup01']
Numero server: 4
"""

# Creare la lista iniziale
server = ["web01", "db01", "cache01"]

# Aggiungere "backup01" alla fine
server.append("backup01")

# Inserire "proxy01" all'inizio
server.insert(0, "proxy01")

# Rimuovere "cache01"
server.remove("cache01")

# Stampare lista finale e lunghezza
print(server)
print("Numero server:", len(server))
