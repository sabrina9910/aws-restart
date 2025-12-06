"""Obiettivo: Creare dizionari e accedere ai valori.
Consegna:
Creare un dizionario config con le seguenti coppie:
"host": "192.168.1.1"
"port": 8080
"ssl": True
"timeout": 30
Stampare il valore di "host"
Modificare "port" in 443
Aggiungere una nuova chiave "protocol" con valore "https"
Stampare il dizionario completo

Output Atteso:
Host: 192.168.1.1
{'host': '192.168.1.1', 'port': 443, 'ssl': True, 'timeout': 30, 'protocol': 'https'}

"""
# 1. Creare il dizionario config
config = {
    "host": "192.168.1.1",
    "port": 8080,
    "ssl": True,
    "timeout": 30
}

# 2. Stampare il valore di "host"
print("Host:", config["host"])

# 3. Modificare "port" in 443
config["port"] = 443

# 4. Aggiungere una nuova chiave "protocol"
config["protocol"] = "https"

# 5. Stampare il dizionario completo
print("Config completo:", config)
