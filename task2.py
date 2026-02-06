print("Task 2: Filtro de Spam Bayesiano")

def data(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

contenido = data('entrenamiento.txt')
#print(contenido.lower())

def get_symbols(texto):
    symbols = []
    for char in texto:
        # Si NO es letra y NO es espacio (y no lo hemos guardado ya)
        if not char.isalpha() and not char.isspace() and char not in symbols:
            symbols.append(char)
    return symbols

simbolos = get_symbols(contenido)
print(simbolos)

def clean_text(texto):
    for simbolo in get_symbols(texto):
        texto = texto.replace(simbolo, "")
    return texto.lower()

print(clean_text(contenido))
