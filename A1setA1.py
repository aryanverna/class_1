import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error

df=pd.read_csv('Advertising.csv')
df.sample(5)
df.info()

a=df["TV"]
b=df["Sales"]
plt.figure(figsize=(10,5))
plt.scatter(a,b,color="green")

a=df["Radio"]
b=df["Sales"]
plt.figure(figsize=(10,5))
plt.scatter(a,b,color="red")

a=df["Newspaper"]
b=df["Sales"]
plt.figure(figsize=(10,5))
plt.scatter(a,b,color="purple")
plt.show()

X=np.array(df[["TV"]])
y=np.array(df[["Sales"]])
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=5)
regressor=LinearRegression()
regressor.fit(X_train,y_train)
plt.scatter(X_test,y_test,color="green")
plt.plot(X_train,regressor.predict(X_train),color="red",linewidth=3)
plt.title('Regression(Test Set)')
plt.xlabel('TV')
plt.ylabel('Sales')
plt.show()

y_pred=regressor.predict(X_test)
print('R2 score: %.2f' % r2_score(y_test,y_pred))
print('Mean Error:',mean_squared_error(y_test,y_pred))
def sales_price(tv):
    result=regressor.predict(np.array(tv).reshape(1,-1))
    return(result[0,0])

tv=int(input('Enter TV value:'))
print('The Sales will be:',int(sales_price(tv)))

