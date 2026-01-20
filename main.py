import os
from openai import OpenAI

#API KEY
client = OpenAI()
print(os.getenv("OPENAI_API_KEY")) 
if os.getenv("OPENAI_API_KEY") is None:
    print("API key no encontrada❗ \n▶ Obten tu clave desde https://platform.openai.com/settings/organization/api-keys")
    exit()

def get_clipboard_image_base64():
    use_image = input("¿Pegar imagen? s/n: ")
    if use_image.lower() == "s":
        print("🖼️ [SIMULACIÓN] Imagen pegada")
        return "imagen_simulada_base64"
    return None

# Función de audio (SIMULACIÓN TOTAL)
def record_audio():
    print("🎤 [SIMULACIÓN] Grabando audio...")
    print("── .✦ ── .✦")
    print("✅ [SIMULACIÓN] Audio capturado")

# Transcripción simulada
def transcribe_audio():
    print("📝 [SIMULACIÓN] Transcribiendo audio...")
    return "Esto es una transcripción simulada del usuario."


# BIENVENIDA E INSTRUCCIONES
name = input('Ingresa tu nombre: ')
print(f'\nBienvenid@ {name}.\n')

print ('''
INFO: Tu tutor puede imitar la personalidad de personajes famosos.
Para hacerlo, ingresa el nombre del personaje y de donde proviene. 
Ejemplo: Tony Stark de Marvel, Batman de DC, Vegeta de DB, etc. 
Si tu nombre es de uso común responde "c" en "¿De donde es tu tutor?".
       ''')

tutor = input('\n¿Deseas darle un nombre a tu tutor? s/n ')

if tutor.lower() == 's':
    tutor = input('Ingresa el nombre de tu tutor: ')
    tutor_is_from = input('¿De donde es tu tutor? ')
else:
    tutor = "Tutor"
    tutor_is_from = "c"

# PROMPTS
system_prompt_normal = f"""
Eres un tutor académico claro, paciente y conciso, vas al grano.
Explicas conceptos con ejemplos y analogías.
Haces referencias a películas.
Nunca dejas de ser educativo y comprensible.
Tu nombre es {tutor}
"""

system_prompt_char = f"""
Eres un tutor académico claro, paciente y conciso, vas al grano.
Explicas conceptos con ejemplos y analogías.
Tu forma de hablar debe imitar el estilo del personaje: {tutor}.
Nunca dejas de ser educativo y comprensible.
"""

system_prompt = system_prompt_normal if tutor_is_from.lower() == "c" else system_prompt_char
messages = [{"role": "system", "content": system_prompt}]


print("\nEscribe tu pregunta. Puedes pegar imágenes desde el portapapeles con Ctrl+V.")
print("Escribe 'salir' para terminar.\n")

while True:

    mode = input("Ingresa 't' para escribir o 'v' para hablar: ")

    if mode.lower() == "v":
        record_audio()
        user_input = transcribe_audio()
        print(f"📝 Transcripción: {user_input}")

    else:
        user_input = input(f"{name}: ")

    # SALIDA
    if user_input.lower() == "salir":
        print("Tutor apagado.")
        break

    # CONTROL DE IMAGENES
    image_base64 = get_clipboard_image_base64()

    if image_base64:
        print("🖼️ Imagen detectada (SIMULACIÓN).")
        messages.append({"role": "user", "content": user_input + " [Imagen simulada]"})

    # ENTRADA DEL USUARIO
    else:
        messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_completion_tokens=20
    )

    tutor_reply = response.choices[0].message.content
    print(f"\n{tutor}:", tutor_reply)

    messages.append({"role": "assistant", "content": tutor_reply})