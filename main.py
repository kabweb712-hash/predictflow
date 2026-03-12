"""
PredictFlow — Pipeline principal.
"""

from src.loader import DataLoader
from src.preprocessor import Preprocessor
from src.stats import StatsAnalyzer
from src.utils.logger import setup_logger

logger = setup_logger()


def main():
    logger.info("=== Démarrage PredictFlow ===")

    # 1. Charger
    loader = DataLoader()
    loader.charger().inspecter()

    # 2. Prétraiter
    prep = Preprocessor(loader.df)
    df_clean = prep.pipeline_complet()

    # 3. Sauvegarder le dataset propre
    df_clean.to_csv("data/processed/telco_clean.csv", index=False)
    logger.info("✅ Dataset propre sauvegardé")

    # 4. Statistiques + export JSON
    stats = StatsAnalyzer(df_clean)
    stats.exporter_json()

    logger.info("=== PredictFlow terminé ✅ ===")


if __name__ == "__main__":
    main()
