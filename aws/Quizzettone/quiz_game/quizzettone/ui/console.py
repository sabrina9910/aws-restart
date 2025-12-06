def mostra_feedback(messaggio: str) -> None:
    simbol: str = "*" * 30
    print(f"""
{simbol}
{messaggio}
{simbol}
""")


def mostra_domanda(domanda: str) -> None:
    print(domanda)


def raccogli_risposta() -> str:
    return input("Inserisci la tua scelta (A, B, C o D): ")
