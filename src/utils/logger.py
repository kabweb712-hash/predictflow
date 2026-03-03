import logging
import os
from datetime import datetime

def setup_logger(name="PredictFlow", log_dir="logs"):
    """
    Configure un logger avec sortie console + fichier.
    
    Args:
        name: Nom du logger
        log_dir: Dossier de stockage des logs
    
    Returns:
        Logger configuré
    """
    # 1️⃣ Créer le dossier logs s'il n'existe pas
    os.makedirs(log_dir, exist_ok=True)
    
    # 2️⃣ Créer le logger principal
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # 3️⃣ Éviter les doublons si appelé plusieurs fois
    if logger.handlers:
        return logger
    
    # 4️⃣ Format des messages
    formatter = logging.Formatter(
        '%(asctime)s | %(name)s | %(levelname)-8s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # 5️⃣ Handler CONSOLE (niveau INFO minimum)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # 6️⃣ Handler FICHIER (niveau DEBUG, tout est enregistré)
    log_file = os.path.join(log_dir, f"predictflow_{datetime.now().strftime('%Y%m%d')}.log")
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger
