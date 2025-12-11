from typing import Any
from requests import get, exceptions

BASE_URL: str = "https://api.escuelajs.co/api/v1/products"


def get_data(url: str) -> Any:
    if not url:
        raise ValueError("L'URL non può essere vuoto!")

    try:
        response = get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except exceptions.HTTPError as e:
        raise exceptions.HTTPError(f"Errore HTTP: {e.response.status_code}") from e
    except exceptions.ConnectionError:
        raise exceptions.ConnectionError("Errore di connessione, controlla la rete.")
    except exceptions.Timeout:
        raise exceptions.Timeout("La richiesta è andata in timeout.")
    except exceptions.RequestException as e:
        raise exceptions.RequestException(f"Errore di richiesta: {e}") from e
    except ValueError:
        raise ValueError("Risposta non in formato JSON valido.")


def get_all_products() -> list[dict[str, Any]]:
    data = get_data(BASE_URL)
    if not isinstance(data, list):
        raise TypeError("La risposta non è una lista di prodotti.")
    return data


def get_product_by_id(product_id: int) -> dict[str, Any]:
    return get_data(f"{BASE_URL}/{product_id}")