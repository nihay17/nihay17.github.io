import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = 'Citation Data.xlsx'
df = pd.read_excel('C:\\Users\\Niha\\OneDrive\\Documents\\Grad School\\nihay17.github.io\\KM_Project\\Citation Data.xlsx')

# Optional: Rename columns for ease (edit based on actual headers)
df = df.rename(columns={
    'Publication Year': 'Year',
    'Times Cited, All Databases': 'Citations',
    'Author Full Names': 'Authors',  # adjust as needed
    'Article Title': 'Title'
})

# -------------------------
# 1. Citation Trend by Year
# -------------------------
yearly_citations = df.groupby('Year')['Citations'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(data=yearly_citations, x='Year', y='Citations', marker='o')
plt.title('Total Citations by Year')
plt.ylabel('Citations')
plt.xlabel('Publication Year')
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------------
# 2. Top 10 Most Cited Papers
# -------------------------------
top_papers = df.sort_values(by='Citations', ascending=False).head(10)
print("\nTop 10 Most Cited Papers:")
print(top_papers[['Title', 'Authors', 'Year', 'Citations']])

# ----------------------------------
# 3. Top Authors by Total Citations
# ----------------------------------
# Assumes 'Authors' is a string like: "Smith J; Doe A"
# We'll split and aggregate per author
from collections import Counter

author_counter = Counter()
for authors in df['Authors'].dropna():
    for author in authors.split(';'):
        author = author.strip()
        if author:
            total_cites = df[df['Authors'].str.contains(author, na=False)]['Citations'].sum()
            author_counter[author] = total_cites

# Convert to DataFrame
author_df = pd.DataFrame(author_counter.items(), columns=['Author', 'Total Citations'])
top_authors = author_df.sort_values(by='Total Citations', ascending=False).head(10)

# Plot top authors
plt.figure(figsize=(10, 6))
sns.barplot(data=top_authors, x='Total Citations', y='Author')
plt.title('Top 10 Authors by Total Citations')
plt.tight_layout()
plt.show()


