import csv_fetcher
import pandas as pd

csv_paths = csv_fetcher.get_csv_paths('###')

for csv_path in csv_paths:
    career_name = csv_path.split('/')[-1]
    df = pd.read_csv(csv_path)

    print(f"\n== {career_name} ==")
    print("-- Postulantes --")
    print(f"mean score: {round(df['Puntaje'].mean(), 3)}")
    print(f"median score: {df['Puntaje'].median()}")
    print(f"standard deviation: {round(df['Puntaje'].std(), 3)}")
    print(f"min score: {df[df['Puntaje'] > 0]['Puntaje'].min()}")
    print(f"max score: {df['Puntaje'].max()}")
    print(f"Q1: {round(df['Puntaje'].quantile(0.25), 3)}")
    print(f"Q3: {round(df['Puntaje'].quantile(0.75), 3)}")
    print(f"p90: {round(df['Puntaje'].quantile(0.90), 3)}")
    print(f"p95: {round(df['Puntaje'].quantile(0.95), 3)}")
