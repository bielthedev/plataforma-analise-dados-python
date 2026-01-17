
import matplotlib.pyplot as plt

def plot_vendas(df):
    df.groupby('categoria')['total'].sum().plot(kind='bar')
    plt.show()
