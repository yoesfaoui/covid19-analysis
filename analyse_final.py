# Projet d'analyse COVID-19 basé sur les données Johns Hopkins CSSE
# Ce script montre l'évolution des cas, compare plusieurs pays et analyse les nouvelles infections

import pandas as pd
import matplotlib.pyplot as plt

# on récupère les données
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
df = pd.read_csv(url)

# Agréger par pays
df_country = df.groupby("Country/Region").sum()

# Supprimer les colonnes inutiles si elles existent
cols_to_drop = [col for col in ["Lat", "Long", "Province/State"] if col in df_country.columns]
df_country = df_country.drop(columns=cols_to_drop, errors="ignore")

# S’assurer que toutes les colonnes sont numériques
df_country = df_country.apply(pd.to_numeric, errors="coerce")

#  Convertir les colonnes en datetime
df_country.columns = pd.to_datetime(df_country.columns)

# calcul des nouvelles infections quotidiennes
daily_cases = df_country.diff(axis=1)

# liste de pays à analyser
pays = ["France", "Italy", "Germany", "Spain", "US"]


#  Visualisation des données (cas totaux)

plt.figure(figsize=(12,6))
for p in pays:
    data = df_country.loc[p]
    plt.plot(data.index, data.values, label=p, linewidth=1)
plt.title("Évolution des cas COVID-19 (total)")
plt.xlabel("Date")
plt.ylabel("Nombre de cas")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Zoom sur une période récente

start_date = "2021-01-01"
end_date = "2023-03-09"

plt.figure(figsize=(12,6))
for p in pays:
    data = df_country.loc[p][start_date:end_date]
    plt.plot(data.index, data.values, label=p, linewidth=1, marker='o')
plt.title("Évolution des cas COVID-19 (zoom 2021-2023)")
plt.xlabel("Date")
plt.ylabel("Nombre de cas")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

#  Moyenne mobile (smoothing) des nouvelles infections

window = 7  # moyenne sur 7 jours
plt.figure(figsize=(12,6))
for p in pays:
    data = daily_cases.loc[p][start_date:end_date]
    smoothed = data.rolling(window).mean()
    plt.plot(smoothed.index, smoothed.values, label=p, linewidth=1.5)
plt.title("Nouvelles infections COVID-19 (moyenne mobile 7 jours)")
plt.xlabel("Date")
plt.ylabel("Nombre de nouveaux cas")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


 #Comparaison finale : cas totaux vs nouvelles infections

fig, ax1 = plt.subplots(figsize=(12,6))

# Cas totaux (ligne en pointillé)
for p in pays:
    data = df_country.loc[p][start_date:end_date]
    ax1.plot(data.index, data.values, label=f"{p} total", linestyle='--', linewidth=1)

# Nouvelles infections (moyenne mobile)
ax2 = ax1.twinx()
for p in pays:
    data = daily_cases.loc[p][start_date:end_date]
    smoothed = data.rolling(7).mean()
    ax2.plot(smoothed.index, smoothed.values, label=f"{p} new", linewidth=1)

ax1.set_xlabel("Date")
ax1.set_ylabel("Cas totaux")
ax2.set_ylabel("Nouvelles infections (moyenne mobile 7 jours)")
ax1.grid(True)
fig.autofmt_xdate()
fig.tight_layout()
fig.legend(loc="upper left", bbox_to_anchor=(0.1,0.9))
plt.show()
