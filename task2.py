import math

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

# b. Calcular Likelihoods con Laplace Smoothing (k=1)

# Calcular totales de palabras en cada categoria
total_palabras_spam = sum(bag_spam.values())
total_palabras_ham = sum(bag_ham.values())
tamaño_vocabulario = len(vocabulario)

print("\nTotal palabras en SPAM:", total_palabras_spam)
print("Total palabras en HAM:", total_palabras_ham)
print("Tamaño del vocabulario |V|:", tamaño_vocabulario)

# Diccionarios para guardar las probabilidades
likelihoods_spam = {}
likelihoods_ham = {}

k = 1  # Constante de Laplace Smoothing

# Calcular P(palabra | Spam) para cada palabra en el vocabulario
for palabra in vocabulario:
    # Si la palabra está en bag_spam, usamos su frecuencia, sino es 0
    count_spam = bag_spam.get(palabra, 0)
    p_palabra_spam = (count_spam + k) / (total_palabras_spam + k * tamaño_vocabulario)
    likelihoods_spam[palabra] = p_palabra_spam

# Calcular P(palabra | Ham) para cada palabra en el vocabulario
for palabra in vocabulario:
    # Si la palabra esta en bag_ham, usamos su frecuencia, sino es 0
    count_ham = bag_ham.get(palabra, 0)
    p_palabra_ham = (count_ham + k) / (total_palabras_ham + k * tamaño_vocabulario)
    likelihoods_ham[palabra] = p_palabra_ham

print("\nLikelihoods P(palabra | Spam):")
for clave, valor in likelihoods_spam.items():
    print(f"\n{clave} | {valor}")

print("\nLikelihoods P(palabra | Ham):")
for clave, valor in likelihoods_ham.items():
    print(f"\n{clave} | {valor}")

# Inferencia (Predicción) a. Cree una función predict(mensaje)

def predict(mensaje):
    # i. Tokenizar el mensaje nuevo (limpiar igual que en entrenamiento)
    mensaje_limpio = clean_text(mensaje)
    palabras = mensaje_limpio.split()
    
    print("\nMensaje a predecir:", mensaje)
    print("Mensaje limpio:", mensaje_limpio)
    print("Palabras:", palabras)
    
    # ii. Calcular log-probabilidades para evitar underflow
    # Inicializar con los priors (en logaritmo)
    log_prob_spam = math.log(p_spam)
    log_prob_ham = math.log(p_ham)
    
    print("\nLog P(Spam) inicial:", log_prob_spam)
    print("Log P(Ham) inicial:", log_prob_ham)
    
    # Para cada palabra del mensaje
    for palabra in palabras:
        # Solo considerar palabras que existen en el vocabulario
        if palabra in vocabulario:
            # Sumar log-probabilidades (equivalente a multiplicar probabilidades)
            log_prob_spam += math.log(likelihoods_spam[palabra])
            log_prob_ham += math.log(likelihoods_ham[palabra])
            
            print(f"\nPalabra '{palabra}' encontrada en vocabulario:")
            print(f"  P({palabra} | Spam) = {likelihoods_spam[palabra]}")
            print(f"  P({palabra} | Ham) = {likelihoods_ham[palabra]}")
        else:
            print(f"\nPalabra '{palabra}' NO está en vocabulario (ignorada)")
    
    # iii. Aplicar regla de Bayes (ya aplicada con logaritmos)
    print("\nLog P(Spam | Mensaje) =", log_prob_spam)
    print("Log P(Ham | Mensaje) =", log_prob_ham)
    
    # iv. Retornar la clase con mayor probabilidad
    if log_prob_spam > log_prob_ham:
        prediccion = "spam"
    else:
        prediccion = "ham"
    
    print("\nPrediccion:", prediccion.upper())
    return prediccion

# Ejemplo de uso:
mensaje_prueba = "Fair enough, anything going on?"
resultado = predict(mensaje_prueba)