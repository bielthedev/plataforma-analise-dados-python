
from etl import extract, transform
from analysis import resumo

df = extract('data/raw/vendas.csv')
df = transform(df)
print(resumo(df))
