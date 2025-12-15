def is_carrello_completo(carrello: list[str], lista_spesa: list[str]) -> bool:
    return len(carrello) < len(lista_spesa)


def get_prodotto_formattato(prodotto: str) -> str:
    if not prodotto:
        print("Il prodotto non deve essere vuoto")
    return prodotto.strip().lower()


def get_input_from_utente(text: str) -> str:
    print("*" * 30)
    return input(text)


def log_message(text: str, type: str):
    icon = None
    match type:
        case "ALERT":
            icon = "⚠️"
        case "INFO":
            icon = "✅"
        case "SUCCESS":
            icon = "🎉"
    print(f"{icon} - {text}")


def main() -> None:
    log_message("Benvenuto nel Supermercato 2050!", "INFO")
    log_message("Carrello robotizzato attivato", "INFO")
    
    lista_spesa: list[str] = ["latte", "pane", "uova", "pasta", "frutta", "verdura"]
    carrello: list[str] = []
    
    print(f"\n📝 Lista della spesa: {lista_spesa}")
    print(f"🛒 Carrello attuale: {carrello}\n")
    
    while is_carrello_completo(carrello, lista_spesa):
        prodotto = get_input_from_utente("Inserisci un prodotto da mettere nel carrello: ")
        
        if not prodotto:
            log_message("Il prodotto non può essere vuoto!", "ALERT")
            continue
        
        prodotto_formattato: str = get_prodotto_formattato(prodotto)
        
        if prodotto_formattato in lista_spesa:
            if prodotto_formattato in carrello:
                log_message("Prodotto già inserito nel carrello!", "ALERT")
            else:
                carrello.append(prodotto_formattato)
                log_message(f"'{prodotto_formattato}' aggiunto al carrello!", "SUCCESS")
                print(f"🛒 Carrello attuale: {carrello}")
                print(f"📊 Progresso: {len(carrello)}/{len(lista_spesa)}")
        else:
            log_message("🤖Prodotto non presente nella lista della spesa", "ALERT")
    
    print("\n" + "*" * 50)
    log_message("Spesa completata! Tutti i prodotti raccolti", "SUCCESS")
    print(f"🛒 Carrello finale: {carrello}")
    print("=" * 50)


main()
