import pandas as pd

df = pd.read_csv("books_cleaned_multi_page.csv")

print("Total books:", len(df))
print("Average price:", round(df["Price"].mean(), 2))

print("\nMost expensive book:")
print(df.loc[df["Price"].idxmax()])

print("\nCheapest book:")
print(df.loc[df["Price"].idxmin()])
