def mostra_feedback(messaggio: str) -> None:
    """
    Restituisce il feedback formattato nella maniera desiderata.
    """
    simbol: str = "*" * 30
    print(f"""
{simbol}
{messaggio}
{simbol}
""")


def is_risposta_esatta(scelta: str, risposta_esatta: str) -> bool:
    if scelta.upper() == risposta_esatta:
        return True
    else:
        return False


def genera_feedback(is_corretta: bool) -> str:
    """
    Restituisce il messaggio che indica all'utente se ha indovinato 
    la risposta oppure no. Questa funzione viene eseguita solo se la 
    funzione di validazione restituisce True.
    """
    if is_corretta:
        return "Hai indovinato!"
    else:
        return "Non hai indovinato."


def valida_scelta(scelta: str) -> bool:
    """
    Verifica che la risposta sia una delle opzioni tra A, B, C e D.
    """
    scelta_tmp = scelta.upper()
    if scelta_tmp in "ABCD":
        return True
    else:
        return False


def mostra_domanda(domanda: str) -> None:
    """
    Stampa la domanda e le opzioni di risposta.
    """
    print(domanda)


def raccogli_risposta() -> str:
    """
    Prende l'input dell'utente (la risposta alla domanda).
    """
    return input("Inserisci la tua scelta (A, B, C o D): ")


def leggi_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        content = file.read()
        return content


def estrai_index(content: str) -> int:
    return content.index("£")


def estrai_domanda(content: str, index: int) -> str:
    return content[0:index]


def estrai_risposta(content: str, index: int) -> str:
    return content[index + 1:]


def estrai_lista_domande(file_path: str) -> list[str]:
    lista_domande: list[str] = []
    with open(file_path, "r") as f:
        for i in f:
            lista_domande.append(i.strip())
    return lista_domande


def genera_statistiche(risultato_finale: list[dict[str, str | bool]]) -> dict[str, int]:
    statistica: dict[str, int] = {}

    risposte_esatte: int = 0
    risposte_non_esatte: int = 0

    for i in risultato_finale:
        if i["risposta_corretta"]:
            risposte_esatte += 1
        else:
            risposte_non_esatte += 1

    statistica["risposte_esatte"] = risposte_esatte
    statistica["risposte_non_esatte"] = risposte_non_esatte
    return statistica

def main():
    lista_domande: list[str] = []
    risultato_finale: list[dict[str, str | bool]] = []
    domanda_e_risposta: dict[str, str] = {"domanda": None, "risposta": None}
    lista_domande = estrai_lista_domande("domande.txt")

    counter_domanda_corrente: int = 0
    lista_domande_length: int = len(lista_domande)


    while 0 <= counter_domanda_corrente < lista_domande_length:
        content: str = leggi_file(f"domande_risposte/{lista_domande[counter_domanda_corrente]}")
        index: int = estrai_index(content)
        domanda_e_risposta["domanda"] = estrai_domanda(content, index)
        domanda_e_risposta["risposta"] = estrai_risposta(content, index)

        print(f"Domanda {counter_domanda_corrente + 1} di {lista_domande_length}")
        print("-" * 30)

        mostra_domanda(domanda_e_risposta["domanda"])

        risposta_utente: str = raccogli_risposta()
        is_risposta_valid: bool = valida_scelta(risposta_utente)

        feedback: str = ""

        if is_risposta_valid:
            risultato: dict[str, str | bool] = {}
            is_risposta_corretta: bool = is_risposta_esatta(
                risposta_utente,
                domanda_e_risposta["risposta"]
            )
            feedback = genera_feedback(is_risposta_corretta)

            risultato["domanda"] = lista_domande[counter_domanda_corrente]
            risultato["risposta_corretta"] = is_risposta_corretta
            if len(risultato_finale) > counter_domanda_corrente:
                risultato_finale[counter_domanda_corrente] = risultato
            else:
                risultato_finale.append(risultato)
        else:
            feedback = "Inserisci solo la risposta tra le opzioni elencate (A, B, C o D)."

        mostra_feedback(feedback)
        if not is_risposta_valid:
            continue
        print("Navigazione:")
        print("- Digita 'P' per andare alla domanda precedente")
        print("- Digita 'S' per andare alla domanda successiva")
        print(f"- Oppure digita un numero da 1 a {lista_domande_length} per saltare a quella domanda")
        print("- Premi INVIO (senza scrivere nulla) per TERMINARE il quiz e vedere i risultati")

        scelta_navigazione = input("Scelta: ").strip().upper()
        if scelta_navigazione == "":
            break
        if scelta_navigazione == "P":
            if counter_domanda_corrente > 0:
                counter_domanda_corrente -= 1
            else:
                print("Sei già alla prima domanda, non puoi andare più indietro.")
        elif scelta_navigazione == "S":
            if counter_domanda_corrente < lista_domande_length - 1:
                counter_domanda_corrente += 1
            else:
                print("Sei già all'ultima domanda, non puoi andare oltre.")
        elif scelta_navigazione.isdigit():
            numero = int(scelta_navigazione)
            if 1 <= numero <= lista_domande_length:
                counter_domanda_corrente = numero - 1
            else:
                print(f"Il numero inserito ({numero}) non è tra le domande (1-{lista_domande_length}).")
        else:
            print("Scelta di navigazione non valida. Rimani sulla stessa domanda.")
    print("\n" + "="*50)
    print("RISULTATO FINALE DEL QUIZ")
    print("="*50)
    statistiche: dict[str, int] = genera_statistiche(risultato_finale)
    print(f"Risposte esatte: {statistiche['risposte_esatte']}")
    print(f"Risposte non esatte: {statistiche['risposte_non_esatte']}")
    print(f"Totale domande completate: {len(risultato_finale)}")
    print("="*50)


# Entry point del nostro programma
main()
