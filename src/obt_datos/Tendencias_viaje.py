from pytrends.request import TrendReq
import pandas as pd
from time import sleep

# Cargar tus ciudades
df_ciudades = pd.read_csv("../Modelo_recomendaci-n_Agencia_de_viajes/data/processed/ciudades_con_clima.csv")

# Conectar a Google Trends
pytrends = TrendReq(hl='es-ES', tz=360)

popularidad = []

for idx, row in df_ciudades.iterrows():
    ciudad = row['Ciudad']

    try:
        print(f"Buscando tendencias para {ciudad}...")
        pytrends.build_payload([f"Viajar a {ciudad}"], timeframe='today 12-m')  # Últimos 12 meses
        interest = pytrends.interest_over_time()
        if not interest.empty:
            promedio = interest.mean().values[0]
            popularidad.append(promedio)
        else:
            popularidad.append(0)
    except Exception as e:
        print(f"Error para {ciudad}: {str(e)}")
        popularidad.append(None)

    sleep(2)  # 🔥 Dormir 2 segundos para no ser bloqueado

# Agregar la columna
df_ciudades['popularidad_trends'] = popularidad

# Guardar
df_ciudades.to_csv("../Modelo_recomendaci-n_Agencia_de_viajes/data/processed/ciudades_con_tendencias.csv", index=False)

print("¡Tendencias añadidas correctamente!")