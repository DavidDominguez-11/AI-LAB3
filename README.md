# Laboratorio 3 – Task 2 y Task 3  

## Task 2 – Filtro de Spam Bayesiano

### Objetivo
Implementar **desde cero** un clasificador de texto usando **Naive Bayes**, reforzando el entendimiento del modelo probabilístico y sus supuestos.

### Descripción
Se construyó un filtro de spam utilizando el enfoque **Bag of Words**, calculando explícitamente:
- Probabilidades a priori (Spam / Ham)
- Likelihoods con **Laplace Smoothing (k = 1)**
- Inferencia mediante la regla de Bayes (usando log-probabilidades)

El modelo clasifica mensajes como *Spam* o *Ham* sin utilizar librerías de machine learning.

### Pasos principales
- Limpieza y tokenización del texto
- Construcción del vocabulario
- Cálculo de probabilidades
- Predicción de mensajes nuevos
- Evaluación con **Accuracy** y **Matriz de Confusión**

### Aprendizajes clave
- La independencia condicional es una **aproximación**, no una verdad absoluta.
- Laplace Smoothing evita probabilidades cero.
- Naive Bayes es simple, eficiente y sorprendentemente efectivo para texto.

---

## Task 3 – SVM y Árboles de Decisión (League of Legends)

### Objetivo
Aplicar **SVM** y **Árboles de Decisión** a un dataset real de e-sports, analizando el compromiso entre **precisión** e **interpretabilidad**.

### Dataset
- **League of Legends Diamond Ranked Games (10 min)**
- Variable objetivo: `blueWins`
- Fuente: Kaggle

---

### Limpieza y Pre-procesamiento
- Eliminación de columnas redundantes y **data leakage** (variables del equipo rojo).
- Separación Train/Test (80/20).
- **StandardScaler aplicado para SVM**, no obligatorio para árboles.

---

### Support Vector Machines
- Entrenamiento de:
  - SVM con **Kernel Lineal**
  - SVM con **Kernel RBF**
- Comparación de accuracy.
- Análisis de **separabilidad lineal** de las partidas de LoL.

---

### Árboles de Decisión
- Entrenamiento de un `DecisionTreeClassifier`.
- Visualización del árbol (profundidad limitada).
- Análisis de **Feature Importance**.

---

### Comparación Final
- **SVM:** mejor accuracy.
- **Árbol de Decisión:** mayor interpretabilidad.

---

##  Cómo ejecutar
1. Abrir el archivo `.ipynb`
2. Ejecutar las celdas en orden
3. Revisar las secciones de análisis y visualización