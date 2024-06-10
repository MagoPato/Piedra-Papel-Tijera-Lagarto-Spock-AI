import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam
import tkinter as tk
from tkinter import messagebox
import threading

# Definimos las opciones disponibles
opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]

# Mapeo de opciones a números
opciones_map = {op: idx for idx, op in enumerate(opciones)}
opciones_inv_map = {idx: op for op, idx in opciones_map.items()}

# Definimos las reglas del juego
reglas = {
    "piedra": ["tijera", "lagarto"],
    "papel": ["piedra", "spock"],
    "tijera": ["papel", "lagarto"],
    "lagarto": ["papel", "spock"],
    "spock": ["piedra", "tijera"]
}

# Creación del modelo
def crear_modelo():
    model = Sequential([
        LSTM(128, input_shape=(None, 5), return_sequences=True),
        LSTM(128),
        Dense(5, activation='softmax')
    ])
    model.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy')
    return model

modelo = crear_modelo()

# Función para determinar el ganador
def determinar_ganador(eleccion_jugador, eleccion_ia):
    if eleccion_jugador == eleccion_ia:
        return "Empate"
    elif eleccion_ia in reglas[eleccion_jugador]:
        return "Ganaste"
    else:
        return "Perdiste"

# Función para convertir jugadas a vectores
def convertir_a_vector(eleccion):
    vector = np.zeros(5)
    vector[opciones_map[eleccion]] = 1
    return vector

# Inicializamos el historial de jugadas
historial = []

# Función para entrenar el modelo basado en el historial
def entrenar_modelo(historial):
    if len(historial) > 10:
        X = []
        y = []
        for i in range(len(historial) - 6):
            X.append(historial[i:i+5])
            y.append(historial[i+5])
        
        X = np.array(X)
        y = np.array(y)
        modelo.fit(X, y, epochs=20, verbose=0)

# Función para actualizar la jugada
def actualizar_jugada(eleccion_jugador):
    # Deshabilitar los botones
    for btn in botones:
        btn.config(state=tk.DISABLED, bg="gray")
    
    entrada_jugador = convertir_a_vector(eleccion_jugador)
    
    if len(historial) >= 5:
        input_seq = np.array(historial[-5:]).reshape(1, 5, 5)
        prediccion = modelo.predict(input_seq, verbose=0)
        eleccion_ia = opciones_inv_map[np.argmax(prediccion)]
    else:
        eleccion_ia = np.random.choice(opciones)  # Para las primeras jugadas

    resultado = determinar_ganador(eleccion_jugador, eleccion_ia)
    resultado_texto.set(f"IA eligió: {eleccion_ia}. Resultado: {resultado}")

    historial.append(entrada_jugador)
    salida_ia = convertir_a_vector(eleccion_ia)
    historial.append(salida_ia)
    
    entrenar_modelo(historial)
    
    # Habilitar los botones
    for btn in botones:
        btn.config(state=tk.NORMAL, bg=boton_colores[btn.cget('text').lower()])

# Configuración de la GUI
ventana = tk.Tk()
ventana.title("Piedra, Tijera, Papel, Lagarto, Spock")
ventana.geometry("500x300")
ventana.configure(bg="lightblue")
ventana.resizable(False, False)

frame = tk.Frame(ventana, bg="lightblue")
frame.pack(pady=20)

resultado_texto = tk.StringVar()
resultado_texto.set("Haz tu elección:")

tk.Label(frame, textvariable=resultado_texto, font=("Helvetica", 14), bg="lightblue").pack(pady=10)

botones_frame = tk.Frame(ventana, bg="lightblue")
botones_frame.pack(pady=20)

boton_colores = {
    "piedra": "lightgray",
    "papel": "white",
    "tijera": "lightpink",
    "lagarto": "lightgreen",
    "spock": "lightblue"
}

botones = []

for opcion in opciones:
    btn = tk.Button(botones_frame, text=opcion.capitalize(), font=("Helvetica", 12), bg=boton_colores[opcion],
                    command=lambda op=opcion: threading.Thread(target=actualizar_jugada, args=(op,)).start())
    btn.pack(side=tk.LEFT, padx=10)
    botones.append(btn)

tk.Button(ventana, text="Salir", font=("Helvetica", 12), bg="red", command=ventana.quit).pack(pady=10)

ventana.mainloop()
