def churn_rate(df):
    """Version B : taux de churn en pourcentage."""  # ← change seulement ça
    total = len(df)
    churned = df['Churn'].value_counts().get('Yes', 0)
    rate = (churned / total) * 100
    return round(rate, 2)