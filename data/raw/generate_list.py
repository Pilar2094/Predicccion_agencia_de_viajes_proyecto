import pandas as pd
from geopy.geocoders import Nominatim
from time import sleep

ciudades_por_temporada = [
    # Primavera (marzo - mayo)
    "Tokio, Japón", "París, Francia", "Barcelona, España", "Roma, Italia", "Madrid, España",
    "Ámsterdam, Países Bajos", "Lisboa, Portugal", "Estambul, Turquía", "Buenos Aires, Argentina", "Seúl, Corea del Sur",
    
    # Verano (junio - agosto)
    "Cancún, México", "Honolulú, Hawái, Estados Unidos", "Río de Janeiro, Brasil", "Sídney, Australia", "Bali, Indonesia",
    "Dubái, Emiratos Árabes Unidos", "Marrakech, Marruecos", "Lima, Perú", "Cartagena, Colombia", "Miconos, Grecia",
    
    # Otoño (septiembre - noviembre)
    "Nueva York, Estados Unidos", "Montreal, Canadá", "Vancouver, Canadá", "Praga, República Checa", "Londres, Reino Unido",
    "Berlín, Alemania", "Buenos Aires, Argentina", "San Francisco, Estados Unidos", "Ciudad de México, México", "Zúrich, Suiza",
    
    # Invierno (diciembre - febrero)
    "Moscú, Rusia", "Estocolmo, Suecia", "Helsinki, Finlandia", "Oslo, Noruega", "Copenhague, Dinamarca",
    "Reikiavik, Islandia", "Ginebra, Suiza", "Ámsterdam, Países Bajos", "Kitzbühel, Austria", "Quebec, Canadá",
    
    # Otras ciudades para completar las 100
    "Los Ángeles, Estados Unidos", "Chicago, Estados Unidos", "Houston, Estados Unidos", "Miami, Estados Unidos", "Berlín, Alemania",
    "Viena, Austria", "Budapest, Hungría", "Varsovia, Polonia", "Dublín, Irlanda", "Oslo, Noruega",
    "Estocolmo, Suecia", "Helsinki, Finlandia", "Zúrich, Suiza", "Ginebra, Suiza", "Bruselas, Bélgica",
    "Moscú, Rusia", "Estambul, Turquía", "Dubái, Emiratos Árabes Unidos", "Tokio, Japón", "Osaka, Japón",
    "Seúl, Corea del Sur", "Pekín, China", "Shanghái, China", "Bangkok, Tailandia", "Singapur, Singapur",
    "Kuala Lumpur, Malasia", "Yakarta, Indonesia", "Manila, Filipinas", "Ciudad Ho Chi Minh, Vietnam", "Hanói, Vietnam",
    "Nueva Delhi, India", "Bombay, India", "Bangalore, India", "Chennai, India", "Hyderabad, India",
    "Ciudad del Cabo, Sudáfrica", "Johannesburgo, Sudáfrica", "El Cairo, Egipto", "Casablanca, Marruecos", "Marrakech, Marruecos",
    "Río de Janeiro, Brasil", "São Paulo, Brasil", "Buenos Aires, Argentina", "Santiago, Chile", "Lima, Perú",
    "Bogotá, Colombia", "Medellín, Colombia", "Caracas, Venezuela", "Quito, Ecuador", "Ciudad de Panamá, Panamá",
    "Ciudad de México, México", "Guadalajara, México", "Cancún, México", "Punta Cana, República Dominicana", "San Juan, Puerto Rico",
    "Toronto, Canadá", "Vancouver, Canadá", "Montreal, Canadá", "Calgary, Canadá", "Ottawa, Canadá",
    "Sídney, Australia", "Melbourne, Australia", "Brisbane, Australia", "Perth, Australia", "Auckland, Nueva Zelanda",
    "Wellington, Nueva Zelanda", "Honolulú, Hawái, Estados Unidos", "Anchorage, Alaska, Estados Unidos", "Reikiavik, Islandia", "Tallin, Estonia",
    "Riga, Letonia", "Vilna, Lituania", "Luxemburgo, Luxemburgo", "Mónaco, Mónaco", "San Marino, San Marino",
    "Andorra la Vieja, Andorra", "La Valeta, Malta", "Doha, Catar", "Ciudad de Kuwait, Kuwait", "Manama, Baréin",
    "Ammán, Jordania", "Jerusalén, Israel", "Teherán, Irán", "Bagdad, Irak", "Beirut, Líbano",
    "Túnez, Túnez", "Argel, Argelia", "Nairobi, Kenia", "Adís Abeba, Etiopía", "Acra, Ghana"
]

# Inicializar geolocalizador
geolocator = Nominatim(user_agent="geoapiExercises")

# Lista para almacenar coordenadas
data = []

# Obtener coordenadas para cada ciudad
for ciudad in ciudades_por_temporada:
    try:
        location = geolocator.geocode(ciudad)
        if location:
            data.append({
                "ciudad": ciudad,
                "lat": location.latitude,
                "lon": location.longitude
            })
    except Exception as e:
        print(f"Error en {ciudad}: {e}")
    sleep(1)  # Pausa para evitar sobrecarga en el servidor

# Convertir a DataFrame
df_ciudades = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
output_path = '../Modelo_recomendaci-n_Agencia_de_viajes/data/raw/listado_destinos_coordenadas.csv'  
df_ciudades.to_csv(output_path, index=False)

print("✅ El archivo CSV ha sido guardado como 'destinos_temporada.csv'.")