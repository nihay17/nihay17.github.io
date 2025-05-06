from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer
from umap import UMAP
import pandas as pd

# ✅ Load and filter data
df = pd.read_excel("Citation Data.xlsx")
df_filtered = df.dropna(subset=["Abstract", "Publication Year"])
documents = df_filtered["Abstract"].astype(str).str.strip().tolist()
timestamps = df_filtered["Publication Year"].astype(int).tolist()

print(f"✅ Total valid documents: {len(documents)}")

# ✅ Configure vectorizer and UMAP
vectorizer_model = CountVectorizer(
    stop_words="english",
    max_df=1.0,   # Accept terms in all docs
    min_df=1,     # Keep even rare terms
    ngram_range=(1, 2)
)

umap_model = UMAP(n_neighbors=15, n_components=5, metric="cosine", random_state=42)

# ✅ Train BERTopic model
topic_model = BERTopic(
    vectorizer_model=vectorizer_model,
    umap_model=umap_model,
    language="english",
    calculate_probabilities=True,
    verbose=True
)

topics, probs = topic_model.fit_transform(documents)

# ✅ Try to visualize topic evolution over time
if len(documents) == len(timestamps):
    try:
        topic_model.visualize_topics_over_time(documents, timestamps).show()
    except Exception as e:
        print("⚠️ Could not render topic trend visualization:", e)
        # Fallback: List topic trends manually
        topics_over_time = topic_model.topics_over_time(documents, timestamps)
        print("\n📈 Top Topic Trends (Textual Fallback):")
        for topic_id in topics_over_time["Topic"].unique():
            trend = topics_over_time[topics_over_time["Topic"] == topic_id]
            years = trend["Timestamp"].tolist()
            freq = trend["Frequency"].tolist()
            print(f"Topic {topic_id}:")
            print(f"  Years: {years}")
            print(f"  Frequency: {freq}\n")
else:
    print("⚠️ Cannot visualize or compute trends: Document and timestamp count mismatch.")
    
# View top keywords for Topic 0
print("🔍 Topic 0 Keywords:")
print(topic_model.get_topic(0))

# View top keywords for Topic 1
print("\n🔍 Topic 1 Keywords:")
print(topic_model.get_topic(1))

