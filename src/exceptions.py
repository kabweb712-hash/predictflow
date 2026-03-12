"""
PredictFlow — Hiérarchie d'exceptions personnalisées.
"""

class PredictFlowError(Exception):
    """Erreur de base pour tout PredictFlow."""
    pass

class DataLoadError(PredictFlowError):
    """Erreur lors du chargement des données."""
    pass

class PreprocessingError(PredictFlowError):
    """Erreur lors du prétraitement."""
    pass

class StatsError(PredictFlowError):
    """Erreur lors du calcul des statistiques."""
    pass