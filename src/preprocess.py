import pandas as pd

def clean_data(input_path, output_path):
    df = pd.read_csv(input_path)
    df['rating'] = df['rating'].fillna(df['rating'].median())
    # Verificación de tipos
    if not df['year'].dtype == 'int':
        df['year'] = df['year'].astype(int)
    if not df['rating'].dtype == 'float':
        df['rating'] = df['rating'].astype(float)
    df.to_csv(output_path, index=False)
    return df