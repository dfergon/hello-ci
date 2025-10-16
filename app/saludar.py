def saludo(nombre: str) -> str:
    nombre = (nombre or "").strip()
    return f"Hola, {nombre}!" if nombre else "Hola!"


if __name__ == "__main__":
    print(saludo("Mundo"))
