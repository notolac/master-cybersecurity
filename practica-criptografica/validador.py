#!/usr/bin/env python3
import argparse
import csv
import hashlib
import re
import time
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def generate_hash(password: str) -> str:
    """Genera y retorna el hash SHA-256 de una contraseña."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def is_valid_sha256(hash_str: str) -> bool:
    """Valida que el hash tenga 64 caracteres hexadecimales."""
    return bool(re.fullmatch(r"[a-fA-F0-9]{64}", hash_str))

def search_hash_in_csv(hash_to_find: str, csv_file: str = "passwords.csv") -> str | None:
    """
    Busca en el archivo CSV el hash indicado.
    Retorna la contraseña asociada si se encuentra; de lo contrario, retorna None.
    """
    with open(csv_file, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["hash"].lower() == hash_to_find.lower():
                return row["password"]
    return None

def main():
    parser = argparse.ArgumentParser(
        description="Interfaz para generación y comparación de hashes SHA-256."
    )
    # Se pueden agregar argumentos adicionales en el futuro
    args = parser.parse_args()
    
    console.print("[bold green]Bienvenido a la interfaz de hashes SHA-256[/bold green]")
    console.print("Seleccione una opción:")
    console.print("1) Generar Hash")
    console.print("2) Comparador de Hash")
    
    option = Prompt.ask("Ingrese la opción (1 o 2)", choices=["1", "2"])
    
    if option == "1":
        password = Prompt.ask("Ingrese la contraseña para generar su hash")
        hash_result = generate_hash(password)
        console.print(f"[bold blue]Hash SHA-256:[/bold blue] {hash_result}")
    
    elif option == "2":
        hash_input = Prompt.ask("Ingrese el hash SHA-256 a buscar")
        if not is_valid_sha256(hash_input):
            console.print("[bold red]El hash ingresado no es válido. Asegúrese de que tenga 64 caracteres hexadecimales.[/bold red]")
            return
        console.print("Buscando el hash en el archivo CSV...")
        start_time = time.perf_counter()
        password_found = search_hash_in_csv(hash_input, "passwords.csv")
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        if password_found:
            console.print(f"[bold green]Hash encontrado![/bold green] La contraseña correspondiente es: [bold yellow]{password_found}[/bold yellow]")
            console.print(f"Tiempo de búsqueda: [bold cyan]{elapsed_time:.6f} segundos[/bold cyan]")
        else:
            console.print("[bold red]Hash no encontrado en el archivo CSV.[/bold red]")

if __name__ == "__main__":
    main()
