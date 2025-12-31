import pandas as pd
import sys
sys.stdout.reconfigure(encoding="utf-8")
# import os
# print("Script location:", os.path.dirname(__file__))
# print("Working directory:", os.getcwd())

# print(pd.__version__)
#^Series
#In pandas, a Series is a one-dimensional labeled array.
#Think of it as a single column of data with labels (indexes).

# data = [100.3,102.1,104.4,120.1]
# series = pd.Series(data, index=[1,2,3,4])
# series.loc[4] = 200

# print(series.iloc[0])

# print(series[series<105])

# calories = {
#   "Day 1": 1750,
#   "Day 2": 2100,
#   "Day 3": 1700
# }

# series = pd.Series(calories)
# series.loc["Day 3"] += 500

# print(series)
# print(series.loc["Day 2"])

#===================================DATAFRAMES===========================

# data = {
#   "Name": ["Spongebob", "Patrick", "Squidward"],
#   "Age": [30,35,50],
#   "Employment": ["cook", "chiller", "cashier"]
# }

# df = pd.DataFrame(data, index=["Employee 1","Employee 2","Employee 3"])

# print(df)
# df.loc["Employee 1","Age"] = 43
# print(df.loc["Employee 1"]["Age"])

#New column
# df["teams"] = ["Arsenal", "Leeds", "Celtic"]

# #New Row
# new_rows = pd.DataFrame([{"Name":"Sandy","Age": 28,"teams":"Hearts","Employment": "Engineer"},
#                         {"Name":"Eugene","Age": 48,"teams":"Rangers","Employment": "Manager"}], 
#                        index=["Employee 4","Employee 5"])
# df = pd.concat([df, new_rows])

# print(df)
#=================================CSV FILE==============================================
# df = pd.read_csv("sample_data1.csv")
# df = pd.read_csv(
#     r"C:\Users\Ben\Desktop\gif\python-tutorials\Pandas\sample_data1.csv"
# )
# print(df)

#=================================JSON FILE==============================================
# df = pd.read_json(
#     r"C:\Users\Ben\Desktop\gif\python-tutorials\Pandas\sample_data2.json"
# )

# print(df)

#===============================SELECTION============================================
#&BY COLUMN

df = pd.read_csv(
    # r"C:\Users\Ben\Desktop\gif\python-tutorials\Pandas\sample_data1.csv", index_col="Name")
    r"C:\Users\Ben\Desktop\gif\python-tutorials\Pandas\sample_data1.csv")
# print(df["Name"].to_string())
# print(df["Height"].to_string())
# print(df["Weight"].to_string())
# print(df[['Name','Height']]) 

#&BY ROW

# print(df)
# print(df.loc["Onix"])
# print(df.loc["Lapras",["Height","Type1"]])
# print(df.loc["Lapras": "Zapdos"])
# print(df.iloc[0:11:2, 0:3])

# pokemon = input("Enter a pokemon name: ")

# try:
#   print(df.loc[pokemon])
# except: KeyError
# print(f'Pokemon ${pokemon} not found')


tall_pokemon = df[df["Height"] >=2]
heavy_pokemon = df[df["Weight"]>100]
water_pokemon = df[df["Type1"]=="Water"]

# print(tall_pokemon)
# print(heavy_pokemon)
# print(water_pokemon)

# print(water_pokemon.mean(numeric_only=True))
# print(water_pokemon.sum(numeric_only=True))
# print(water_pokemon.min(numeric_only=True))
# print(water_pokemon.max(numeric_only=True))
# print(water_pokemon.count(numeric_only=True))

# print(df["Height"].mean(numeric_only=True))
# print(df["Height"].sum(numeric_only=True))

# GROUP BY

# group = df.groupby("Type1")
# print(group["Height"].mean())
# print(group["Height"].sum())
# print(group["Height"].min())
# print(group["Height"].max())
# print(group["Height"].count())

#=================================DATA CLEANING==============================
# df = df.drop(columns=["Legendary", "No"])
# df = df.dropna(subset=["Type2"])
# df = df.fillna({"Type2": "None"})

# df["Type1"] = df["Type1"].replace({"Grass": "GRASS", "Fire": "FIRE", "Water": "WATER"})

# df["Name"] = df["Name"].str.lower()
# df["Legendary"] = df["Legendary"].astype(bool)

print(df.to_string())