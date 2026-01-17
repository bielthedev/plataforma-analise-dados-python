
import pandas as pd

def extract(path):
    return pd.read_csv(path)

def transform(df):
    df['total'] = df['quantidade'] * df['preco']
    return df

def load(df, output):
    df.to_csv(output, index=False)
