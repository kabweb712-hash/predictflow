import pandas as pd
import os
from src.utils.logger import setup_logger

# Initialiser le logger au début du module
logger = setup_logger()


def load_data(filepath: str) -> pd.DataFrame:
    """Charge le dataset Telco et retourne un DataFrame propre."""
    logger.info(f"Tentative de chargement du fichier : {filepath}")
    
    try:
        if not os.path.exists(filepath):
            logger.error(f"Dataset introuvable : {filepath}")
            raise FileNotFoundError(f"❌ Dataset introuvable : {filepath}")
        
        df = pd.read_csv(filepath)
        logger.debug(f"Fichier CSV lu avec succès. Shape brute : {df.shape}")
        
        df = fix_total_charges(df)
        logger.info(f"✅ Dataset chargé : {df.shape[0]} lignes, {df.shape[1]} colonnes")
        
        return df
    
    except FileNotFoundError as e:
        logger.error(f"Erreur FileNotFoundError : {e}")
        return None
    
    except pd.errors.EmptyDataError:
        logger.error("Le fichier CSV est vide")
        return None
    
    except Exception as e:
        logger.critical(f"Erreur inattendue lors du chargement : {e}")
        return None


def fix_total_charges(df: pd.DataFrame) -> pd.DataFrame:
    """Convertit TotalCharges en float (problème connu du dataset Telco)."""
    logger.debug("Conversion de la colonne TotalCharges en float")
    
    before_count = df['TotalCharges'].isna().sum()
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    after_count = df['TotalCharges'].isna().sum()
    
    if after_count > before_count:
        logger.warning(f"{after_count - before_count} valeurs TotalCharges converties en NaN")
    
    return df


def get_basic_info(df: pd.DataFrame) -> None:
    """Affiche les informations de base sur le DataFrame."""
    logger.info(f"Dataset : {df.shape[0]} lignes, {df.shape[1]} colonnes")
    logger.debug(f"Colonnes : {list(df.columns)}")
    
    missing = df.isnull().sum()[df.isnull().sum() > 0]
    if len(missing) > 0:
        logger.warning(f"Valeurs manquantes détectées :\n{missing}")


def get_column_names(df: pd.DataFrame) -> list:
    colonnes = list(df.columns)
    logger.debug(f"{len(colonnes)} colonnes récupérées")
    return colonnes


def get_first_client(df: pd.DataFrame) -> dict:
    """Retourne le premier client sous forme de dictionnaire."""
    premier_client = df.iloc[0].to_dict()
    logger.debug("Premier client extrait")
    return premier_client


def get_unique_values(df: pd.DataFrame, column: str) -> set:
    """Retourne les valeurs uniques d'une colonne donnée."""
    unique_vals = set(df[column].unique())
    logger.debug(f"Colonne '{column}' : {len(unique_vals)} valeurs uniques")
    return unique_vals


def churn_par_contrat(df: pd.DataFrame) -> dict:
    """Calcule le taux de churn par type de contrat."""
    logger.info("Calcul du taux de churn par type de contrat")
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
    
    logger.debug(f"Stats churn calculées pour {len(resume)} types de contrats")
    return resume


def filter_at_risk_clients(df: pd.DataFrame) -> pd.DataFrame:
    """Retourne les clients à risque de churn."""
    logger.info("Filtrage des clients à risque")
    
    mask = (
        (df["tenure"] < 12) &
        (df["Contract"] == "Month-to-month") &
        (df["TechSupport"] == "No")
    )
    at_risk = df[mask]
    logger.warning(f"🚨 {len(at_risk)} clients à risque détectés")
    
    return at_risk


if __name__ == "__main__":
    logger.info("=== Démarrage du script loader.py ===")
    
    df = load_data("data/telco_churn.csv")

    if df is None:
        logger.critical("⛔ Impossible de continuer sans données")
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
    
    logger.info("=== Script terminé avec succès ===")
