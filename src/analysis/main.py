import csv_fetcher
import pandas as pd

csv_paths = csv_fetcher.get_csv_paths('/home/jsanchez/Projects/applicant-scraper/output/unmsm')

for csv_path in csv_paths:
    career_name = csv_path.split('/')[-1]
    df = pd.read_csv(csv_path)
    # applicants
    df = pd.read_csv(csv_path)
    # admitted
    #df = df[df['Observación'] == 'ALCANZO VACANTE']
    admitted = df[df['Observación'] == 'ALCANZO VACANTE']

    # applicants
    # print(f"({round(df['Puntaje'].mean(), 3)}, {df['Puntaje'].median()}, {round(df['Puntaje'].std(), 3)}, {df[df['Puntaje'] > 0]['Puntaje'].min()}, {df['Puntaje'].max()}, {round(df['Puntaje'].quantile(0.25), 3)}, {round(df['Puntaje'].quantile(0.75), 3)}, {round(df['Puntaje'].quantile(0.90), 3)}, {round(df['Puntaje'].quantile(0.95), 3)}) --{career_name[:-4]}")
    # admitted
    #print(f"({round(df['Puntaje'].mean(), 3)}, {df['Puntaje'].median()}, {round(df['Puntaje'].std(), 3)}, {df[df['Puntaje'] > 0]['Puntaje'].min()}, {df['Puntaje'].max()}, {round(df['Puntaje'].quantile(0.25), 3)}, {round(df['Puntaje'].quantile(0.75), 3)}, {round(df['Puntaje'].quantile(0.90), 3)}, {round(df['Puntaje'].quantile(0.95), 3)}) --{career_name[:-4]}")

    print(f"\n== {career_name[:-4]} ==")


    print("-- Postulantes --")

    print(f"applicants: {len(df)}")
    print(f"available seats: {len(admitted)}")

    print(f"\nranking competitiveness: 12")
    print(f"ranking popularity: 2")

    print(f"\napplicants/available seats: {round(len(df) / len(admitted))}")

    print(f"\nmean score: {round(df['Puntaje'].mean(), 3)}")
    print(f"median score: {df['Puntaje'].median()}")
    print(f"min score: {df[df['Puntaje'] > 0]['Puntaje'].min()}")
    print(f"max score: {df['Puntaje'].max()}")
    print(f"Q1: {round(df['Puntaje'].quantile(0.25), 3)}")
    print(f"Q3: {round(df['Puntaje'].quantile(0.75), 3)}")
    print(f"p90: {round(df['Puntaje'].quantile(0.90), 3)}")
    print(f"p95: {round(df['Puntaje'].quantile(0.95), 3)}")
    print(f"standard deviation: {round(df['Puntaje'].std(), 3)}")

    print("\n-- Ingresantes --")
    print(f"mean score: {round(admitted['Puntaje'].mean(), 3)}")
    print(f"median score: {admitted['Puntaje'].median()}")
    print(f"min score: {admitted[admitted['Puntaje'] > 0]['Puntaje'].min()}")
    print(f"max score: {admitted['Puntaje'].max()}")
    print(f"Q1: {round(admitted['Puntaje'].quantile(0.25), 3)}")
    print(f"Q3: {round(admitted['Puntaje'].quantile(0.75), 3)}")
    print(f"p90: {round(admitted['Puntaje'].quantile(0.90), 3)}")
    print(f"p95: {round(admitted['Puntaje'].quantile(0.95), 3)}")
    print(f"standard deviation: {round(admitted['Puntaje'].std(), 3)}")
