import pandas as pd
import matplotlib.pyplot as plt
from bertopic import BERTopic


# Load dataset
data = pd.read_excel("Citation Data.xlsx")

# Group by research area
research_areas = data['Research Areas'].dropna().unique()  # Remove NaN values
topic_dist = {}

# Apply BERTopic to each research area
model = BERTopic.load("bertopic_model")
model.save("bertopic_model")  # Saves locally

for area in research_areas:
    area_data = data[data['Research Areas'] == area]
    
    # Ensure abstracts exist for transformation
    if not area_data['Abstract'].dropna().empty:
        topics, _ = model.transform(area_data['Abstract'].dropna())
        topic_dist[area] = pd.Series(topics).value_counts(normalize=True)

# Convert dictionary to DataFrame for visualization
topic_df = pd.DataFrame(topic_dist).fillna(0)

# Plot stacked bar chart
plt.figure(figsize=(12, 6))
topic_df.plot(kind='bar', stacked=True)
plt.title('Topic Distribution by Research Area')
plt.xlabel('Research Area')
plt.ylabel('Proportion')
plt.legend(title='Topic ID')
plt.savefig('topic_distribution.png')
plt.close()
