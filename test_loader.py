from src.loader import load_data, get_basic_info

df = load_data('data/telco_churn.csv')
get_basic_info(df)