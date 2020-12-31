import requests
import pandas as pd
import matplotlib.pyplot as plt 

#Enter tge ticker of the companies that you want to analyse
companies = ['AAPL', 'FB', 'GOOG', 'F', 'TSLA']

#empty list to add each of the companies
listofdf = []

#API end point request
requests.get(f"https://financialmodelingprep.com/api/v3/historical-price-full/aapl?serietype=line")

#outcome
{
    "symbol":"AAPL",
    "historical": [
        {"date": "1989-09-19",
        "close": 1.54},
        {"date": "1989-09-20",
        "close": 1.59},
        {"date": "1989-09-21",
        "close": 1.6},
    ]
}


#For loop for AAPL
for item in companies:
    histprices = requests.get(f"https://financialmodelingprep.com/api/v3/historical-price-full/{item}?serietype=line")

##convert response to json
    histprices = histprices.json()

##Parse the API response and select only last 600 days of prices
    histprices - histprices['historical'][-600:]

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