import requests
import pandas as pd

# API Keys - înlocuiește cu ale tale
FOOTBALL_API_KEY = "0276922ae2d6496eb831c9795f7e9806"
ODDS_API_KEY = "6bdf4cd25864a80a4347fae0be9f833d"

# Funcție pentru a lua meciurile dintr-o competiție
def get_matches(league_id):
    url = f"https://api.football-data.org/v4/competitions/{league_id}/matches"
    headers = {"X-Auth-Token": FOOTBALL_API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        matches = []
        for match in data["matches"]:
            matches.append({
                "Home Team": match["homeTeam"]["name"],
                "Away Team": match["awayTeam"]["name"],
                "Date": match["utcDate"],
                "Status": match["status"],
                "Score": match.get("score", {}).get("fullTime", {})
            })
        return pd.DataFrame(matches)
    else:
        print("Eroare la obținerea datelor:", response.text)
        return None

# Testare
if __name__ == "__main__":
    df = get_matches("PL")  # "PL" este codul pentru Premier League
    print(df.head())  # Afișează primele 5 meciuri

df.to_csv("meciuri.csv", index=False)
print("Datele au fost salvate în meciuri.csv")
