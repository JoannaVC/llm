# Proyecto 8: LLM
Este proyecto implementa un tutor académico interactivo usando la API de OpenAI.
Permite al usuario hacer preguntas por texto, voz (simulada) e imágenes (simuladas), y recibir respuestas educativas personalizadas.

## Funciones
- Entrada por texto
- Entrada por voz (simulada)
- Entrada por imagen (simulada)
- Tutor con personalidad configurable (imitación de personajes)

## Requisitos
- Python
- Librería openai
- API Key de OpenAI

## Instrucciones
- Ingrese a https://platform.openai.com/settings/organization/api-keys
- Cree una cuenta
- Genere su API_KEY
- Guarde su API_KEY
- Abra su terminal
- Copie y pegue el siguiente comando:

´´´bash
export OPENAI_API_KEY="ingrese su API_KEY aquí"
´´´
se debería ver así:

export OPENAI_API_KEY="sk-7Fh3KpL9XQ2mWZ8T4RjA6C0YB"

- Ejecute el archivo principal:
´´´bash
python main.py
´´´
- 

## Notas:
- La idea original del proyecto era permitir pegar imágenes reales desde el portapapeles y usar micrófono.
- WSL no soporta portapapeles de imágenes ni micrófono de forma nativa.
- Debido a las limitaciones de cuota de la API de OpenAI, no fue posible implementar entrada real por voz o imagen en Windows/MacOS.
- Por esta razón, se implementaron simulaciones para representar la intención del proyecto.
- También se limitó el uso de tokens para evitar consumo excesivo de cuota.