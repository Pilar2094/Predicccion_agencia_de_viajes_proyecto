import requests
import csv
import pandas as pd
import os
import time  # Importamos el módulo para hacer pausas

# Ruta al archivo CSV con las ciudades
ciudades_file_path = "/Users/joanafernandes/Data Science Bootcamp/Predicccion_agencia_de_viajes_proyecto/data/processed/ciudades_con_clima.csv"

# Leer el archivo CSV para obtener las ciudades
df = pd.read_csv(ciudades_file_path)

# Verificar las columnas en el archivo CSV
df.columns = df.columns.str.strip()  # Eliminar espacios en los nombres de las columnas
ciudades = df['Ciudad'].tolist()

# Solicitar al usuario la fecha de entrada, fecha de salida y la cantidad de personas
checkin_date = input("Introduce la fecha de entrada (YYYY-MM-DD): ")
checkout_date = input("Introduce la fecha de salida (YYYY-MM-DD): ")
adults = input("Introduce el número de adultos: ")

# URL y parámetros para la solicitud a la API (de hoteles)
hotel_url = "https://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/{country}/{currency}/{locale}/{originPlace}/{destinationPlace}/{outboundDate}/{inboundDate}"

# Tu API Key (reemplaza con la tuya)
headers = {
    "X-RapidAPI-Key": "00a9d75f9cmshe80dc90d83ba4b2p1f5989jsn9ca86a8265e4",
    "X-RapidAPI-Host": "skyscanner44.p.rapidapi.com"
}

# Lista para almacenar los resultados que vamos a guardar en el CSV
resultados_hoteles = []

# Recorremos las ciudades en el archivo CSV
for ciudad in ciudades:
    querystring = {
        "location": ciudad,
        "checkin_date": checkin_date,
        "checkout_date": checkout_date,
        "adults": adults,
        "currency": "EUR"
    }

    # Hacer la solicitud a la API para obtener los resultados de hoteles
    try:
        response = requests.get(hotel_url, headers=headers, params=querystring)

        if response.status_code == 200:
            data = response.json()
            
            # Procesar los hoteles con los detalles extra
            for hotel in data.get('hotels', []):
                nombre = hotel.get('name', 'Desconocido')
                precio = hotel.get('price', {}).get('amount', 'No disponible')
                moneda = hotel.get('price', {}).get('currency', 'EUR')
                direccion = hotel.get('address', 'No disponible')
                rating = hotel.get('rating', 'No disponible')
                distancia_centro = hotel.get('distance_from_center', 'No disponible')
                imagen = hotel.get('image_url', 'No disponible')
                
                # Guardar los resultados relevantes en la lista
                resultados_hoteles.append([ciudad, nombre, precio, moneda, direccion, rating, distancia_centro, imagen])
        else:
            print(f"Error al obtener datos para {ciudad}: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud para {ciudad}: {e}")
    
    time.sleep(2)  # Pausar 2 segundos entre solicitudes para evitar el límite de la API

# Guardar los resultados en un archivo CSV de hoteles
output_file_path_hoteles = os.path.join("../Predicccion_agencia_de_viajes_proyecto/data/processed/hoteles_filtrados.csv")

with open(output_file_path_hoteles, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Ciudad", "Hotel", "Precio", "Moneda", "Dirección", "Rating", "Distancia al Centro", "Imagen"])
    writer.writerows(resultados_hoteles)

print(f"Datos de hoteles guardados en '{output_file_path_hoteles}'")