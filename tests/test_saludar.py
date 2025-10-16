from app.saludar import saludo


def test_saludo_vacio():
    assert saludo("") == "Hola!"


def test_saludo_nombre():
    assert saludo("Diego") == "Hola, Diego!"
