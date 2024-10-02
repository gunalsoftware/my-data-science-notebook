import yfinance as yf
import matplotlib.pyplot as plt

def make_graph(data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Close'], label='Close Price')
    plt.xlabel('Date')
    plt.ylabel('Close Price (USD)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

# Download Tesla stock data
tesla_data = yf.download('TSLA', start='2010-01-01', end='2023-01-01')

# Reset the index
tesla_data.reset_index(inplace=True)

# Plot the Tesla stock data
make_graph(tesla_data, 'Tesla Stock Price (2010-2023)')
