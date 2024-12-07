Paso 1: Instalar PyInstaller
Primero, asegúrate de tener PyInstaller instalado. Puedes instalarlo usando pip:

bash
Copy code
pip install pyinstaller
Paso 2: Crear un Script de Ejecución
Crea un script de Python que inicie tu aplicación de Streamlit. Llamemos a este script run_app.py:

run_app.py:

python
Copy code
import subprocess
import sys

def run_streamlit_app():
    subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])

if __name__ == "__main__":
    run_streamlit_app()
Paso 3: Empaquetar con PyInstaller
Ahora, usa PyInstaller para empaquetar tu aplicación. Asegúrate de que todos los archivos necesarios (como diccionario.json, lecciones.json, y app.py) estén en el mismo directorio que run_app.py.

Ejecuta el siguiente comando en la terminal:

bash
Copy code
pyinstaller --onefile --add-data "app.py;." --add-data "diccionario.json;." --add-data "lecciones.json;." run_app.py
Explicación de las Opciones:
--onefile: Crea un solo archivo ejecutable.

--add-data "app.py;.": Incluye app.py en el paquete.

--add-data "diccionario.json;.": Incluye diccionario.json en el paquete.

--add-data "lecciones.json;.": Incluye lecciones.json en el paquete.

Paso 4: Ejecutar el Archivo .exe
Después de que PyInstaller termine, encontrarás un archivo .exe en la carpeta dist. Este archivo es tu aplicación empaquetada. Puedes distribuir este archivo .exe y ejecutarlo en cualquier sistema Windows sin necesidad de instalar Python o las dependencias.

Notas Adicionales
Tamaño del Archivo: El archivo .exe generado puede ser bastante grande debido a que incluye todas las dependencias de Python.

Compatibilidad: Asegúrate de que todas las dependencias y bibliotecas que utilizas sean compatibles con el sistema operativo en el que estás empaquetando la aplicación.

Recursos Estáticos: Si tienes más archivos estáticos (como imágenes, otros archivos json, etc.), asegúrate de incluirlos en el comando pyinstaller usando la opción --add-data.

Ejemplo Completo
Aquí tienes un ejemplo completo de cómo podrías estructurar tu proyecto:

Copy code
proyecto/
│
├── app.py
├── diccionario.json
├── lecciones.json
├── run_app.py
└── dist/
    └── run_app.exe
Ejecutar el Archivo .exe
Simplemente haz doble clic en run_app.exe dentro de la carpeta dist para ejecutar tu aplicación de Streamlit.

¡Y eso es todo! Ahora tienes tu aplicación de Streamlit empaquetada en un archivo .exe que puedes distribuir fácilmente.
