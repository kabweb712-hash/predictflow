def churn_rate(df):
    """Calcule le taux de churn en pourcentage."""
    total = len(df)
    churned = df['Churn'].value_counts().get('Yes', 0)
    rate = (churned / total) * 100
    return round(rate, 2)