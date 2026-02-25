# stats.py — Statistiques descriptives sur le dataset Telco

def churn_rate(df):
     """Version A : calcule le taux de churn."""
    total = len(df)
    churned = df['Churn'].value_counts().get('Yes', 0)
    rate = (churned / total) * 100
    return round(rate, 2)

