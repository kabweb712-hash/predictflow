def churn_rate(df):
    """Calcule le taux de churn en pourcentage."""
    total = len(df)
    churned = df['Churn'].sum()        
    rate = (churned / total) * 100
    return round(rate, 2)


def average_charges(df):
    """Calcule les charges moyennes par client."""
    return df[df['Churn'] == 1]['MonthlyCharges'].mean(), df[df['Churn'] == 0]['MonthlyCharges'].mean()



def tenure_stats(df):
    """Affiche les valeurs min, max et moyenne de la durée d'abonnement."""
    return int(df['tenure'].min()), int(df['tenure'].max()), round(float(df['tenure'].mean()), 2)


def contract_distribution(df):
    """Affiche la distribution des types de contrats."""
    return df['Contract'].value_counts()

