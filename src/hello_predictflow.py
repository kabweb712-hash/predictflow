import csv
import os

# ==== CONFIGURATION ===
PROJECT_NAME = "PredictFlow"
VERSION = "0.1.0"
DATA_PATH = "data/telco_churn.csv"


def print_banner():
    print("=" * 50)
    print(f" {PROJECT_NAME} v{VERSION}")
    print(" MLOps Churn Prediction Platform")
    print("=" * 50)


def check_dataset(filepath):
    """Vérifie que le dataset existe et affiche ses infos"""
    if not os.path.exists(filepath):
        print(f"❌ Dataset introuvable : {filepath}")
        return False

    with open(filepath, encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = sum(1 for _ in reader)

    print(f"✅ Dataset trouvé : {filepath}")
    print(f"    → {rows} clients")
    print(f"    → {len(header)} colonnes")
    print(f"    → Colonnes : {', '.join(header[:5])} ...")
    return True


def check_churn_rate(filepath): 
    """Calcule le taux de chrun brut."""
    total = 0
    churned = 0
    
    with open(filepath, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += 1
            if row['Churn'].strip() == 'Yes':  
                churned += 1
    
    rate = (churned / total) * 100
    print(f"\n📊 Taux de churn : {churned}/{total} = {rate:.1f}%")


if __name__ == "__main__":
    print_banner()
    print("\n🔍 Vérification du dataset...")
    if check_dataset(DATA_PATH):
        check_churn_rate(DATA_PATH)
    print("\n✅ PredictFlow initialisé avec succès !")