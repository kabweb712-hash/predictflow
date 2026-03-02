import pandas as pd
import os


def load_data(filepath: str) -> pd.DataFrame:
    """Charge le dataset Telco et retourne un DataFrame propre."""
    try:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"❌ Dataset introuvable : {filepath}")
        df = pd.read_csv(filepath)
        df = fix_total_charges(df)
        print(f"✅ Dataset chargé : {df.shape[0]} lignes, {df.shape[1]} colonnes")  
        return df
    
    except FileNotFoundError as e:
        print(e)
        return None
    
    except pd.errors.EmptyDataError:
        print(f"❌ Erreur : Le fichier CSV est vide.")
        return None
    
    except Exception as e:
        print(f"❌ Erreur inattendue : {e}")
        return None



def fix_total_charges(df: pd.DataFrame) -> pd.DataFrame:
    """Convertit TotalCharges en float (problème connu du dataset Telco)."""
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    return df


def get_basic_info(df: pd.DataFrame) -> None:
    """Affiche les informations de base sur le DataFrame."""
    print(f"✅ Dataset chargé : {df.shape[0]} lignes, {df.shape[1]} colonnes")
    print(f"📋 Colonnes : {list(df.columns)}")
    print(f"❓ Valeurs manquantes :\n{df.isnull().sum()[df.isnull().sum() > 0]}")


def get_column_names(df: pd.DataFrame) -> list:
    colonnes = list(df.columns)
    return colonnes



def get_first_client(df: pd.DataFrame) -> dict:
    """Retourne le premier client sous forme de dictionnaire."""
    premier_client = df.iloc[0].to_dict()
    return premier_client


def get_unique_values(df: pd.DataFrame, column: str) -> set:
    """Retourne les valeurs uniques d'une colonne donnée."""
    return set(df[column].unique())


def churn_par_contrat(df: pd.DataFrame) -> dict:
    """Calcule le taux de churn par type de contrat."""
    resume = {}

    for contrat in df["Contract"].unique():
        sous_ensemble = df[df["Contract"] == contrat]
        total = len(sous_ensemble)
        churned = (sous_ensemble["Churn"] == "Yes").sum()
        resume[contrat] = {
            "total": total,
            "churned": int(churned),
            "taux": round(churned / total * 100, 1)
        }
    return resume


def filter_at_risk_clients(df: pd.DataFrame) -> pd.DataFrame:
    """Retourne les clients à risque de churn."""
    
    mask = (
        (df["tenure"] < 12) &
        (df["Contract"] == "Month-to-month") &
        (df["TechSupport"] == "No")
    )
    return df[mask]


if __name__ == "__main__":
    df = load_data("data/telco_churn.csv")

    if df is None : 
        print("⛔ Impossible de continuer sans données.")
        exit(1)

    colonnes = get_column_names(df)
    print(f"\n📋 {len(colonnes)} colonnes trouvées")

    client = get_first_client(df)
    print(f"\n👤 PREMIER CLIENT :")
    
    for cle, valeur in client.items():
        print(f"  {cle:25} : {valeur}")
    
    print(f"\n🔍 VALEURS UNIQUES :")
    print(f"  Contract       : {get_unique_values(df, 'Contract')}")
    print(f"  InternetService: {get_unique_values(df, 'InternetService')}")
    print(f"  PaymentMethod  : {get_unique_values(df, 'PaymentMethod')}")
    print(f"\n📊 CHURN PAR CONTRAT :")
    
    stats = churn_par_contrat(df)
    for contrat, s in stats.items():
        print(f"  {contrat:20} : {s['total']:4d} clients, "
              f"{s['churned']:4d} churned ({s['taux']}%)")
    
    print(f"\n🚨 CLIENTS À RISQUE :")
    at_risk = filter_at_risk_clients(df)
    print(f"  {len(at_risk)} clients à risque détectés")
    print(at_risk[["tenure", "Contract", "TechSupport", "Churn"]].head(5))
