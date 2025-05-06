from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import make_blobs
from umap import UMAP
import pandas as pd
import matplotlib.pyplot as plt

# ✅ Load and clean the data
df = pd.read_excel("Citation Data.xlsx")
documents = df["Abstract"].dropna().astype(str).str.strip()
documents = documents[documents != ""].tolist()

print(f"✅ Total valid documents: {len(documents)}")

# ✅ Optional: Configure vectorizer to filter common/short words
vectorizer_model = CountVectorizer(
    stop_words="english",
    max_df=1.0,        # Allow terms in up to 100% of docs
    min_df=2,          # Terms must appear in at least 2 docs
    ngram_range=(1, 2)
)

# ✅ Dimensionality reduction with UMAP
umap_model = UMAP(n_neighbors=15, n_components=5, metric="cosine", random_state=42)

# ✅ Build and fit the topic model
topic_model = BERTopic(
    umap_model=umap_model,
    vectorizer_model=vectorizer_model,
    language="english",
    calculate_probabilities=True,
    verbose=True
)

topics, probs = topic_model.fit_transform(documents)

# ✅ Show top keywords for each topic
print("\n📚 Top 10 keywords for each topic:\n")
for topic_num in range(min(10, len(topic_model.get_topic_info()))):
    words = topic_model.get_topic(topic_num)
    keywords = [word for word, _ in words]
    print(f"Topic {topic_num}: {', '.join(keywords[:10])}")

# ✅ Topic visualizations
try:
    fig = topic_model.visualize_topics()
    fig.show()
except Exception as e:
    print("⚠️ Could not render visualize_topics():", e)

# ✅ Bar chart of top topics
try:
    topic_model.visualize_barchart(top_n_topics=10).show()
except Exception as e:
    print("⚠️ Could not render visualize_barchart():", e)

# ✅ Topic hierarchy
try:
    topic_model.visualize_hierarchy().show()
except Exception as e:
    print("⚠️ Could not render visualize_hierarchy():", e)

# ✅ Heatmap of topic similarity
try:
    topic_model.visualize_heatmap().show()
except Exception as e:
    print("⚠️ Could not render visualize_heatmap():", e)
