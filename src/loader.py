import pandas as pd
import os


def load_data(filepath: str) -> pd.DataFrame:
    """Charge le dataset Telco et retourne un DataFrame propre."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"❌ Dataset introuvable : {filepath}")
    df = pd.read_csv(filepath)
    df = fix_total_charges(df)  
    return df


def fix_total_charges(df: pd.DataFrame) -> pd.DataFrame:
    """Convertit TotalCharges en float (problème connu du dataset Telco)."""
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    return df


def get_basic_info(df: pd.DataFrame) -> None:
    """Affiche les informations de base sur le DataFrame."""
    print(f"✅ Dataset chargé : {df.shape[0]} lignes, {df.shape[1]} colonnes")
    print(f"📋 Colonnes : {list(df.columns)}")
    print(f"❓ Valeurs manquantes :\n{df.isnull().sum()[df.isnull().sum() > 0]}")
