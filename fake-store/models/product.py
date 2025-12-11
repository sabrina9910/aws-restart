from typing import Any


def product_model(product: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": product["id"],
        "title": product["title"],
        "price": product["price"],
        "category": product["category"]["name"],
        "description": product["description"],
    }
def print_product(product: dict[str, Any]) -> None:
    print("*" * 30)
    print("PRODOTTO")
    print("*" * 30)
    print(f"ID: {product['id']}")
    print(f"TITOLO: {product['title']}")
    print(f"CATEGORIA: {product['category']}")
    print(f"PREZZO: {product['price']}")
    print(f"DESCRIZIONE: {product['description']}")


def print_products_list(products: list[dict[str, Any]]) -> None:
    print("\nLISTA PRODOTTI (ID - Titolo)")
    print("-" * 40)
    for p in products:
        print(f"{p['id']} - {p['title']}")
