import pandas as pd

def clean_data(input_path, output_path):
    df = pd.read_csv(input_path)
    # In case there is any NULL value, they will be filled with mean value
    df['rating'] = df['rating'].fillna(df['rating'].mean())
    # type-conversion
    df['year'] = df['year'].astype(int)
    df['rating'] = df['rating'].astype(float)
    df.to_csv(output_path, index=False)
    return df

if __name__ == "__main__":
    clean_data("data/movies.csv", "data/movies_clean.csv")