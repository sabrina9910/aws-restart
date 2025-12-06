from typing import List, Dict


def is_risposta_esatta(scelta: str, risposta_esatta: str) -> bool:
    return scelta.upper() == risposta_esatta


def genera_feedback(is_corretta: bool) -> str:
    return "Hai indovinato!" if is_corretta else "Non hai indovinato."


def valida_scelta(scelta: str) -> bool:
    return scelta.upper() in "ABCD"


def genera_statistiche(risultato_finale: List[Dict[str, str | bool]]) -> Dict[str, int]:
    risposte_esatte = sum(1 for r in risultato_finale if r.get("risposta_corretta"))
    risposte_non_esatte = len(risultato_finale) - risposte_esatte
    return {"risposte_esatte": risposte_esatte, "risposte_non_esatte": risposte_non_esatte}
