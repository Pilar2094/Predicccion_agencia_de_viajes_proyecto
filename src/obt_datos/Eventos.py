import requests
import pandas as pd
from time import sleep
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

# Leer dataset de ciudades
df_ciudades = pd.read_csv("../Predicccion_agencia_de_viajes_proyecto/data/processed/ciudades_con_clima.csv")

# Cargar variables de entorno
load_dotenv()
API_KEY = os.getenv("TICKETMASTER_API_KEY")

# Validar el token
if not API_KEY:
    raise ValueError("La clave de API de Ticketmaster no se encontró. Por favor, verifica tu archivo .env.")

# Para guardar los resultados
num_eventos = []
tipo_evento = []

# URL base de Ticketmaster para buscar eventos
url = "https://app.ticketmaster.com/discovery/v2/events.json"

# Recorrer cada fila del DataFrame de ciudades
for idx, row in df_ciudades.iterrows():
    ciudad = row['Ciudad']
    lat = row['Latitud']
    lon = row['Longitud']

    # Obtener la fecha de hoy y la fecha de fin (30 días más)
    fecha_inicio = datetime.utcnow().replace(second=0, microsecond=0).isoformat() + "Z"
    fecha_fin = (datetime.utcnow() + timedelta(days=30)).replace(second=0, microsecond=0).isoformat() + "Z"

    print(f"Buscando eventos para {ciudad} desde {fecha_inicio} hasta {fecha_fin}...")

    # Parámetros para la solicitud
    params = {
        "apikey": API_KEY,
        "latlong": f"{lat},{lon}",
        "radius": 50,  # Radio de búsqueda (50 km)
        "startDateTime": fecha_inicio,
        "endDateTime": fecha_fin,
        "size": 50,  # Número de eventos por solicitud
    }

    try:
        # Realizar la solicitud
        response = requests.get(url, params=params, timeout=20)
        print(f"Requesting events for {ciudad} with URL: {response.url}")  # Ver la URL completa

        if response.status_code == 200:
            data = response.json()
            events = data.get("_embedded", {}).get("events", [])
            num_eventos.append(len(events))

            if events:
                categorias = [event.get("classifications", [{}])[0].get("segment", {}).get("name", "Desconocido") for event in events]
                tipo_evento.append(categorias[0] if categorias else "Desconocido")
            else:
                tipo_evento.append("Sin eventos")
        else:
            print(f"Error en {ciudad}: {response.status_code} {response.text}")
            num_eventos.append(None)
            tipo_evento.append(None)

    except Exception as e:
        print(f"Error buscando eventos en {ciudad}: {str(e)}")
        num_eventos.append(None)
        tipo_evento.append(None)

    sleep(1)  # Esperar para no sobrecargar la API

# Añadir los resultados al DataFrame
df_ciudades['num_eventos'] = num_eventos
df_ciudades['tipo_evento'] = tipo_evento

# Guardarlo en un nuevo CSV
df_ciudades.to_csv("../Predicccion_agencia_de_viajes_proyecto/data/processed/ciudades_con_eventos.csv", index=False)

print("¡Eventos añadidos correctamente con Ticketmaster!")