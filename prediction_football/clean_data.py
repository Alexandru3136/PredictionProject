import pandas as pd

# Încărcăm datele
df = pd.read_csv("meciuri.csv")

# Eliminăm meciurile care nu s-au jucat
df = df[df["Status"] == "FINISHED"]

# Transformăm scorurile în două coloane noi
df["Home Goals"] = df["Score"].apply(lambda x: eval(x).get("home", 0) if isinstance(x, str) else 0)
df["Away Goals"] = df["Score"].apply(lambda x: eval(x).get("away", 0) if isinstance(x, str) else 0)

# Salvăm datele curățate
df.to_csv("meciuri_curate.csv", index=False)
print("Datele curățate au fost salvate în meciuri_curate.csv")
