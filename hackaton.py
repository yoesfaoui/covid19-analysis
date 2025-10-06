import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error

# Charger les données
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master


df = pd.read_csv(url)
# Agréger par pays
df_country = df.groupby("Country/Region").sum()

# Supprimer les colonnes inutiles si elles existent
cols_to_drop = [col for col in ["Lat", "Long", "Province/State"] if col in df_country.columns]
df_country = df_country.drop(columns=cols_to_drop, errors="ignore")