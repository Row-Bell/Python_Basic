'''import requests
import pandas as pd
import matplotlib.pyplot as plt 

#Enter tge ticker of the companies that you want to analyse
companies = ['AAPL', 'FB', 'GOOG', 'F', 'TSLA']

#empty list to add each of the companies
listofdf = []

#API end point request
#requests.get(f"https://financialmodelingprep.com/api/v3/historical-price-full/aapl?serietype=line")

#For loop for AAPL
for item in companies:
    histprices = requests.get(f"https://financialmodelingprep.com/api/v3/historical-price-full/{item}?serietype=line")

##convert response to json
    histprices = histprices.json()

##Parse the API response and select only last 600 days of prices
    #histprices = histprices["historical"][-600:]

##Convert from dict to pandas datafram
    histpricesdf = pd.DataFrame.from_dict(histprices)

##rename column from close to the name of the company
    histpricesdf = histpricesdf.rename({'close': item}, axis=1)

##append all dfs to list
    listofdf.append(histpricesdf)

#Set index of each DataFrame by common column before concatinating them
dfs = [df.set_index('date') for df in listofdf]

histpriceconcat = pd.concat(dfs, axis=1)

#Plotting the stocks
for i, col in enumerate(histpriceconcat.columns):
    histpriceconcat[col].plot()

plt.title('Price Evolution Comparison')

plt.xticks(rotation=70)
plt.legend(histpriceconcat.columns)

#Saving the graph into a JPG file
plt.savefig('fool.png', bbox_inches='tight')

# Import the yfinance. If you get module not found error the run !pip install yfinance from your Jupyter notebook
import yahoofinance as yf

# Get the data for the stock AAPL
data = yf.download('AAPL','2016-01-01','2019-08-01')

# Import the plotting library
import matplotlib.pyplot as plt


# Plot the close price of the AAPL
data['Adj Close'].plot()
plt.show()'''
#################################################
from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd

# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
tickers = ['AAPL', 'MSFT', '^GSPC']

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2010-01-01'
end_date = '2016-12-31'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
panel_data = data.DataReader('INPX', 'google', start_date, end_date)

panel_data.to_frame().head(9)

# Getting just the adjusted closing prices. This will return a Pandas DataFrame
# The index in this DataFrame is the major index of the panel_data.
close = panel_data['Close']

# Getting all weekdays between 01/01/2000 and 12/31/2016
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')

# How do we align the existing prices in adj_close with our new set of dates?
# All we need to do is reindex close using all_weekdays as the new index
close = close.reindex(all_weekdays)

# Reindexing will insert missing values (NaN) for the dates that were not present
# in the original set. To cope with this, we can fill the missing by replacing them
# with the latest available price for each instrument.
close = close.fillna(method='ffill')

print(all_weekdays)

# DatetimeIndex(['2010-01-01', '2010-01-04', '2010-01-05', '2010-01-06',
#               '2010-01-07', '2010-01-08', '2010-01-11', '2010-01-12',
#               '2010-01-13', '2010-01-14',
#               ...
#               '2016-12-19', '2016-12-20', '2016-12-21', '2016-12-22',
#               '2016-12-23', '2016-12-26', '2016-12-27', '2016-12-28',
#               '2016-12-29', '2016-12-30'],
#              dtype='datetime64[ns]', length=1826, freq='B')

close.head(10)

close.describe()

# Get the MSFT timeseries. This now returns a Pandas Series object indexed by date.
msft = close.loc[:, 'MSFT']

# Calculate the 20 and 100 days moving averages of the closing prices
short_rolling_msft = msft.rolling(window=20).mean()
long_rolling_msft = msft.rolling(window=100).mean()

# Plot everything by leveraging the very powerful matplotlib package
fig, ax = plt.subplots(figsize=(16,9))

ax.plot(msft.index, msft, label='MSFT')
ax.plot(short_rolling_msft.index, short_rolling_msft, label='20 days rolling')
ax.plot(long_rolling_msft.index, long_rolling_msft, label='100 days rolling')

ax.set_xlabel('Date')
ax.set_ylabel('Adjusted closing price ($)')
ax.legend()