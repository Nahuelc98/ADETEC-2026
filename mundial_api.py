from google import genai # Importamos librería de gemini ia.
from key_mundial import api_mundial # Traemos la variable con la clave de la api de gemini.

# Consultamos via IA el plantel de una selección:
client = genai.Client(api_key=api_mundial)
print("   --- VER PLANTEL ---   ")
print("-" * 30)
seleccion=input("Ingrese el nombre de la selección: ").capitalize().strip()
print(f"PLANTEL DE {seleccion.upper()}\n")

response = client.models.generate_content(
    model="gemini-3.5-flash-lite", # Elegir el modelo de LLM 
    # Promt para buscar el plantel de la selección:
    contents=f"Busca el listado oficial de jugadores convocados de FIFA que tengas disponible de la selección de {seleccion}. Entrega el resultado en formato lista de python donde cada elemento de esa lista es el nombre y apellido del jugador, su dorsal y su posición. Ejemplo: plantel = [['Lionel Messi',10, 'Mediocampista'], ['Emiliano Marinez', 23, 'Arquero']].En el caso que no encuentres información entrega el resultado con una lista vacía. Ejemplo: seleccion=[]. Para todo resultado sólo muestra la lista de Python sin texto ni comentarios.")
print(response.text)

# Escribimos la respuesta de la ia en un archivo .txt:
respuesta = str(response.text)
with open("ver_plantel.txt","w",encoding="utf-8") as respuesta_api:
    respuesta_api.write(respuesta)
