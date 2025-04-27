import pandas as pd

# Definimos todos los datos
data = [
    # Primavera
    ["Tokyo, Japón", "Primavera", "Solitario / Cultura", "Ciudad / Cultura"],
    ["París, Francia", "Primavera", "Pareja / Cultura", "Ciudad / Romántico"],
    ["Barcelona, España", "Primavera", "Pareja / Amigos", "Ciudad / Playa / Cultura"],
    ["Roma, Italia", "Primavera", "Pareja / Cultura", "Ciudad / Cultura / Romántico"],
    ["Madrid, España", "Primavera", "Solitario / Pareja / Cultura", "Ciudad / Cultura"],
    ["Amsterdam, Países Bajos", "Primavera", "Solitario / Pareja / Amigos", "Ciudad / Cultura"],
    ["Lisboa, Portugal", "Primavera", "Pareja / Familia", "Ciudad / Cultura / Playa"],
    ["Estambul, Turquía", "Primavera", "Solitario / Cultura", "Ciudad / Cultura / Histórico"],
    ["Buenos Aires, Argentina", "Primavera", "Familia / Cultura", "Ciudad / Cultura"],
    ["Seúl, Corea del Sur", "Primavera", "Solitario / Cultura", "Ciudad / Cultura"],
    
    # Verano
    ["Cancún, México", "Verano", "Pareja / Familia / Amigos", "Playa / Relax"],
    ["Honolulu, Hawái, EE. UU.", "Verano", "Pareja / Familia / Solitario", "Playa / Naturaleza"],
    ["Río de Janeiro, Brasil", "Verano", "Pareja / Amigos", "Playa / Ciudad / Fiesta"],
    ["Sydney, Australia", "Verano", "Familia / Solitario", "Playa / Ciudad / Naturaleza"],
    ["Bali, Indonesia", "Verano", "Pareja / Solitario", "Playa / Relax / Cultura"],
    ["Dubai, Emiratos Árabes Unidos", "Verano", "Pareja / Familia", "Ciudad / Lujo"],
    ["Marrakech, Marruecos", "Verano", "Pareja / Solitario", "Cultura / Histórico"],
    ["Lima, Perú", "Verano", "Solitario / Cultura", "Ciudad / Cultura / Histórico"],
    ["Cartagena, Colombia", "Verano", "Pareja / Amigos / Familia", "Playa / Cultura"],
    ["Mykonos, Grecia", "Verano", "Pareja / Amigos", "Playa / Fiesta / Relax"],
    
    # Otoño
    ["Nueva York, EE. UU.", "Otoño", "Solitario / Pareja / Cultura", "Ciudad / Cultura"],
    ["Montreal, Canadá", "Otoño", "Familia / Solitario", "Ciudad / Naturaleza"],
    ["Vancouver, Canadá", "Otoño", "Solitario / Naturaleza", "Naturaleza / Ciudad"],
    ["Praga, República Checa", "Otoño", "Pareja / Cultura", "Ciudad / Cultura / Romántico"],
    ["Londres, Reino Unido", "Otoño", "Solitario / Cultura", "Ciudad / Cultura"],
    ["Berlín, Alemania", "Otoño", "Solitario / Cultura", "Ciudad / Cultura / Historia"],
    ["Buenos Aires, Argentina", "Otoño", "Familia / Cultura", "Ciudad / Cultura"],
    ["San Francisco, EE. UU.", "Otoño", "Solitario / Innovación", "Ciudad / Cultura / Tecnología"],
    ["Ciudad de México, México", "Otoño", "Cultura / Familia", "Ciudad / Cultura"],
    ["Zurich, Suiza", "Otoño", "Solitario / Naturaleza", "Ciudad / Naturaleza"],
    
    # Invierno
    ["Moscú, Rusia", "Invierno", "Solitario / Cultura", "Ciudad / Cultura / Invierno"],
    ["Estocolmo, Suecia", "Invierno", "Solitario / Naturaleza", "Ciudad / Invierno"],
    ["Helsinki, Finlandia", "Invierno", "Solitario / Naturaleza", "Ciudad / Invierno"],
    ["Oslo, Noruega", "Invierno", "Solitario / Naturaleza", "Ciudad / Invierno"],
    ["Copenhague, Dinamarca", "Invierno", "Pareja / Cultura", "Ciudad / Cultura"],
    ["Reykjavik, Islandia", "Invierno", "Solitario / Naturaleza", "Naturaleza / Aventura"],
    ["Ginebra, Suiza", "Invierno", "Familia / Cultura", "Ciudad / Naturaleza"],
    ["Ámsterdam, Países Bajos", "Invierno", "Solitario / Cultura", "Ciudad / Cultura"],
    ["Kitzbühel, Austria", "Invierno", "Pareja / Familia", "Nieve / Ski"],
    ["Quebec, Canadá", "Invierno", "Familia / Solitario", "Ciudad / Invierno"],
]

# Creamos el DataFrame
df_perfiles = pd.DataFrame(data, columns=["Ciudad", "Temporada", "Perfil_viajero", "Clasificacion_destino"])

# Guardamos el CSV
df_perfiles.to_csv("../Modelo_recomendaci-n_Agencia_de_viajes/data/processed/perfiles_completos_destinos_temporada.csv", index=False)

print("✅ CSV 'perfiles_completos_destinos_temporada.csv' creado con éxito.")