"""
Docstring for iterazione
Obiettivo: Iterare su dizionari.
Consegna:
Creare un dizionario utenti con le seguenti coppie:
"alice": "admin"
"bob": "user"
"charlie": "guest"
Iterare sul dizionario e stampare ogni coppia nel formato: "Username: alice, Ruolo: admin"
Verificare se "bob" è una chiave presente
Stampare tutte le chiavi (usernames)
Stampare tutti i valori (ruoli)

Output Atteso:
Username: alice, Ruolo: admin
Username: bob, Ruolo: user
Username: charlie, Ruolo: guest
bob presente: True
Usernames: dict_keys(['alice', 'bob', 'charlie'])
Ruoli: dict_values(['admin', 'user', 'guest'])
"""

utenti = {
    "alice": "admin",
    "bob": "user",
    "charlie": "guest"
}

for username, ruolo in utenti.items():
    print(f"Username: {username}, Ruolo: {ruolo}")
    print("bob è presente?", "bob" in utenti)
    print("Tutte le chiavi:", list(utenti.keys()))
    print("Tutti i ruoli:", list(utenti.values()))