from quizzettone.data.repository import (
    leggi_file,
    estrai_index,
    estrai_domanda,
    estrai_risposta,
    estrai_lista_domande,
)
from quizzettone.data.services import (
    is_risposta_esatta,
    genera_feedback,
    valida_scelta,
    genera_statistiche,
)
from quizzettone.ui.console import mostra_feedback, mostra_domanda, raccogli_risposta


def main():
    lista_domande = estrai_lista_domande("domande.txt")
    risultato_finale: list[dict[str, str | bool]] = []
    domanda_e_risposta: dict[str, str] = {"domanda": None, "risposta": None}

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
                domanda_e_risposta["risposta"],
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

    print("\n" + "=" * 50)
    print("RISULTATO FINALE DEL QUIZ")
    print("=" * 50)
    statistiche: dict[str, int] = genera_statistiche(risultato_finale)
    print(f"Risposte esatte: {statistiche['risposte_esatte']}")
    print(f"Risposte non esatte: {statistiche['risposte_non_esatte']}")
    print(f"Totale domande completate: {len(risultato_finale)}")
    print("=" * 50)


if __name__ == "__main__":
    main()
