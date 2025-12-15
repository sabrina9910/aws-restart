def is_lista_utente_filled(lista_utente:list[str] ) -> bool:
    if len(lista_utente) < 3:
        return True
    else:
        False

def get_ingrediente_formattato(ingrediente: str) -> str:
    if not ingrediente:
        print("l'ingrediente non deve essere vuoto")

    return ingrediente.strip().lower()

def get_input_from_utente(text: str) -> str:
    if not text:
        print("Il messaggio non deve essere vuoto")
    print("*" * 30)    
    return input (text)

def log_message(text: str, type: str):
    icon = None
    match type:
        case "ALERT":
            icon = "⚠️"
        case "INFO":
            icon = "✅"
    print(f"{icon} - {text}")

def main() -> None:
    log_message("Start del programma", "INFO")

    lista_ricetta: list[str] = ["farina", "acqua", "lievito"]
    lista_utente: list[str] = []

    while is_lista_utente_filled(lista_utente):
        ingrediente = get_input_from_utente("inserisci un ingrediente:")
        if not ingrediente:
            log_message("l'ingrediente non può essere vuoto", "ALERT")

        ingrediente_formattato: str = get_ingrediente_formattato(ingrediente)

        if ingrediente_formattato in lista_ricetta:
        
            if ingrediente_formattato in lista_utente:
                print("Ingrediente già inserito")
            else:
                lista_utente.append(ingrediente_formattato)
                print(lista_utente)

        else:
            log_message("inrediente non valdio", "ALERT")
        
    print("impasta e fai la pizza")
    print("end del programma")

main()