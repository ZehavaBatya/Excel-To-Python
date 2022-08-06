In []: # Libraries
        import pandas as pd
        import numpy as np
        import yfinance as yf
In []: # get S&P500 ticker
        stock_data = yf.Ticker("^GSPC")

        # get historical market data
        df_hist = stock_data.history(period = '5y')

In []:  df_hist.head()

In []:  df_hist['Close'].std()

In []:  df_hist['Close'].min()

In []: df_hist['Close'].max()

In []: df_hist[df_hist['Close'] > 3000]

