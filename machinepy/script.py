import json
from sklearn.cluster import KMeans

# Load the JSON data
with open('machinepy/coordinates.json') as json_file:
    data = json.load(json_file)

# Extract x, y, and timestamp from the JSON data
coordinates = [[entry['x'], entry['y']] for entry in data]

# Define the number of clusters (k) based on the expected number of most visited coordinates
k = 3

# Perform K-means clustering
kmeans = KMeans(n_clusters=k)
kmeans.fit(coordinates)

# Get the cluster labels
clusters = kmeans.labels_

# Count the number of data points in each cluster
cluster_counts = {}
for cluster in clusters:
    cluster_counts[cluster] = cluster_counts.get(cluster, 0) + 1

# Sort the clusters by count in descending order
sorted_clusters = sorted(cluster_counts.items(), key=lambda x: x[1], reverse=True)

# Get the most visited coordinates
most_visited_clusters = sorted_clusters[:k]
most_visited_indices = [cluster[0] for cluster in most_visited_clusters]
most_visited_coordinates = [kmeans.cluster_centers_[index] for index in most_visited_indices]

print('Most visited coordinates:')
for coord in most_visited_coordinates:
    print(f'X: {coord[0]}, Y: {coord[1]}')
