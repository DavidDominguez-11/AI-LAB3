print("Task 2: Filtro de Spam Bayesiano")

def data(path):
    with open(path, 'r', encoding='utf-8') as file:
        print("\nArchivo cargado: ", path)
        return file.read()

contenido = data('testdata.txt')
#print(contenido.lower())

def get_symbols(texto):
    symbols = []
    for char in texto:
        # Si NO es letra y NO es espacio (y no lo hemos guardado ya)
        if not char.isalpha() and not char.isspace() and char not in symbols:
            symbols.append(char)
    print("\nSimbolos extraidos: ", symbols)
    return symbols

#simbolos = get_symbols(contenido)
#print(simbolos)

def clean_text(texto):
    for simbolo in get_symbols(texto):
        texto = texto.replace(simbolo, "")
    print("\nTexto limpio: ", texto)
    return texto.lower()

#print(clean_text(contenido))

text = clean_text(contenido)

palabras = text.split()
vocabulario = list()

for i in palabras:
    if i not in vocabulario or i == 'spam' or i == 'ham':
        vocabulario.append(i)

print("\nVocabulario: ", vocabulario)


# dic de ham y spam
dic = {
    "ham": [],
    "spam": []
}


categoria_actual = None
frase_temporal = []

for palabra in vocabulario:
    if palabra == "ham" or palabra == "spam":
        # Si ya teníamos una categoría y palabras guardadas, las unimos y guardamos
        if categoria_actual and frase_temporal:
            dic[categoria_actual].append(" ".join(frase_temporal))
        
        # Actualizamos a la nueva categoría y reseteamos la frase temporal
        categoria_actual = palabra
        frase_temporal = []
    else:
        # Si no es etiqueta, es parte del mensaje
        frase_temporal.append(palabra)

# Al terminar el bucle, guardamos la última frase pendiente
if categoria_actual and frase_temporal:
    dic[categoria_actual].append(" ".join(frase_temporal))

print("\nDiccionario: ", dic)



