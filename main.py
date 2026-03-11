import pandas as pd
from src.loader import load_data, get_basic_info
from src.preprocessor import drop_useless_columns, fix_total_charges, handle_missing_values, encode_target
from src.utils.logger import setup_logger
from src.stats import churn_rate, average_charges, tenure_stats, contract_distribution

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
    churned_avg, retained_avg = average_charges(df)
    tenure_min, tenure_max, tenure_avg = tenure_stats(df)
    print(f"Taux de churn : {churn_rate(df)}%")
    print(f"Charges moyennes (churners)  : {round(churned_avg, 2)}€")
    print(f"Charges moyennes (fidèles)   : {round(retained_avg, 2)}€")
    print(f"Durée abonnement — min: {tenure_min}m | max: {tenure_max}m | moy: {tenure_avg}m")
    print(f"Distribution contrats :\n{contract_distribution(df)}")

if __name__ == "__main__":
    main()
