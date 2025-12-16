import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

all_books = []

# Rating conversion
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

# Scrape first 5 pages
for page in range(1, 6):
    url = base_url.format(page)
    response = requests.get(url)

    if response.status_code != 200:
        print(f"❌ Failed to load page {page}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]

        price_text = book.find("p", class_="price_color").text
        price = float(price_text.replace("£", "").replace("Â", ""))

        rating_text = book.p["class"][1]
        rating = rating_map.get(rating_text, 0)

        all_books.append({
            "Title": title,
            "Price": price,
            "Rating": rating
        })

# Create DataFrame
df = pd.DataFrame(all_books)

# Save CSV
df.to_csv("books_cleaned_multi_page.csv", index=False)

# -------- EXTRA FEATURES --------
total_books = len(df)
average_price = df["Price"].mean()

print("✅ Scraping completed successfully!")
print("📚 Total books scraped:", total_books)
print("💰 Average book price: £", round(average_price, 2))
