def leggi_file(percorso: str) -> str:
    try:
        f = open(percorso, "r", encoding="utf-8")
        contenuto = f.read()
        f.close()
        return contenuto
    except FileNotFoundError:
        print("Il file non esiste!")
    return ""