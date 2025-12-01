'''
Funzioni da creare
mostra_menu() (senza return)
Non prende parametri
Stampa la domanda e le 4 opzioni
Non restituisce nulla

raccogli_risposta() (con return)
Non prende parametri
Chiede l'input all'utente
Restituisce la scelta 

valida_scelta(scelta) (con return)
prende come parametro il numero scelto
Verifica se è tra A B C D usando if
Restituisce True se valida, False altrimenti

'''



def mostra_domanda() -> None:
    """
    questa funzione restituisce la domanda e le opzioni della risposta
    """
    print(
    """
    Chi parteciperà a sanremo 2026?   
    A. Nayt
    B. La Nina
    C. Nilla Pizzi 
    D. Rocco Papaleo
    """
    )

def raccogli_risposta() -> str:
    """
    Questa funziona si occupa solamente di prendere l'input dell'utente 
    il cotnrollo di tale valore avverrà attraverso una funzione dedicata"
    """
    return input("Inserisci la tua scelta: ")
mostra_domanda()


def valida_scelta(scelta:str) -> bool:
    """ 
    Questa funzione prende un valore di tipo stringa e verifica che la risposta sia una delle opzioni tra a b c d
    se la stringa è vuota o non una di quelle sopra elencate restitutisce False 
    """
    scelta_tmp = scelta.upper()
    if scelta_tmp == "A" or scelta_tmp == "B" or scelta_tmp ==  "C" or scelta_tmp == "D":

        return True
    else:
        return False 

risposta_da_validare: str = raccogli_risposta()
risposta_validata: bool = valida_scelta(risposta_da_validare)

print(risposta_validata)