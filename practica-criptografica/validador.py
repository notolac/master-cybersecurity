#!/usr/bin/env python3
import csv
import hashlib
import time
import os
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def generate_hash(password: str) -> str:
    """Genera y retorna el hash SHA-256 de la contraseña."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def search_hash_in_csv(hash_to_find: str, csv_file: str = "passwords.csv") -> str | None:
    """
    Busca en el archivo CSV el hash indicado.
    Retorna la contraseña asociada si se encuentra; de lo contrario, retorna None.
    Si el archivo no existe, se devuelve None.
    """
    try:
        with open(csv_file, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["hash"].lower() == hash_to_find.lower():
                    return row["password"]
    except FileNotFoundError:
        return None
    return None

def append_to_csv(password: str, hash_value: str, csv_file: str = "passwords.csv"):
    """Agrega una nueva fila con la contraseña y su hash al CSV. Si el archivo no existe, lo crea con encabezados."""
    file_exists = os.path.exists(csv_file)
    mode = "a" if file_exists else "w"
    with open(csv_file, mode, newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["password", "hash"])
        writer.writerow([password, hash_value])

def main():
    # Solicitar la contraseña al usuario
    password = Prompt.ask("Ingrese la contraseña para generar su hash")

    # Pantalla de carga fake para la generación del hash (1 segundo)
    with console.status("[bold green]Generando hash...[/bold green]", spinner="dots"):
        time.sleep(1)
        hash_result = generate_hash(password)
    
    console.print(f"[bold blue]Hash SHA-256:[/bold blue] {hash_result}")

    # Pantalla de carga fake para imitar la búsqueda del hash en el CSV (1 segundo)
    with console.status("[bold green]Buscando hash en el archivo CSV...[/bold green]", spinner="dots"):
        time.sleep(1)
        start_time = time.perf_counter()
        password_found = search_hash_in_csv(hash_result, "passwords.csv")
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

    # Mostrar el resultado de la búsqueda
    if password_found:
        console.print(f"[bold green]Hash encontrado![/bold green] La contraseña correspondiente es: [bold yellow]{password_found}[/bold yellow]")
        console.print(f"Tiempo de búsqueda: [bold cyan]{elapsed_time:.6f} segundos[/bold cyan]")
    else:
        console.print("[bold red]Hash no encontrado en el archivo CSV. Se agregará una nueva entrada.[/bold red]")
        append_to_csv(password, hash_result, "passwords.csv")
        console.print("[bold green]Nueva entrada agregada al archivo CSV.[/bold green]")

if __name__ == "__main__":
    main()
