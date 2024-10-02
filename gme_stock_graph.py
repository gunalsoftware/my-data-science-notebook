import yfinance as yf
import matplotlib.pyplot as plt

def make_graph(data, title)
    plt.figure(figsize=(10, 6))
    plt.plot(data['Data'], data['Close'], lable='Close Price')
    plt.ylabel('Date')
    plt.ylabel('Close Price (USD)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()



gme_data = yf.download('GME', start='2010-01-01', end='2013-01-01')


gme_data.reset_index(inplace=True)

make_graph(gme_data, 'GameStop Stock Price (2010-2013)')

