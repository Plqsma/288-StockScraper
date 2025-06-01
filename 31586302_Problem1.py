import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import sys

client = MongoClient('mongodb://localhost:27017/')
db = client['stock_data']
collection = db['most_active']

url = "https://finance.yahoo.com/most-active"
try:
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    html = response.content
except requests.exceptions.RequestException:
    try:
        with open('most_active.html', 'rb') as f:
            html = f.read()
    except FileNotFoundError:
        print("Failed to download page and local file not found.")
        sys.exit(1)

soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table')
if not table:
    print("No table found in the HTML.")
    sys.exit(1)

stocks = []
for index, row in enumerate(table.tbody.find_all('tr'), start=1):
    cols = row.find_all('td')
    if len(cols) >= 9:
        try:
            change = cols[4].text.strip()
            price = cols[3].text.strip().split()[0]
            volume = cols[6].text.strip()

            stock = {
                'Index': index,
                'Symbol': cols[0].text.strip(),
                'Name': cols[1].text.strip(),
                'Price': price,
                'Change': change,
                'Volume': volume
            }
            stocks.append(stock)
        except Exception as e:
            print(f"Error processing row {index}: {e}")
            continue

if stocks:
    collection.delete_many({})
    collection.insert_many(stocks)
    print(f"Stored {len(stocks)} inside website at localhost/31586302_Problem1.php")
else:
    print("No stock data found to store.")
