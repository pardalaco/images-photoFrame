# photoFrame

`photoFrame` es una aplicación simple que permite agregar un marco blanco de proporción 1:1 a todas las imágenes contenidas en una carpeta. El programa toma como entrada la ruta de una carpeta con imágenes y la ruta de salida donde se guardarán las imágenes con el marco aplicado. Utiliza OpenCV (`cv2`) y NumPy para el procesamiento de las imágenes, y una interfaz gráfica básica con `tkinter` para facilitar la selección de las carpetas.

## Características

- Añade un marco blanco de proporción 1:1 a las imágenes.
- Interfaz gráfica con `tkinter` para seleccionar las rutas de entrada y salida.
- Exporta las imágenes con el marco a una carpeta de destino especificada por el usuario.

## Requisitos

- Python 3.x
- Librerías necesarias:
  - `opencv-python` (Para manipulación de imágenes)
  - `numpy` (Para manejo de matrices y dimensiones)
  - `tkinter` (Para la interfaz gráfica)

## Uso

### Ejecución del programa

Puedes ejecutar la aplicación desde la terminal o usar la interfaz gráfica para seleccionar las carpetas de entrada y salida.

1. **Ejecución desde terminal**:
   Para ejecutar la aplicación, utiliza el siguiente comando:

   ```bash
   python photoFrame.py <ruta_de_entrada> <ruta_de_salida>
   ```

2. **Uso con interfaz gráfica**:
   Simplemente ejecuta el programa sin argumentos:

   ```bash
   python photoFrame.py
   ```

   Esto abrirá una ventana emergente donde podrás seleccionar las carpetas a través de la interfaz gráfica.


### Uso con Interfaz Gráfica

La aplicación esta exportada como formato de aplicación para macOS.