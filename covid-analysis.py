import pandas as pd
import matplotlib.pyplot as plt

url_confirmed = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
url_deaths = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
url_recovered = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"

df_confirmed=pd.read_csv(url_confirmed)
df_deaths=pd.read_csv(url_deaths)
df_recovered=pd.read_csv(url_recovered)

"""print(df.head())"""
"""print(df.columns)"""

#on suprime les colonnes comme latitude et longitude car inutiles pour notre analyse et groupement par pays
df_confirmed=df_confirmed.groupby("Country/Region").sum().drop(columns=["Lat","Long"])
df_deaths=df_deaths.groupby("Country/Region").sum().drop(columns=["Lat","Long"])
df_recovered=df_recovered.groupby("Country/Region").sum().drop(columns=["Lat","Long"])

#print(df_country.head())

#on choisit les pays

pays=["France","Italy","Germany","Spain","US"]

#print(data.head())
#tracer les courbes
plt.figure(figsize=(12,6))
for p in pays:
   
    confirmed=df_confirmed.loc[p].iloc[2:]
    deaths=df_deaths.loc[p].iloc[2:]
    recovered=df_recovered.loc[p].iloc[2:]

    confirmed.index=pd.to_datetime(confirmed.index)
    deaths.index=pd.to_datetime(deaths.index)
    recovered.index=pd.to_datetime(recovered.index)
   
    plt.plot(confirmed.index,confirmed.values,label=f"{p} Confirmed", linewidth=1)
    plt.plot(deaths.index,deaths.values,label=f"{p} Deaths", linestyle='--', linewidth=1)
    plt.plot(recovered.index,recovered.values,label=f"{p} Recovered", linestyle=':', linewidth=1)
# personnalisation du graphique

plt.title("Covid-19: Cas confirmés, Décès et Rétablis")
plt.xlabel("la date")
plt.ylabel("Nomre de cas")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
