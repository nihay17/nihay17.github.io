from bertopic import BERTopic
from more_itertools import dft
from networkx import dfs_tree
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

documents = dft['Abstract'].dropna().astype(str).str.strip()
documents = documents[documents != ""].tolist()

print("Total documents:", len(documents))
print("Sample document:", documents[0] if documents else "No documents found")

timestamps = dfs_tree['Publication Year'].dropna().astype(str).str.strip()

print(len(documents), len(timestamps))
# Optional: Set up UMAP separately (optional tuning)
from umap import UMAP
umap_model = UMAP(n_neighbors=15, n_components=5, metric='cosine')

# Load your data
df = pd.read_excel("Citation Data.xlsx")
documents = df['Abstract'].dropna().tolist()  # or use 'Article Title' or 'Keywords'

# Optional: use publication years if available
timestamps = df['Publication Year'].dropna().tolist()

# Build and fit the topic model
topic_model = BERTopic(umap_model=umap_model)
topics, probs = topic_model.fit_transform(documents)

# 1. Intertopic Distance Map
topic_model.visualize_topics().show()

# 2. Top Words per Topic
topic_model.visualize_barchart(top_n_topics=10).show()

# 3. Topic Evolution Over Time (only if you have timestamps)
if len(timestamps) == len(documents):
    topic_model.visualize_topics_over_time(documents, timestamps).show()

# 4. Topic Hierarchy
topic_model.visualize_hierarchy().show()

# 5. Topic Similarity Heatmap
topic_model.visualize_heatmap().show()
