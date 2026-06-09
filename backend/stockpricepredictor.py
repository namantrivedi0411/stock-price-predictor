import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

stocks=input("Enter the code of the stock:")
data=yf.download(stocks,"2008-01-01","2026-05-31",auto_adjust=True)
print(data.head())

print(data.shape)
print(data.info())
print(data.describe())

data.Close.plot(figsize=(10,7),color='r')
plt.ylabel("{} Prices".format(stocks))
plt.title("{} Price Series".format(stocks))
plt.show()


sns.histplot(data["Close"])
plt.show()

data['Prev_Close'] = data['Close'].shift(1)
data['MA50'] = data['Close'].rolling(50).mean()
data['MA200'] = data['Close'].rolling(200).mean()

data.dropna(inplace=True)

x = data[['Prev_Close','MA50','MA200']]
y = data['Close']

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.linear_model import LinearRegression

lr=LinearRegression()
lr.fit(x_train,y_train)
pred1=lr.predict(x_test)
print(pred1)

#MSE ---> Mean Squared
#RMSE ---> sart(MSE)
#r2_square ---> 1.0 (good model)

from sklearn.metrics import mean_squared_error, r2_score

def calculate_metrics(y_test,y_pred):    #y_test: ground truth    y_pred: model predicted
    mse=mean_squared_error(y_test,y_pred)
    rmse=np.sqrt(mse)
    r2_scores=r2_score(y_test,y_pred)

    print("MSE: ",mse)
    print("RMSE: ",rmse)
    print("R2_Score: ",r2_scores)

calculate_metrics(y_test,pred1)

from sklearn.linear_model import Lasso,Ridge

la=Lasso().fit(x_train,y_train)
ri=Ridge().fit(x_train,y_train)
la_p=la.predict(x_test)
ri_p=ri.predict(x_test)

calculate_metrics(y_test,la_p)
calculate_metrics(y_test,ri_p)


from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV

svr=SVR()

param_grid={'C':[0.1,1,10,100,1000],
            'gamma':[1,0.1,0.01,0.001,0.0001],
            'kernel':['rbf']}

grid=GridSearchCV(SVR(), param_grid,refit=True,verbose=3)
grid.fit(x_train,y_train)

svr=SVR(C=10,gamma=0.01,kernel='rbf')
svr.fit(x_train,y_train)
svr_pred=svr.predict(x_test)

import joblib
joblib.dump(ri,'model.pkl')
#ridge_from_joblib=model=joblib.load("model.pkl")
joblib.dump(x.columns.tolist(),"features.pkl")
