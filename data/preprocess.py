import pandas as pd
import os


def preprocess_files():
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
  
  ruta_absoluta_entrenos = "data/entrenos/"
  ruta_absoluta_partidos = "data/partidos/"

  dfs, fechas = [], []
  for filename in os.listdir(ruta_absoluta_entrenos):  #Recorremos toda la carpeta con todos los ficheros
    df = pd.read_csv(f"{ruta_absoluta_entrenos}{filename}", header=9) #Leemos el fichero en cuestion
    df.drop_duplicates(subset=['Player Name'], keep='first', inplace=True) #Eliminamos los jugadores duplicaod
    df = df[df["Position Name"] != "Goal Keeper"] #Nos quedamos con los jugadores de campo solo
    df["Position Name"] = df["Position Name"].apply(lambda x: pos_dict[x]) #Cambiamos las posiciones
    df["Nombre"] = df["Player Name"].apply(lambda x: x.split(" ")[0])   
    
    apellidos = []
    for idx, row in df.iterrows():
      if ((row["Player Name"].split(" ")[1] == "IBARRA") | (row["Player Name"].split(" ")[1] == "MEDINA")):
        apellido = row["Player Name"].split(" ")[0][:3] + "."+ row["Player Name"].split(" ")[1]
        apellidos.append(apellido)
      else:
        apellidos.append(row["Player Name"].split(" ")[1])
    df["Apellido"] = apellidos 
    if filename == 'ctr-report-ent-109.csv':
      df.Date = '20/06/2024'
    elif filename == 'ctr-report-ent-114.csv':
      df.Date = '25/06/2024'
    elif filename == 'ctr-report-ent-117.csv':
      df.Date = '27/06/2024'
    elif filename == 'ctr-report-02-jul-0408-p-m.csv':
      df.Date = '02/07/2024'
    if df.Date[0] in fechas:
      df["Sesion"] = "Tarde"
    else:
      df["Sesion"] = "Mañana"
      fechas.append(df.Date[0])
    df["Partido/Entreno"] = "Entreno"
    dfs.append(df)
    print(filename, df.Date[0], df.shape)
    
  for filename in os.listdir(ruta_absoluta_partidos):  #Recorremos toda la carpeta con todos los ficheros
    # df_aux = pd.read_csv(f"./temporada24-25/{filename}", header=2) #Leemos el fichero en cuestion
    # print(df_aux)
    df = pd.read_csv(f"{ruta_absoluta_partidos}{filename}", header=9) #Leemos el fichero en cuestion
    df.drop_duplicates(subset=['Player Name'], keep='first', inplace=True) #Eliminamos los jugadores duplicaod
    df = df[df["Position Name"] != "Goal Keeper"] #Nos quedamos con los jugadores de campo solo
    df["Position Name"] = df["Position Name"].apply(lambda x: pos_dict[x]) #Cambiamos las posiciones
    df["Nombre"] = df["Player Name"].apply(lambda x: x.split(" ")[0])   
    
    apellidos = []
    for idx, row in df.iterrows():
      if ((row["Player Name"].split(" ")[1] == "IBARRA") | (row["Player Name"].split(" ")[1] == "MEDINA")):
        apellido = row["Player Name"].split(" ")[0][:3] + "."+ row["Player Name"].split(" ")[1]
        apellidos.append(apellido)
      else:
        apellidos.append(row["Player Name"].split(" ")[1])
    df["Apellido"] = apellidos
    if filename == 'ctr-report-copa-ecu1-olmedo-vs-idv.csv':
      df.Date = '31/07/2024'
    elif filename == 'ctr-report-2f2barcelona-vs-idv.csv':
      df.Date = '10/08/2024'
    
    if df.Date[0] in fechas:
      df["Sesion"] = "Tarde"
    else:
      df["Sesion"] = "Mañana"
      fechas.append(df.Date[0])
    df["Partido/Entreno"] = "Partido"

    dfs.append(df)
    print(filename, df.Date[0], df.shape)
  result = pd.concat(dfs, ignore_index=True)
  result['Date'] = pd.to_datetime(result['Date'], format='%d/%m/%Y')
  
  # Create separate columns for month, day, and year
  result['Dia'] = result['Date'].dt.day
  result['Mes'] = result['Date'].dt.month
  result['Año'] = result['Date'].dt.year
  
  month_dict = {
    1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril',
    5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
    9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
  }

  # Map the month number to the month name
  result['Mes'] = result['Mes'].map(month_dict)
  earliest_date = result['Date'].min()

  # Calculate the number of weeks between each date and the earliest date
  result['Semana'] = ((result['Date'] - earliest_date).dt.days // 7) + 1
  result = result.rename(columns={'Position Name': 'Posicion'})
  
  result.rename(columns = {"Partido/Entreno": "PartidoEntreno"}, inplace=True)
  result['HSR %'] = (result["Velocity Band 6 Total Distance"] / result['Total Distance'].sum()) * 100
  result["VHSR"] = result["Velocity Band 7 Total Distance"] + result["Velocity Band 8 Total Distance"] 
  result['VHSR %'] = (result["VHSR"] / result['Total Distance'].sum()) * 100
  result["AccMayoresGen2"] = result["Acceleration B2-3 Average Efforts (Session) (Gen 2)"] + result["Acceleration B3 Efforts (Gen 2)"]
  result['TotalMinutes'] = result['Total Duration'].apply(lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1]) + int(x.split(':')[2]) / 60)
  result["Relative Distance"] = result["Total Distance"] / result["TotalMinutes"]
  result['Band5 %'] = (result["Velocity Band 5 Total Distance"] / result['Total Distance']) * 100
  result['Band6 %'] = (result["Velocity Band 6 Total Distance"] / result['Total Distance']) * 100
  result['Band7 %'] = (result["Velocity Band 7 Total Distance"] / result['Total Distance']) * 100
  result['Band8 %'] = (result["Velocity Band 8 Total Distance"] / result['Total Distance']) * 100
  result.to_excel("../data.xlsx", index=False)
  return result

preprocess_files()