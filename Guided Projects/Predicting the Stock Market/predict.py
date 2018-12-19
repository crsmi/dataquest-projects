import pandas as pd
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

#Import SP500 data and clean date column
hist = pd.read_csv('sphist.csv')
hist['Date'] = pd.to_datetime(hist['Date'])
hist = hist.sort_values(by='Date')

#Generate Price History Indicators
hist['day_5'] = hist['Close'].rolling(window=5).mean().shift(1)
hist['day_30'] = hist['Close'].rolling(window=30).mean().shift(1)
hist['day_365'] = hist['Close'].rolling(window=365).mean().shift(1)
hist['price_ratio'] = (hist['Close'].rolling(window=5).mean()/hist['Close'].rolling(window=365).mean()).shift(1)
hist['price_std_ratio'] = (hist['Close'].rolling(window=5).std()/hist['Close'].rolling(window=365).std()).shift(1)
hist['volume_ratio'] = (hist['Volume'].rolling(window=5).mean()/hist['Volume'].rolling(window=365).mean()).shift(1)
hist['volume_std_ratio'] = (hist['Volume'].rolling(window=5).std()/hist['Volume'].rolling(window=365).std()).shift(1)

#Remove Rows with NA in created columns
hist = hist[hist["Date"] > datetime(year=1951, month=1, day=2)]
hist = hist.dropna(axis=0)

#Train/Test Split
train = hist[hist["Date"] < datetime(year=2013, month=1, day=1)]
test = hist[hist["Date"] >= datetime(year=2013, month=1, day=1)]

#Train 
model = LinearRegression()
features = ['day_5','day_30','day_365','price_ratio','price_std_ratio','volume_ratio','volume_std_ratio']
model.fit(train[features],train['Close'])
predictions = model.predict(test[features])
error = mean_absolute_error(test['Close'],predictions)
print(error)