import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.ensemble import GradientBoostingRegressor

class Model():
    def __init__(self):
        #url = "https://raw.githubusercontent.com/crisb-7/BostonRealEstate/main/bostonRealEstate.csv"
        url = "bostonRealEstate.csv"
        df = pd.read_csv(url)
        df = df.dropna(axis = 0)
        scaler = StandardScaler()
        x = scaler.fit_transform(df.drop(columns = "MEDV"))
        y = df.MEDV
        x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.90, random_state = 0)
        regressor = (GradientBoostingRegressor(random_state = 0))
        self.cv_train=regressor.fit(x_train, y = y_train)

    def predict(self, responses):
        print(responses)
        result = self.cv_train.predict([responses])
        
        return result
