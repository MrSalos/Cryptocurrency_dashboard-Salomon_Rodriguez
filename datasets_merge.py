import pandas as pd
import numpy as np

csv_files = [
             'Datasets\coin_Aave.csv', 
             'Datasets\coin_BinanceCoin.csv', 
             'Datasets\coin_Bitcoin.csv',
             'Datasets\coin_Cardano.csv',
             'Datasets\coin_ChainLink.csv', 
             'Datasets\coin_Cosmos.csv',
             'Datasets\coin_CryptocomCoin.csv',
             'Datasets\coin_Dogecoin.csv',
             'Datasets\coin_Ethereum.csv',
             'Datasets\coin_Litecoin.csv',
             'Datasets\coin_Monero.csv',
             'Datasets\coin_NEM.csv',
             'Datasets\coin_Stellar.csv',
             'Datasets\coin_Tether.csv',
             'Datasets\coin_XRP.csv'
]

column_names = ['SNo', 'Name', 'Symbol', 'Date', 'High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap']

currencies = pd.DataFrame(columns=column_names)

currencies[['Name', 'Symbol', 'Date']] = currencies[['Name', 'Symbol', 'Date']].astype('string')
currencies[['High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap']] = currencies[['High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap']].astype('float')




for csv in csv_files:
    df = pd.read_csv(csv)

    currencies = currencies.merge(df, how='outer')


currencies.to_csv('Datasets\crypto_currencies.csv')
