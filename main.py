import pandas as pd
from src.loader import load_data, get_basic_info
from src.preprocessor import drop_useless_columns, fix_total_charges, handle_missing_values, encode_target
from src.stats import churn_rate
from src.utils.logger import setup_logger

logger = setup_logger()

def main():
    # 1️⃣ Charger les données
    df = load_data("data/raw/telco_churn.csv")
    if df is None:
        logger.critical("Échec du chargement des données. Fin du programme.")
        return

    # 2️⃣ Afficher les infos de base
    get_basic_info(df)

    # 3️⃣ Prétraitement
    df = drop_useless_columns(df)
    df = fix_total_charges(df)
    df = handle_missing_values(df)
    df = encode_target(df)

    # 4️⃣ Statistiques
    rate = churn_rate(df)
    logger.info(f"Taux de churn : {rate}%")

if __name__ == "__main__":   # ← à la racine, pas dans main()
    main()