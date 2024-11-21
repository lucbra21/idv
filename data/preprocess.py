import pandas as pd
import os


import pandas as pd
import os
from typing import List, Dict, Tuple

def preprocess_files() -> pd.DataFrame:
    # Definir tipos de datos específicos para optimizar memoria
    dtypes = {
        'Player Name': 'category',
        'Position Name': 'category',
        'Nombre': 'category',
        'Apellido': 'category',
        'Sesion': 'category',
        'Partido/Entreno': 'category'
    }
    
    pos_dict = {
        "Defensa Central": "DEF CEN",
        "Defensa Lateral": "DEF LAT",
        "Medio Centro": "MED",
        "Interior": "MED INT",
        "Delantero": "DEL",
        "Extremo": "DEL EXT",
        "Arquero": "POR", 
        "Goal Keeper": "POR"
    }

    # Mapeo de fechas para evitar condicionales repetitivos
    date_mapping = {
        'ctr-report-ent-109.csv': '20/06/2024',
        'ctr-report-ent-114.csv': '25/06/2024',
        'ctr-report-ent-117.csv': '27/06/2024',
        'ctr-report-02-jul-0408-p-m.csv': '02/07/2024',
        'ctr-report-copa-ecu1-olmedo-vs-idv.csv': '31/07/2024',
        'ctr-report-2f2barcelona-vs-idv.csv': '10/08/2024'
    }

    def process_single_file(filepath: str, filename: str, is_partido: bool) -> Tuple[pd.DataFrame, str]:
        # Leer solo las columnas necesarias
        needed_cols = ['Player Name', 'Position Name', 'Date', 'Total Distance', 
                      'Velocity Band 6 Total Distance', 'Velocity Band 7 Total Distance',
                      'Velocity Band 8 Total Distance', 'Total Duration',
                      'Velocity Band 5 Total Distance', 'Acceleration B2-3 Average Efforts (Session) (Gen 2)',
                      'Acceleration B3 Efforts (Gen 2)']
        
        df = pd.read_csv(filepath, header=9, usecols=needed_cols, dtype=dtypes)
        
        # Procesar el DataFrame
        df = df[df["Position Name"] != "Goal Keeper"].copy()
        df.drop_duplicates(subset=['Player Name'], keep='first', inplace=True)
        
        # Crear todas las columnas nuevas de una vez
        new_cols = {
            'Position Name': df['Position Name'].map(pos_dict),
            'Nombre': df['Player Name'].str.split().str[0],
            'Apellido': df.apply(lambda x: f"{x['Player Name'].split()[0][:3]}.{x['Player Name'].split()[1]}" 
                               if x['Player Name'].split()[1] in ['IBARRA', 'MEDINA'] 
                               else x['Player Name'].split()[1], axis=1),
            'Partido/Entreno': 'Partido' if is_partido else 'Entreno'
        }
        
        # Asignar fecha del mapeo si existe
        if filename in date_mapping:
            df['Date'] = date_mapping[filename]
            
        # Concatenar todas las columnas nuevas de una vez
        df = pd.concat([df, pd.DataFrame(new_cols)], axis=1)
        
        return df, df.Date.iloc[0]

    # Procesar archivos
    dfs = []
    fechas = set()  # Usar set es más eficiente que lista para búsquedas
    
    # Procesar entrenos
    for filename in os.listdir("data/entrenos/"):
        df, fecha = process_single_file(f"data/entrenos/{filename}", filename, False)
        df['Sesion'] = "Tarde" if fecha in fechas else "Mañana"
        fechas.add(fecha)
        dfs.append(df)
        
    # Procesar partidos
    for filename in os.listdir("data/partidos/"):
        df, fecha = process_single_file(f"data/partidos/{filename}", filename, True)
        df['Sesion'] = "Tarde" if fecha in fechas else "Mañana"
        fechas.add(fecha)
        dfs.append(df)

    # Concatenar y procesar resultado final
    result = pd.concat(dfs, ignore_index=True)
    result['Date'] = pd.to_datetime(result['Date'], format='%d/%m/%Y')
    
    # Crear todas las columnas de fecha de una vez
    date_cols = pd.concat([
        result['Date'].dt.day.rename('Dia'),
        result['Date'].dt.month.rename('Mes'),
        result['Date'].dt.year.rename('Año')
    ], axis=1)
    
    result = pd.concat([result, date_cols], axis=1)
    
    # Calcular métricas en una sola operación
    total_distance = result['Total Distance'].sum()
    result['TotalMinutes'] = result['Total Duration'].str.split(':').apply(
        lambda x: int(x[0]) * 60 + int(x[1]) + int(x[2]) / 60)
    
    metrics = {
        'HSR %': (result["Velocity Band 6 Total Distance"] / total_distance) * 100,
        'VHSR': result["Velocity Band 7 Total Distance"] + result["Velocity Band 8 Total Distance"],
        'Relative Distance': result["Total Distance"] / result["TotalMinutes"],
        'Band5 %': (result["Velocity Band 5 Total Distance"] / result["Total Distance"]) * 100,
        'Band6 %': (result["Velocity Band 6 Total Distance"] / result["Total Distance"]) * 100,
        'Band7 %': (result["Velocity Band 7 Total Distance"] / result["Total Distance"]) * 100,
        'Band8 %': (result["Velocity Band 8 Total Distance"] / result["Total Distance"]) * 100
    }
    
    result = pd.concat([result, pd.DataFrame(metrics)], axis=1)
    
    # Guardar y retornar
    result.to_excel("../data.xlsx", index=False)
    return result

preprocess_files()