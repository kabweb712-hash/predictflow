"""
PredictFlow — Module de prétraitement des données.
"""

import pandas as pd
from src.exceptions import PreprocessingError


class BaseProcessor:
    """Classe de base — contient la validation commune."""

    def __init__(self, df):
        self.df = df

    def valider(self):
        """Vérifie que self.df est un DataFrame valide."""
        if self.df is None:
            raise PreprocessingError("Pas de données à traiter.")
        if not isinstance(self.df, pd.DataFrame):
            raise PreprocessingError("Les données doivent être un DataFrame pandas.")


class Preprocessor(BaseProcessor):
    """Nettoie et prépare le dataset Telco."""

    def nettoyer(self):
        """Supprime colonnes inutiles et valeurs manquantes."""
        self.valider()
        self.df = self.df.drop(columns=["customerID"], errors="ignore")
        self.df["TotalCharges"] = pd.to_numeric(
            self.df["TotalCharges"], errors="coerce"
        )
        self.df = self.df.dropna()
        print(f"✅ Nettoyage : {len(self.df):,} lignes conservées")
        return self

    def encoder_cible(self):
        """Encode Churn : Yes→1, No→0."""
        self.valider()
        self.df["Churn"] = self.df["Churn"].map({"Yes": 1, "No": 0})
        print("✅ Churn encodé : Yes→1, No→0")
        return self

    def pipeline_complet(self):
        """Exécute le pipeline complet dans l'ordre."""
        self.valider()
        self.nettoyer()
        self.encoder_cible()
        print("✅ Pipeline complet terminé")
        return self.df


# ─────────────────────────────────────────
# TEST DU MODULE
# ─────────────────────────────────────────
if __name__ == "__main__":
    from src.loader import DataLoader

    loader = DataLoader()
    loader.charger()

    prep = Preprocessor(loader.df)
    df_clean = prep.pipeline_complet()

    print(f"\n📊 Dataset nettoyé : {df_clean.shape}")
    print(f"Taux de churn : {df_clean['Churn'].mean()*100:.1f}%")
