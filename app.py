import streamlit as st
import json
import os
import getpass
from googletrans import Translator
import speech_recognition as sr
import gtts
import playsound
import modelo

# Cargar diccionario y lecciones
with open('diccionario.json', 'r', encoding='utf-8') as f:
    diccionario = json.load(f)

with open('lecciones.json', 'r', encoding='utf-8') as f:
    lecciones = json.load(f)

# Función para convertir texto a voz
def speak(text, lang='es'):
    tts = gtts.gTTS(text, lang=lang)
    tts.save("response.mp3")
    playsound.playsound("response.mp3")
    os.remove("response.mp3")

# Función para escuchar la entrada del usuario
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Escuchando...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='es')
            return text
        except Exception as e:
            st.write(f"Error al escuchar: {e}")
    return ""

# Función para traducir texto
def translate(text, src_lang, dest_lang):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

# Detectar el nombre del usuario
username = getpass.getuser()

# Interfaz de Streamlit
st.title(f"Tutor de Coreano - ¡Hola {username}!")

# Menú de navegación
menu = st.sidebar.selectbox("Menú", ["Lecciones", "Diccionario", "Tareas"])

# Cargar o inicializar tareas
if os.path.exists("tareas.json"):
    with open("tareas.json", "r") as f:
        tareas = json.load(f)
else:
    tareas = []

# Cargar o inicializar modelo de PyTorch
if os.path.exists("model.pth"):
    model = modelo.load_model()
else:
    model = modelo.SimpleModel()
    modelo.save_model(model)

if menu == "Lecciones":
    st.header("Lecciones")
    for leccion in lecciones:
        st.subheader(leccion['titulo'])
        st.write(leccion['descripcion'])
        for ejercicio in leccion['ejercicios']:
            respuesta = st.text_input(ejercicio['pregunta'])
            if respuesta.lower() == ejercicio['respuesta'].lower():
                st.success("¡Correcto!")
            else:
                st.error("Incorrecto")

elif menu == "Diccionario":
    st.header("Diccionario")
    palabra = st.text_input("Buscar palabra")
    if palabra in diccionario:
        st.write(f"Coreano: {diccionario[palabra]['coreano']}")
        st.write(f"Definición: {diccionario[palabra]['definicion']}")
        st.write(f"Ejemplo: {diccionario[palabra]['ejemplo']}")
    else:
        st.write("Palabra no encontrada")

elif menu == "Tareas":
    st.header("Tareas")
    tarea = st.text_input("Agregar tarea")
    if tarea:
        tareas.append(tarea)
        with open("tareas.json", "w") as f:
            json.dump(tareas, f)
        st.write(f"Tarea agregada: {tarea}")

    if tareas:
        st.subheader("Tareas pendientes")
        for tarea in tareas:
            st.write(tarea)

# Sección de traducción
st.header("Traducción")
user_input = listen()
if user_input:
    st.write(f"Usuario: {user_input}")
    
    # Traducir de español a coreano
    korean_translation = translate(user_input, 'es', 'ko')
    st.write(f"Coreano: {korean_translation}")
    speak(korean_translation, lang='ko')
    
    # Traducir de coreano a español
    spanish_translation = translate(korean_translation, 'ko', 'es')
    st.write(f"Español: {spanish_translation}")
    speak(spanish_translation, lang='es')
