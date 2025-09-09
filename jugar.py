"""
Jugar
"""
import pyautogui
import time
import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras
from PIL import Image
import os
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
# Ruta a las imágenes capturadas
pyautogui.press('space')
# Tamaño de entrada esperado por la capa densa
input_shape = input_shape = (15, 15, 1)  # Cambiamos a una resolución de 64x64
imagen_anterior = pyautogui.screenshot(region=(750, 450, 250, 2 ))
imagen_anterior = imagen_anterior.resize((input_shape[1], input_shape[0]))  # Reescalar la imagen a 64x64
imagen_anterior = imagen_anterior.convert("L")  # Convertir a escala de grises
imagen_anterior = np.array(imagen_anterior) / 255.0  # Normalizar los valores de píxeles
imagen_anterior = imagen_anterior[:, :, np.newaxis]
# Definir la función para verificar si las imágenes son idénticas
def are_images_identical(image1, image2):
    if np.array_equal(np.array(image1), np.array(image2)):
        return 0
    else:
        return 1
prediccion = 0
t = 0
modelo_cargado =  keras.models.load_model('dino_chan.h5')
while True:
    screenshot = pyautogui.screenshot(region=(750, 449, 170, 20 ))
    screenshot = screenshot.resize((input_shape[1], input_shape[0]))  # Reescalar la imagen a 64x64
    screenshot = screenshot.convert("L")  # Convertir a escala de grises
    screenshot = np.array(screenshot) / 255.0  # Normalizar los valores de píxeles
    screenshot = screenshot[:, :, np.newaxis]
    # Obtener el estado actual (imagen)
    estado_actual = screenshot
    # Cargar las imágenes anteriores y calcular la diferencia
    if are_images_identical(imagen_anterior, estado_actual) != 1 and t>15:
        imagen_anterior = estado_actual
        pyautogui.press('space')  # Presionar la tecla "space" para reiniciar el juego
        pyautogui.press('space')  # Presionar la tecla "space" para reiniciar el juego
        t = 0  # Reiniciar el tiempo de juego
    else:
        imagen_anterior = estado_actual
        # Decidir si saltar o no
        # Cargar el modelo desde el archivo HDF5
        prediccion = modelo_cargado.predict(imagen_anterior[np.newaxis, ...], verbose = 0)
        # Decidir si saltar o no
        decision = 1 if prediccion >= 0.5 else 0
        #print(decision)
        if decision == 1:
            pyautogui.press('space')
    t += 1  # Incrementar el tiempo de juego

    # Mostrar la imagen en tiempo real
    #plt.imshow(estado_actual[:, :, 0], cmap='gray')  # Mostrar el primer canal de la imagen en escala de grises
    #plt.pause(0.01)  # Pausa breve para que la imagen se actualice en la ventana
    #plt.clf()  # Limpiar el gráfico en cada iterac ión
    #plt.xticks([])
    #plt.yticks([])
