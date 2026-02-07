print("Task 2: Filtro de Spam Bayesiano")

def data(path):
    with open(path, 'r', encoding='utf-8') as file:
        print("\nArchivo cargado: ", path)
        return file.read()

#contenido = data('testdata.txt')
contenido = data('entrenamiento.txt')

def get_symbols(texto):
    symbols = []
    for char in texto:
        if not char.isalpha() and not char.isspace() and char not in symbols:
            symbols.append(char)
    return symbols

def clean_text(texto):
    symbols = get_symbols(texto)
    for simbolo in symbols:
        texto = texto.replace(simbolo, "")
    return texto.lower()

lineas = contenido.strip().split('\n')

dic = {
    "ham": [],
    "spam": []
}

for linea in lineas:
    partes = linea.split('\t')
    if len(partes) == 2:
        etiqueta = partes[0].strip().lower()
        mensaje_original = partes[1].strip()
        
        # Limpiar el mensaje
        mensaje_limpio = clean_text(mensaje_original)
        
        # Agregar a la categoría correspondiente
        if etiqueta in dic:
            dic[etiqueta].append(mensaje_limpio)

print("\nDiccionario:", dic)

# Crear vocabulario SOLO de las palabras de los mensajes
todas_las_palabras = []
for mensajes in dic.values():
    for mensaje in mensajes:
        todas_las_palabras.extend(mensaje.split())

# Vocabulario sin duplicados
vocabulario = sorted(list(set(todas_las_palabras)))

print("\nVocabulario:", vocabulario)

# Bag of Words: Diccionarios con palabra:frecuencia
bag_spam = {}
bag_ham = {}

# Contar palabras en SPAM
for mensaje in dic['spam']:
    for palabra in mensaje.split():
        if palabra in bag_spam:
            bag_spam[palabra] += 1
        else:
            bag_spam[palabra] = 1

# Contar palabras en HAM
for mensaje in dic['ham']:
    for palabra in mensaje.split():
        if palabra in bag_ham:
            bag_ham[palabra] += 1
        else:
            bag_ham[palabra] = 1

print("\nBag of Words SPAM:", bag_spam)
print("\nBag of Words HAM:", bag_ham)

# a. Calcule las probabilidades a priori (Priors): P(Spam) y P(Ham)

total_mensajes = len(dic['spam']) + len(dic['ham'])
num_spam = len(dic['spam'])
num_ham = len(dic['ham'])

p_spam = num_spam / total_mensajes
p_ham = num_ham / total_mensajes

print("\nProbabilidades a Priori:")
print("P(Spam) =", num_spam, "/", total_mensajes, "=", p_spam)
print("P(Ham) =", num_ham, "/", total_mensajes, "=", p_ham)