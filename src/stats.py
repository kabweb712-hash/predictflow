"""
PredictFlow — Module de statistiques descriptives.
"""

import json
import pandas as pd
from src.exceptions import StatsError


class StatsAnalyzer:
    """Calcule et exporte les statistiques du dataset."""

    def __init__(self, df):
        self.df = df

    def taux_churn(self):
        """Calcule le taux de churn en %."""
        if "Churn" not in self.df.columns:
            raise StatsError("Colonne 'Churn' manquante.")
        total = len(self.df)
        churned = self.df["Churn"].sum()
        return round(churned / total * 100, 2) if total > 0 else 0

    def stats_charges(self):
        """Charges moyennes churners vs actifs."""
        if "MonthlyCharges" not in self.df.columns:
            raise StatsError("Colonne 'MonthlyCharges' manquante.")
        churners = self.df[self.df["Churn"] == 1]["MonthlyCharges"]
        actifs = self.df[self.df["Churn"] == 0]["MonthlyCharges"]
        return {
            "churners": round(churners.mean(), 2),
            "actifs": round(actifs.mean(), 2)
        }

    def stats_tenure(self):
        """Statistiques d'ancienneté."""
        if "tenure" not in self.df.columns:
            raise StatsError("Colonne 'tenure' manquante.")
        return {
            "min": int(self.df["tenure"].min()),
            "max": int(self.df["tenure"].max()),
            "moyenne": round(float(self.df["tenure"].mean()), 2)
        }

    def resume_complet(self):
        """Rassemble toutes les stats dans un dict."""
        return {
            "taux_churn": self.taux_churn(),
            "stats_charges": self.stats_charges(),
            "stats_tenure": self.stats_tenure()
        }

    def exporter_json(self, chemin="data/stats.json"):
        """Exporte le résumé complet en JSON."""
        stats = self.resume_complet()
        with open(chemin, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=4)
        print(f"✅ Stats exportées → {chemin}")


# ─────────────────────────────────────────
if __name__ == "__main__":
    from src.loader import DataLoader
    from src.preprocessor import Preprocessor

    loader = DataLoader()
    loader.charger()

    prep = Preprocessor(loader.df)
    df_clean = prep.pipeline_complet()

    stats = StatsAnalyzer(df_clean)
    stats.exporter_json()
