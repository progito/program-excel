import pandas as pd
from config import INPUT_FILE, OUTPUT_FILE


def merge() -> bool:
    """
    Функция формирования/объединения
    :return: bool
    """
    df = pd.read_csv(INPUT_FILE, sep=';')
    if df['PLU'].isnull().any():
        df = df.dropna(subset=['PLU'])
    try:
        df['PLU'] = df['PLU'].astype(int)
    except ValueError as error:
        print(f"{error}")
        return False
    pd.merge(df[['PLU']], df[['SAP_ID']], how='cross').to_csv(OUTPUT_FILE, index=False, sep=';')
    return True

if __name__ == '__main__':
    merge()