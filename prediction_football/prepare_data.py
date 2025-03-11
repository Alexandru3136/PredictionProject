import pandas as pd

# Încărcăm datele curățate
df = pd.read_csv("meciuri_curate.csv")

# Creăm eticheta (ce vrem să prezicem)
df["Winner"] = df.apply(lambda row: 1 if row["Home Goals"] > row["Away Goals"] else (2 if row["Home Goals"] < row["Away Goals"] else 0), axis=1)

# Selectăm caracteristicile relevante
features = df[["Home Goals", "Away Goals"]]
labels = df["Winner"]

# Salvăm datele pentru antrenare
features.to_csv("features.csv", index=False)
labels.to_csv("labels.csv", index=False)
print("Datele pentru antrenare au fost salvate.")
