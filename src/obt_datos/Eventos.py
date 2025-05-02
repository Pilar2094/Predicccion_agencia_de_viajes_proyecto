import requests
import pandas as pd
from time import sleep
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

# Leer dataset original con info climática
df_ciudades = pd.read_csv("../Predicccion_agencia_de_viajes_proyecto/data/processed/ciudades_con_clima.csv")

# Cargar clave API
load_dotenv()
API_KEY = os.getenv("TICKETMASTER_API_KEY")

if not API_KEY:
    raise ValueError("La clave de API de Ticketmaster no se encontró.")

# URL de eventos
url = "https://app.ticketmaster.com/discovery/v2/events.json"

# Lista para acumular todas las filas de salida
filas = []

for _, row in df_ciudades.iterrows():
    ciudad = row['Ciudad']
    lat = row['Latitud']
    lon = row['Longitud']
    temp = row['Temperatura']
    humedad = row['Humedad']
    descripcion_clima = row['Descripcion']

    fecha_inicio = datetime.utcnow().replace(second=0, microsecond=0).isoformat() + "Z"
    fecha_fin = (datetime.utcnow() + timedelta(days=30)).replace(second=0, microsecond=0).isoformat() + "Z"

    params = {
        "apikey": API_KEY,
        "latlong": f"{lat},{lon}",
        "radius": 50,
        "startDateTime": fecha_inicio,
        "endDateTime": fecha_fin,
        "size": 50,
    }

    try:
        response = requests.get(url, params=params, timeout=20)
        data = response.json()

        events = data.get("_embedded", {}).get("events", [])

        if events:
            for event in events:
                nombre_evento = event.get("name", "Desconocido")
                fecha_evento = event.get("dates", {}).get("start", {}).get("localDate", "Sin fecha")
                descripcion_evento = event.get("info", "Sin descripción")

                filas.append({
                    "Ciudad": ciudad,
                    "Latitud": lat,
                    "Longitud": lon,
                    "Temperatura": temp,
                    "Humedad": humedad,
                    "Descripcion": descripcion_clima,
                    "Nombre_Evento": nombre_evento,
                    "Fecha_Evento": fecha_evento,
                    "Descripcion_Evento": descripcion_evento
                })
        else:
            # Si no hay eventos, igual agregar una fila para registrar ausencia
            filas.append({
                "Ciudad": ciudad,
                "Latitud": lat,
                "Longitud": lon,
                "Temperatura": temp,
                "Humedad": humedad,
                "Descripcion": descripcion_clima,
                "Nombre_Evento": "Sin eventos",
                "Fecha_Evento": "",
                "Descripcion_Evento": ""
            })

    except Exception as e:
        print(f"Error con {ciudad}: {str(e)}")

    sleep(1)

# Crear DataFrame final
df_eventos = pd.DataFrame(filas)

# Guardar a CSV
df_eventos.to_csv("../Predicccion_agencia_de_viajes_proyecto/data/processed/ciudades_con_eventos.csv", index=False)

print("✅ Archivo guardado con eventos en filas separadas.")