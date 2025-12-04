#!/usr/bin/env python3
"""Entry point that loads `strutture-dati.py` by path and prints its `stringhe` variable.

This uses `runpy.run_path` because the filename contains a hyphen and cannot be imported
with a normal module import.
"""
from pathlib import Path
import runpy
import sys


def main() -> int:
    base = Path(__file__).resolve().parent
    target = base / "strutture-dati.py"
    if not target.exists():
        print(f"File non trovato: {target}")
        return 1

    try:
        ns = runpy.run_path(str(target))
    except Exception as e:
        print(f"Errore eseguendo {target}: {e}")
        return 2

    stringhe = ns.get("stringhe")
    print("Valore di 'stringhe' in strutture-dati.py:")
    print(stringhe)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
