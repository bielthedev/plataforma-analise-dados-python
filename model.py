
from sklearn.linear_model import LinearRegression

def treinar(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model
