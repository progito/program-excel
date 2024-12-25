import pandas as pd
from config import INPUT_FILE, OUTPUT_FILE


def merge() -> bool:
    """
    Функция формирования/объединения
    :return: bool
    """
    try:
        df = pd.read_csv(INPUT_FILE, sep=';')
        df['PLU'] = df['PLU'].fillna(method='ffill')
        if df['SAP_ID'].isnull().any():
            df = df.dropna(subset=['SAP_ID'])
        df['PLU'] = df['PLU'].astype(int)
        result = pd.merge(df[['PLU']], df[['SAP_ID']], how='cross')
        result = result.drop_duplicates()
        result.to_csv(OUTPUT_FILE, index=False, sep=';')
        print(f"Файл успешно сохранен: {OUTPUT_FILE}")
        return True

    except Exception as error:
        print(f"Ошибка: {error}")
        return False


if __name__ == '__main__':
    merge()
