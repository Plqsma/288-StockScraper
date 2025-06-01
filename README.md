# Yahoo Finance Stock Scraper & MongoDB Viewer

This project scrapes the **most active stocks** from Yahoo Finance using Python, stores the data in a **MongoDB collection**, and serves it via a PHP frontend for local web viewing.

---

## Features

- Scrapes live stock data (symbol, name, price, change, volume) from [Yahoo Finance](https://finance.yahoo.com/most-active)
- Handles web failures with a fallback to a local HTML file
- Saves stock data into MongoDB (`stock_data.most_active`)
- Displays saved stock data using a simple PHP web interface

---

## File Structure

| File | Description |
|------|-------------|
| `31586302_Problem1.py` | Python script for scraping and inserting stock data into MongoDB |
| `31586302_Problem1.php` | PHP script to display MongoDB data on `localhost` |
| `most_active.html` | Optional local backup HTML file for scraping fallback |

---

## How to Run

### 1. Start MongoDB
Make sure MongoDB is running on `localhost:27017`

### 2. Run the Python Scraper
```bash
python3 31586302_Problem1.py
```

### 3. View Results in Browser
Move `31586302_Problem1.php` to your web server directory (e.g., `htdocs` for XAMPP), then open:
```
http://localhost/31586302_Problem1.php
```

---

## Technologies Used

- **Python**: Web scraping with `requests`, `BeautifulSoup`
- **MongoDB**: NoSQL database for storing stock data
- **PHP**: Simple script to query and display MongoDB contents in a web browser

---

## Example Output

After running the scraper, you'll see a webpage displaying the most active stocks with the following fields:
- Symbol
- Name
- Price
- Change
- Volume
