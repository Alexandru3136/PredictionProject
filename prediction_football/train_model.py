import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Încărcăm datele pentru antrenare
features = pd.read_csv("features.csv")
labels = pd.read_csv("labels.csv")

# Împărțim datele în seturi de antrenare și testare (80% antrenare, 20% testare)
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Construim modelul RandomForest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train.values.ravel())  # Antrenăm modelul

# Facem predicții pe setul de testare
predictions = model.predict(X_test)

# Evaluăm acuratețea
accuracy = accuracy_score(y_test, predictions)
print(f"Acuratețea modelului: {accuracy:.2f}")

# Salvăm modelul antrenat
import joblib
joblib.dump(model, "predictor_model.pkl")
print("Modelul a fost salvat.")
