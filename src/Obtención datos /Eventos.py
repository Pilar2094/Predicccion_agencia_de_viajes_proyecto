import requests
import pandas as pd
from time import sleep
from dotenv import load_dotenv
import os
from datetime import datetime

# Leer dataset
df_ciudades = pd.read_csv("../Modelo_recomendaci-n_Agencia_de_viajes/data/processed/Datos_climaticos_completos_hist.csv")

# Cargar variables de entorno
load_dotenv()
TOKEN = os.getenv("Event_BRITE_KEY")

# Validar el token
if not TOKEN:
    raise ValueError("El token de Eventbrite no se encontró. Por favor, verifica tu archivo .env.")

# Para guardar resultados
num_eventos = []
tipo_evento = []

# URL base
url = "https://www.eventbriteapi.com/v3/events/search/"

# Recorrer cada fila
for idx, row in df_ciudades.iterrows():
    ciudad = row['Ciudad']
    lat = row['Latitud']
    lon = row['Longitud']

    # Obtener la fecha de hoy en formato ISO (sin microsegundos)
    fecha_actual = datetime.utcnow().replace(second=0, microsecond=0).isoformat() + "Z"

    print(f"Buscando eventos para {ciudad} a partir de {fecha_actual}...")

    # Parámetros para la solicitud
    params = {
        "location.latitude": lat,
        "location.longitude": lon,
        "location.within": "30km",
        "start_date.range_start": fecha_actual,
        "token": TOKEN  # Token en la URL
    }

    try:
        # Realizar la solicitud
        response = requests.get(url, params=params, timeout=20)
        print(f"Requesting events for {ciudad} with URL: {response.url}")  # Ver la URL

        if response.status_code == 200:
            data = response.json()
            eventos = data.get('events', [])
            num_eventos.append(len(eventos))

            if eventos:
                categorias = [evento.get('category_id', "Desconocido") for evento in eventos]
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

# Añadir resultados al dataframe
df_ciudades['num_eventos'] = num_eventos
df_ciudades['tipo_evento'] = tipo_evento

# Guardarlo
df_ciudades.to_csv("../Modelo_recomendaci-n_Agencia_de_viajes/data/processed/ciudades_con_eventos.csv", index=False)

print("¡Eventos añadidos correctamente!")