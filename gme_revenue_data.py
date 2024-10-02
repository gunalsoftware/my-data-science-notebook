import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL of the webpage containing GameStop revenue data
url = 'https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue'

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the revenue data
table = soup.find('table', {'class': 'historical_data_table table'})

# Check if the table exists
if table:
    # Extract the table rows
    rows = table.find_all('tr')

    # Initialize an empty list to store the data
    data = []

    # Loop through the rows and extract the date and revenue
    for row in rows[1:]:
        cols = row.find_all('td')
        date = cols[0].text.strip()
        revenue = cols[1].text.strip().replace('$', '').replace(',', '')
        data.append([date, revenue])

    # Create a DataFrame
    gme_revenue = pd.DataFrame(data, columns=['Date', 'Revenue'])

    # Convert the Revenue column to numeric
    gme_revenue['Revenue'] = pd.to_numeric(gme_revenue['Revenue'], errors='coerce')

    # Display the last five rows
    print(gme_revenue.tail())
else:
    print("Table not found on the webpage.")
