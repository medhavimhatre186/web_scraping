import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("books_cleaned_multi_page.csv")

# 1️⃣ Price Distribution
plt.figure()
plt.hist(df["Price"], bins=10)
plt.xlabel("Book Price (£)")
plt.ylabel("Number of Books")
plt.title("Distribution of Book Prices")
plt.show(block=False)
plt.pause(3)
plt.close()

# 2️⃣ Books Count by Rating
rating_counts = df["Rating"].value_counts().sort_index()

plt.figure()
plt.bar(rating_counts.index, rating_counts.values)
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.title("Books Count by Rating")
plt.show(block=False)
plt.pause(3)
plt.close()

# 3️⃣ Average Price by Rating
avg_price_rating = df.groupby("Rating")["Price"].mean()

plt.figure()
plt.bar(avg_price_rating.index, avg_price_rating.values)
plt.xlabel("Rating")
plt.ylabel("Average Price (£)")
plt.title("Average Book Price by Rating")
plt.show(block=False)
plt.pause(3)
plt.close()

print("✅ All graphs displayed successfully")
