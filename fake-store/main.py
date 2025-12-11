from services.api import get_all_products, get_product_by_id
from models.product import product_model, print_product, print_products_list


def find_product_by_name(products: list[dict], search_term: str) -> dict | None:
    search_lower = search_term.lower().strip()
    for product in products:
        if search_lower in product["title"].lower():
            return product
    return None


def main() -> None:
    try:
        products = get_all_products()
        print_products_list(products)

        print("\nCome vuoi cercare?")
        print("• Scrivi un NUMERO per ID (es: 1, 42)")
        print("• Scrivi PAROLE per nome (es: laptop, phone)")
        
        search_input = input("Cosa cerchi? ").strip().lower()

        if search_input.isdigit():
            product_id = int(search_input)
            raw_product = get_product_by_id(product_id)
        
        else:
            raw_product = find_product_by_name(products, search_input)
            if not raw_product:
                print(f"Errore'{search_input}' non trovato!")
                return
            
        product = product_model(raw_product)
        print_product(product)


    except Exception as e:
        print(f"Errore: {e}")



if __name__ == "__main__":
    main()