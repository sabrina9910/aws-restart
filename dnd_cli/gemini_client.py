import os
import json
from typing import Dict, Any

from dotenv import load_dotenv
from google import genai

from models import character_schema
from utils import clamp_int

MODEL_NAME = "gemini-2.5-flash"

load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("Devi impostare GEMINI_API_KEY nel file .env")

client = genai.Client(api_key=API_KEY)


def _normalize_character(data: Dict[str, Any]) -> Dict[str, Any]:
    stats = data.get("stats", {}) or {}
    fixed_stats = {
        k: clamp_int(stats.get(k, 10), 3, 18)
        for k in ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
    }

    level = data.get("level", 1)
    try:
        level = int(level)
        if level < 1:
            level = 1
    except Exception:
        level = 1

    return {
        "name": str(data.get("name", "")).strip(),
        "race": str(data.get("race", "")).strip(),
        "class": str(data.get("class", "")).strip(),
        "level": level,
        "stats": fixed_stats,
        "backstory": str(data.get("backstory", "")).strip(),
        "physical_description": str(data.get("physical_description", "")).strip(),
    }


def generate_character_from_prompt(user_prompt: str) -> Dict[str, Any]:
    prompt = (
        "Genera un personaggio Dungeons & Dragons in italiano.\n"
        "Regole:\n"
        "- Compila TUTTI i campi richiesti.\n"
        "- Non lasciare stringhe vuote: se manca un dettaglio, inventalo in modo coerente.\n"
        "- backstory: 600-1200 caratteri.\n"
        "- physical_description: 250-600 caratteri, concreta (aspetto, abiti, segni particolari).\n"
        f"Descrizione utente: {user_prompt}\n"
    )

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config={
                "temperature": 0.7,
                "candidate_count": 1,
                "response_mime_type": "application/json",
                "response_schema": character_schema(),
            },
        )

        text = (response.text or "").strip()
        if not text:
            raise RuntimeError("Risposta vuota dal modello.")

        data = json.loads(text)
        return _normalize_character(data)

    except Exception as e:
        raise RuntimeError(f"Errore Gemini: {e}")


def regenerate_backstory(character: Dict[str, Any]) -> str:
    prompt = (
        "Scrivi SOLO la backstory in italiano (max 1200 caratteri).\n"
        f"Nome: {character.get('name')}\n"
        f"Razza: {character.get('race')}\n"
        f"Classe: {character.get('class')}\n"
        f"Stats: {character.get('stats')}\n"
        f"Descrizione fisica: {character.get('physical_description')}\n"
    )

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config={"temperature": 0.7, "candidate_count": 1},
        )

        text = (response.text or "").strip()
        if not text:
            raise RuntimeError("Gemini non ha generato una backstory valida.")
        return text

    except Exception as e:
        raise RuntimeError(f"Errore Gemini: {e}")
