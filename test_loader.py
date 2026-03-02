import pandas as pd

def load_data(file_path):
    """
    Charge un fichier CSV de manière sécurisée.
    
    Args:
        file_path (str): Chemin vers le fichier CSV
        
    Returns:
        pd.DataFrame ou None: DataFrame si succès, None si échec
    """
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Fichier chargé : {len(df)} lignes")
        return df
    
    except FileNotFoundError:
        print(f"❌ Erreur : Le fichier '{file_path}' est introuvable.")
        return None


# === TESTS ===
if __name__ == "__main__":
    print("🧪 TEST 1 : Fichier qui existe")
    print("-" * 40)
    df1 = load_data("data/telco_churn.csv")
    if df1 is not None:
        print(f"📊 Colonnes : {list(df1.columns[:3])}...")  # Affiche 3 premières colonnes
    print()
    
    print("🧪 TEST 2 : Fichier qui n'existe pas")
    print("-" * 40)
    df2 = load_data("data/fichier_inexistant.csv")
    if df2 is None:
        print("✅ La fonction a bien retourné None")
