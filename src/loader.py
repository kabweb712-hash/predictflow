"""
PredictFlow — Module de chargement des données
Classe DataLoader : charge, inspecte et filtre le dataset Telco.
"""

import pandas as pd
from pathlib import Path


class DataLoader:
    """
    Charge et gère le dataset Telco Customer Churn.

    Usage:
        loader = DataLoader("data/telco_churn.csv")
        loader.charger().inspecter()
        churners = loader.filtrer(churn="Yes")
    """

    COLONNES_NUMERIQUES = ["tenure", "MonthlyCharges", "TotalCharges"]

    def __init__(self, chemin="data/raw/telco_churn.csv"):
        self.chemin = Path(chemin)
        self.df = None
        self.est_charge = False

    def charger(self):
        """Charge le CSV et corrige les types."""
        try:
            self.df = pd.read_csv(self.chemin)
            self.df["TotalCharges"] = pd.to_numeric(
                self.df["TotalCharges"], errors="coerce"
            )
            self.est_charge = True
            print(f"✅ Dataset chargé : {self.df.shape[0]:,} lignes, "
                  f"{self.df.shape[1]} colonnes")
        except FileNotFoundError:
            print(f"❌ Fichier introuvable : {self.chemin}")
        except Exception as e:
            print(f"❌ Erreur inattendue : {e}")
        return self

    def inspecter(self):
        """Affiche un résumé du dataset."""
        if not self.est_charge:
            print("⚠️  Aucune donnée chargée. Appelle charger() d'abord.")
            return self

        nb_churned = (self.df["Churn"] == "Yes").sum()
        print(f"\n📊 DATASET : {self.chemin.name}")
        print(f"{'─'*45}")
        print(f"  Clients total    : {len(self.df):,}")
        print(f"  Churned          : {nb_churned:,} "
              f"({nb_churned/len(self.df)*100:.1f}%)")
        print(f"  Actifs           : {len(self.df)-nb_churned:,} "
              f"({(len(self.df)-nb_churned)/len(self.df)*100:.1f}%)")

        manquantes = self.df.isnull().sum()
        manquantes = manquantes[manquantes > 0]
        print(f"\n  Valeurs manquantes :")
        if manquantes.empty:
            print("    Aucune ✅")
        else:
            for col, nb in manquantes.items():
                print(f"    {col} : {nb}")
        return self

    def filtrer(self, churn=None, contrat=None, anciennete_max=None):
        """
        Filtre les clients selon des critères.

        Args:
            churn (str)         : "Yes" ou "No"
            contrat (str)       : "Month-to-month", "One year", "Two year"
            anciennete_max (int): ancienneté maximum en mois

        Returns:
            pd.DataFrame: sous-ensemble filtré (self.df non modifié)
        """
        if not self.est_charge:
            print("⚠️  Aucune donnée chargée. Appelle charger() d'abord.")
            return None

        masque = pd.Series([True] * len(self.df), index=self.df.index)

        if churn:
            masque &= (self.df["Churn"] == churn)
        if contrat:
            masque &= (self.df["Contract"] == contrat)
        if anciennete_max is not None:
            masque &= (self.df["tenure"] <= anciennete_max)

        resultat = self.df[masque].copy()
        print(f"✅ Filtrage : {len(resultat):,} clients sélectionnés")
        return resultat

    def __str__(self):
        if self.est_charge:
            return (f"DataLoader('{self.chemin.name}') "
                    f"— {len(self.df):,} clients chargés")
        return f"DataLoader('{self.chemin.name}') — non chargé"

    def __repr__(self):
        return f"DataLoader(chemin='{self.chemin}', charge={self.est_charge})"

    def __len__(self):
        return len(self.df) if self.est_charge else 0


# ─────────────────────────────────────────
# TEST DU MODULE
# ─────────────────────────────────────────
if __name__ == "__main__":
    loader = DataLoader()
    loader.charger().inspecter()

    print(f"\n{loader}")
    print(f"Nb clients : {len(loader)}")

    churners = loader.filtrer(churn="Yes", contrat="Month-to-month")
    if churners is not None:
        print(f"Churners mensuels : {len(churners)}")