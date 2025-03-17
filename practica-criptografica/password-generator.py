#!/usr/bin/env python3
import csv
import hashlib

def generate_variants(base_password: str) -> set[str]:
    """
    Genera variantes de una contraseña base aplicando transformaciones:
      - Versión original, con la primera letra en mayúscula y en mayúsculas.
      - Combinaciones de prefijos y sufijos numéricos.
      - Se añade, opcionalmente, un símbolo especial al final.
    """
    variants: set[str] = set()
    transformations = [
        base_password,
        base_password.capitalize(),
        base_password.upper()
    ]
    prefix_options = [""] + [str(i) for i in range(10)]
    suffix_options = [""] + [str(i) for i in range(10)]
    # Lista de símbolos especiales para agregar (excluimos el valor vacío en este paso)
    special_options = ["!", "@", "#", "$", "%", "&"]

    for transform in transformations:
        for prefix in prefix_options:
            for suffix in suffix_options:
                base_variant = prefix + transform + suffix
                # Agregamos la variante sin símbolo
                variants.add(base_variant)
                # Agregamos variantes con cada símbolo especial al final
                for symbol in special_options:
                    variants.add(base_variant + symbol)
    return variants

def main():
    # Lista de contraseñas comunes (puede ampliarse o modificarse)
    base_passwords = [
        "123456", "password", "12345678", "qwerty", "abc123",
        "123456789", "111111", "1234567", "sunshine", "qwerty123",
        "iloveyou", "admin", "welcome", "666666", "1q2w3e4r",
        "password1", "123123", "qwertyuiop", "123321", "password123",
        "1qaz2wsx", "654321", "123", "987654321", "qwe123",
        "zxcvbnm", "asdfgh", "1234", "qazwsx", "trustno1",
        "dragon", "letmein", "monkey", "football", "whatever",
        "shadow", "baseball", "superman", "696969", "michael",
        "ashley", "hunter", "biteme", "jordan", "mustang",
        "jennifer", "2000", "blahblah", "harley", "michelle",
        "cookie", "pepper", "snoopy", "samantha", "summer",
        "princess", "butterfly", "tigger", "angels", "justin",
        "batman", "nicole", "hunter2", "jackson", "ginger",
        "heather", "thomas", "jessica", "welcome1", "cheese",
        "cheeseburger", "hannah", "taylor", "charlie", "william",
        "bailey", "jasmine", "scooter", "george", "andrew",
        "buster", "busterbrown", "soccer", "bandit", "qwert",
        "matrix", "passw0rd", "yankees", "lakers", "joshua",
        "maggie", "peppermint", "gingerbread", "chocolate", "mercedes",
        "flower", "diamond", "turtle", "shelby", "maverick",
        "starwars", "nintendo", "pokemon", "iloveme", "spongebob"
    ]
    
    all_variants: set[str] = set()
    # Se generan variantes a partir de cada contraseña base
    for bp in base_passwords:
        variants = generate_variants(bp)
        all_variants.update(variants)
        # Si ya se supera el límite deseado, se detiene la generación
        if len(all_variants) >= 10000:
            break
    
    # Seleccionamos las primeras 10,000 variantes
    password_list = list(all_variants)[:10000]
    
    # Se crea y escribe el archivo CSV con dos columnas: password y hash
    with open("passwords.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["password", "hash"])  # Encabezados
        for pwd in password_list:
            hash_hex = hashlib.sha256(pwd.encode("utf-8")).hexdigest()
            writer.writerow([pwd, hash_hex])
    
    print(f"Se han generado y cifrado {len(password_list)} contraseñas. Archivo 'passwords.csv' creado.")

if __name__ == "__main__":
    main()
