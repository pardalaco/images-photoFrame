import cv2
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Funciones de generación de imagen
# --------------------------------------------------------
def cargar_y_escale_imagen(ruta_imagen, tamaño_maximo=1000):
    # Cargar la imagen desde la ruta especificada
    imagen = cv2.imread(ruta_imagen)
    
    if imagen is None:
        raise FileNotFoundError(f"No se pudo cargar la imagen desde {ruta_imagen}")

    # Obtener las dimensiones de la imagen
    alto, ancho = imagen.shape[:2]

    # Calcular el factor de escala para que la imagen tenga un tamaño máximo de tamaño_maximo
    factor_escala = tamaño_maximo / max(alto, ancho)
    
    # Redimensionar la imagen manteniendo la relación de aspecto
    nuevo_alto = int(alto * factor_escala)
    nuevo_ancho = int(ancho * factor_escala)
    imagen_redimensionada = cv2.resize(imagen, (nuevo_ancho, nuevo_alto))
    
    return imagen_redimensionada

def colocar_imagen_en_centro(imagen_centrada, tamaño_imagen=1080):
    # Crear una imagen blanca de tamaño_imagen x tamaño_imagen
    imagen_blanca = np.ones((tamaño_imagen, tamaño_imagen, 3), dtype=np.uint8) * 255

    # Obtener las dimensiones de la imagen redimensionada
    alto, ancho = imagen_centrada.shape[:2]

    # Calcular la posición para centrar la imagen
    x_inicio = (tamaño_imagen - ancho) // 2
    y_inicio = (tamaño_imagen - alto) // 2

    # Colocar la imagen redimensionada en el centro de la imagen blanca
    imagen_blanca[y_inicio:y_inicio+alto, x_inicio:x_inicio+ancho] = imagen_centrada
    
    return imagen_blanca


# Funciones TKinter
# --------------------------------------------------------
def seleccionar_carpeta_entrada():
    ruta = filedialog.askdirectory()
    if ruta:
        entrada_var.set(ruta)
        verificar_rutas()

def seleccionar_carpeta_salida():
    ruta = filedialog.askdirectory()
    if ruta:
        salida_var.set(ruta)
        verificar_rutas()

def verificar_rutas():
    if entrada_var.get() and salida_var.get():
        boton_generar.config(state=tk.NORMAL)
    else:
        boton_generar.config(state=tk.DISABLED)

def generar():
     # Obtener la lista de archivos en la carpeta
    archivos = os.listdir(entrada_var.get())
    
    # Filtrar solo los archivos de imagen (por ejemplo, .jpg, .png)
    archivos_imagenes = [f for f in archivos if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    for archivo in archivos_imagenes:
        ruta_imagen = os.path.join(entrada_var.get(), archivo)
        
        # Cargar y redimensionar la imagen
        imagen_redimensionada = cargar_y_escale_imagen(ruta_imagen)
        
        # Crear la imagen blanca y colocar la imagen redimensionada en el centro
        imagen_final = colocar_imagen_en_centro(imagen_redimensionada)

        # Definir la ruta de salida para la imagen procesada
        ruta_salida_imagen = os.path.join(salida_var.get(), archivo)

        # Guardar la imagen final en la carpeta de salida
        cv2.imwrite(ruta_salida_imagen, imagen_final)



    # Mensaje de información
    if archivos_imagenes:
        archivos_lista = "\n".join(archivos_imagenes)
        messagebox.showinfo(
            "¡Proceso completado!",
            f"Las siguientes imágenes se han procesado correctamente:\n\n{archivos_lista}"
        )
    else:
        messagebox.showinfo(
            "Sin imágenes",
            "No se encontraron imágenes en la carpeta especificada."
        )

        
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Selector de Carpetas")

# Variables para almacenar las rutas
entrada_var = tk.StringVar()
salida_var = tk.StringVar()

# Crear botones para seleccionar carpetas
boton_entrada = tk.Button(ventana, text="Seleccionar Carpeta de Entrada", command=seleccionar_carpeta_entrada)
boton_entrada.pack(pady=5)

# Etiquetas para mostrar las rutas seleccionadas
etiqueta_entrada = tk.Label(ventana, textvariable=entrada_var, wraplength=300)
etiqueta_entrada.pack(pady=5)

boton_salida = tk.Button(ventana, text="Seleccionar Carpeta de Salida", command=seleccionar_carpeta_salida)
boton_salida.pack(pady=5)

etiqueta_salida = tk.Label(ventana, textvariable=salida_var, wraplength=300)
etiqueta_salida.pack(pady=5)

# Crear el botón de generar, inicialmente deshabilitado
boton_generar = tk.Button(ventana, text="Generar", command=generar, state=tk.DISABLED)
boton_generar.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
