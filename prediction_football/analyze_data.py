import pandas as pd
import matplotlib.pyplot as plt

# Încărcăm datele curățate
df = pd.read_csv("meciuri_curate.csv")

# Afișăm primele 5 rânduri
print(df.head())

# Statistici generale
print(df.describe())

# Distribuția golurilor
plt.hist(df["Home Goals"], bins=10, alpha=0.5, label="Goluri Acasă")
plt.hist(df["Away Goals"], bins=10, alpha=0.5, label="Goluri Deplasare")
plt.legend()
plt.xlabel("Numărul de goluri")
plt.ylabel("Numărul de meciuri")
plt.title("Distribuția golurilor în meciuri")
plt.show()
