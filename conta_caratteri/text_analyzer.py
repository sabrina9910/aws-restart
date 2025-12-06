"""
Obiettivo: Scrivere un programma modulare che legga un file di testo e restituisca alcune statistiche sui caratteri presenti.
L'esercizio è diviso in step incrementali.
Step 1: La logica di base Create un file chiamato text_analyzer.py.
 Al suo interno, scrivete due funzioni:
conta_caratteri(testo: str) -> int: restituisce il numero totale di caratteri nella stringa (spazi inclusi).
frequenza_caratteri(testo: str) -> dict[str, int]: restituisce un dizionario dove la chiave è il carattere e il valore è il numero di volte che appare nel testo.

Step 2: Integrazione dell'Input/Output Nello stesso file text_analyzer.py (o in un nuovo modulo io_utils.py se preferite separare le responsabilità), aggiungete una funzione per leggere il file:
leggi_file(percorso: str) -> str: accetta il percorso di un file e ne restituisce il contenuto come stringa. Gestite eventuali errori se il file non esiste.

Step 3: Il programma principale Create un file main_analyzer.py. Questo sarà il punto di ingresso del programma.
Importate le funzioni create nello Step 1 e Step 2.

Il programma deve chiedere all'utente il percorso di un file di testo (potete crearne uno di prova, es: prova.txt).
Utilizzando le funzioni importate, il programma deve stampare a video:

Il numero totale di caratteri.
Solo i caratteri che compaiono più di 5 volte (usando il dizionario delle frequenze).
"""


def leggi_file(percorso: str) -> str:
    try:
        with open(percorso, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("Errore: il file non esiste.")
        return ""


def conta_caratteri(testo: str) -> int:
    return len(testo)


def frequenza_caratteri(testo: str) -> dict:
    frequenze = {}
    for c in testo:
        if c in frequenze:
            frequenze[c] += 1
        else:
            frequenze[c] = 1
    return frequenze


def main():
    percorso = input("Percorso del file: ")
    testo = leggi_file(percorso)

    if testo == "":
        return

    print("Caratteri totali:", conta_caratteri(testo))

    freq = frequenza_caratteri(testo)

    print("Caratteri con più di 5 occorrenze:")
    for char, n in freq.items():
        if n > 5:
            print(char, ":", n)


if __name__ == "__main__":
    main()

