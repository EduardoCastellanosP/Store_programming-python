import json
import os
from typing import Dict, List, Optional

def read_json(file_path):
    """Lee un archivo JSON y maneja errores si el archivo está vacío o malformado."""
    if not os.path.exists(file_path):  # Si el archivo no existe, retorna un diccionario vacío
        return {}

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().strip()  # Leer el contenido y eliminar espacios en blanco
            if not content:  # Si el archivo está vacío, retorna un diccionario vacío
                return {}

            return json.loads(content)  # Cargar los datos JSON
    except (json.JSONDecodeError, FileNotFoundError):
        return {}  # Si hay un error, retorna un diccionario vacío


def write_json(file_path: str, data: Dict) -> None:
    """Escribe un diccionario en un archivo JSON, creando la carpeta si no existe."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Crea la carpeta si no existe

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def update_json(file_path, data, keys):
    # Verifica si el archivo existe; si no, lo crea con un JSON vacío
    if not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Crea la carpeta si no existe
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump({}, file)  # Archivo vacío con estructura JSON válida

    # Ahora abre y actualiza el archivo
    with open(file_path, "r+", encoding="utf-8") as file:
        contenido = json.load(file)
        for key in keys:
            if key not in contenido:
                contenido[key] = []  # Se asegura de que la clave exista en el JSON
        contenido[keys[0]].append(data)  # Agrega los nuevos datos
        file.seek(0)
        json.dump(contenido, file, indent=4, ensure_ascii=False)


def delete_json(file_path: str, path: List[str]) -> bool:
    """
    Elimina datos en la ruta especificada
    Retorna True si se eliminó exitosamente
    """
    data = read_json(file_path)
    current = data

    for key in path[:-1]:
        if key not in current:
            return False
        current = current[key]

    if path and path[-1] in current:
        del current[path[-1]]
        write_json(file_path, data)
        return True
    return False

def initialize_json(file_path: str, initial_structure: Dict) -> None:
    """
    Inicializa el archivo con una estructura base si no existe
    """
    if not os.path.isfile(file_path):
        write_json(file_path, initial_structure)
    else:
        current_data = read_json(file_path)
        for key, value in initial_structure.items():
            if key not in current_data:
                current_data[key] = value
        write_json(file_path, current_data)

# corefiles.py (al final del arch