#!/usr/bin/env python3
import sys
import os

# Aggiungi la cartella quiz_game al PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'quiz_game'))

# Importa e avvia il main
from quizzettone.main import main

if __name__ == "__main__":
    main()
