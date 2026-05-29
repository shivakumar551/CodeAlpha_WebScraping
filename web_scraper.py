import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "http://quotes.toscrape.com"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all quotes
quotes = soup.find_all("div", class_="quote")

# Empty list
data = []

# Extract quote and author
for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    
    data.append({
        "Quote": text,
        "Author": author
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("quotes.csv", index=False)

print("Data scraped successfully!")