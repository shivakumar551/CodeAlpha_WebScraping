import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("div", class_="quote")
data = []
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
