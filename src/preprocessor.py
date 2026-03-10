# preprocessor.py — Nettoyage et préparation des données Telco
import pandas as pd
from src.utils.logger import setup_logger

logger = setup_logger()


def drop_useless_columns(df):
    """Supprime les colonnes inutiles du dataset."""
    useless_cols = ['customerID']
    logger.debug(f"Suppression des colonnes inutiles : {useless_cols}")
    df = df.drop(columns=useless_cols, errors='ignore')
    logger.info(f"✅ Colonnes supprimées : {useless_cols} | Shape : {df.shape}")
    return df


def fix_total_charges(df):
    """Convertit TotalCharges en float et remplace les espaces par NaN."""
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    count = df['TotalCharges'].isna().sum()
    logger.debug(f"Nombre de valeurs NaN dans TotalCharges après conversion : {count}")
    logger.info(f"✅ TotalCharges converti en float | {count} NaN détectés")
    return df


def handle_missing_values(df):
    """Supprime toutes les lignes contenant des valeurs manquantes."""
    before_count = df.isnull().sum().sum()
    df = df.dropna()
    after_count = df.isnull().sum().sum()
    logger.info(f"✅ Lignes supprimées | {before_count} → {after_count} NaN restants | Shape : {df.shape}")
    return df


def encode_target(df):
    """Encode la variable cible Churn en binaire (Yes=1, No=0)."""
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
    logger.info("✅ Variable cible Churn encodée en binaire")
    return df