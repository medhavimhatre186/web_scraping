import pandas as pd

df = pd.read_csv("books_cleaned_multi_page.csv")

print("Total books scraped:", len(df))
print("Average price:", round(df["Price"].mean(), 2))
