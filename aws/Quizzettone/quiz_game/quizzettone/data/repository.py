from pathlib import Path
from typing import List


def _package_root() -> Path:
    # quizzettone/data -> parent is quizzettone
    return Path(__file__).resolve().parent.parent


def leggi_file(file_path: str) -> str:
    p = _package_root() / file_path
    with open(p, "r", encoding="utf-8") as f:
        return f.read()


def estrai_index(content: str) -> int:
    return content.index("£")


def estrai_domanda(content: str, index: int) -> str:
    return content[0:index]


def estrai_risposta(content: str, index: int) -> str:
    return content[index + 1:]


def estrai_lista_domande(file_path: str) -> List[str]:
    lista_domande: List[str] = []
    p = _package_root() / file_path
    with open(p, "r", encoding="utf-8") as f:
        for line in f:
            lista_domande.append(line.strip())
    return lista_domande
