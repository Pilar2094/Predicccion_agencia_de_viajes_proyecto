import pandas as pd

# Datos base por ciudad (sin estación aún)
data_base = [
    ["Tokyo, Japón", "Solitario / Cultura", "Ciudad / Cultura"],
    ["París, Francia", "Pareja / Cultura", "Ciudad / Romántico"],
    ["Barcelona, España", "Pareja / Amigos", "Ciudad / Playa / Cultura"],
    ["Roma, Italia", "Pareja / Cultura", "Ciudad / Cultura / Romántico"],
    ["Madrid, España", "Solitario / Pareja / Cultura", "Ciudad / Cultura"],
    ["Amsterdam, Países Bajos", "Solitario / Pareja / Amigos", "Ciudad / Cultura"],
    ["Lisboa, Portugal", "Pareja / Familia", "Ciudad / Cultura / Playa"],
    ["Estambul, Turquía", "Solitario / Cultura", "Ciudad / Cultura / Histórico"],
    ["Buenos Aires, Argentina", "Familia / Cultura", "Ciudad / Cultura"],
    ["Seúl, Corea del Sur", "Solitario / Cultura", "Ciudad / Cultura"],
    ["Cancún, México", "Pareja / Familia / Amigos", "Playa / Relax"],
    ["Honolulu, Hawái, EE. UU.", "Pareja / Familia / Solitario", "Playa / Naturaleza"],
    ["Río de Janeiro, Brasil", "Pareja / Amigos", "Playa / Ciudad / Fiesta"],
    ["Sydney, Australia", "Familia / Solitario", "Playa / Ciudad / Naturaleza"],
    ["Bali, Indonesia", "Pareja / Solitario", "Playa / Relax / Cultura"],
    ["Dubai, Emiratos Árabes Unidos", "Pareja / Familia", "Ciudad / Lujo"],
    ["Marrakech, Marruecos", "Pareja / Solitario", "Cultura / Histórico"],
    ["Lima, Perú", "Solitario / Cultura", "Ciudad / Cultura / Histórico"],
    ["Cartagena, Colombia", "Pareja / Amigos / Familia", "Playa / Cultura"],
    ["Mykonos, Grecia", "Pareja / Amigos", "Playa / Fiesta / Relax"],
    ["Nueva York, EE. UU.", "Solitario / Pareja / Cultura", "Ciudad / Cultura"],
    ["Montreal, Canadá", "Familia / Solitario", "Ciudad / Naturaleza"],
    ["Vancouver, Canadá", "Solitario / Naturaleza", "Naturaleza / Ciudad"],
    ["Praga, República Checa", "Pareja / Cultura", "Ciudad / Cultura / Romántico"],
    ["Londres, Reino Unido", "Solitario / Cultura", "Ciudad / Cultura"],
    ["Berlín, Alemania", "Solitario / Cultura", "Ciudad / Cultura / Historia"],
    ["San Francisco, EE. UU.", "Solitario / Innovación", "Ciudad / Cultura / Tecnología"],
    ["Ciudad de México, México", "Cultura / Familia", "Ciudad / Cultura"],
    ["Zurich, Suiza", "Solitario / Naturaleza", "Ciudad / Naturaleza"],
    ["Moscú, Rusia", "Solitario / Cultura", "Ciudad / Cultura / Invierno"],
    ["Estocolmo, Suecia", "Solitario / Naturaleza", "Ciudad / Invierno"],
    ["Helsinki, Finlandia", "Solitario / Naturaleza", "Ciudad / Invierno"],
    ["Oslo, Noruega", "Solitario / Naturaleza", "Ciudad / Invierno"],
    ["Copenhague, Dinamarca", "Pareja / Cultura", "Ciudad / Cultura"],
    ["Reykjavik, Islandia", "Solitario / Naturaleza", "Naturaleza / Aventura"],
    ["Ginebra, Suiza", "Familia / Cultura", "Ciudad / Naturaleza"],
    ["Ámsterdam, Países Bajos", "Solitario / Cultura", "Ciudad / Cultura"],
    ["Kitzbühel, Austria", "Pareja / Familia", "Nieve / Ski"],
    ["Quebec, Canadá", "Familia / Solitario", "Ciudad / Invierno"]
]

# Estaciones del año
temporadas = ["Primavera", "Verano", "Otoño", "Invierno"]

# Crear combinaciones de cada ciudad con todas las estaciones
data_completa = []

for ciudad, perfil, clasificacion in data_base:
    for temporada in temporadas:
        data_completa.append([ciudad, temporada, perfil, clasificacion])

# Crear DataFrame
df = pd.DataFrame(data_completa, columns=["Ciudad", "Temporada", "Perfil_viajero", "Clasificacion_destino"])

# Guardar como CSV
df.to_csv("../Modelo_recomendaci-n_Agencia_de_viajes/data/processed/perfiles_completos_destinos_temporada.csv", index=False)

print("✅ CSV 'perfiles_completos_destinos_temporada.csv' creado con TODAS las ciudades y estaciones.")