import json
from sklearn.cluster import KMeans

# Function to analyze a heatmap
def analyze_heatmap(coordinates):
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

    # Calculate the average time spent, frequency of visits, and total time spent on the webpage
    results = []
    total_time = 0
    for cluster in most_visited_clusters:
        cluster_index = cluster[0]
        cluster_entries = [coordinates[i] for i in range(len(coordinates)) if clusters[i] == cluster_index]
        time_sum = sum(entry[2] for entry in cluster_entries)
        average_time = time_sum / len(cluster_entries) / 1000  # Convert from milliseconds to seconds
        frequency = len(cluster_entries)
        results.append((average_time, frequency))
        total_time += max(entry[2] for entry in cluster_entries) - min(entry[2] for entry in cluster_entries)

    # Convert total time to minutes
    total_time_minutes = total_time / 1000 / 60

    return most_visited_coordinates, results, total_time_minutes

# Load the JSON data for Banorte Portal A
with open('coordinate.json') as json_file:
    data1 = json.load(json_file)

# Extract x, y, and timestamp from the JSON data for Banorte Portal A
coordinates1 = [[entry['x'], entry['y'], entry['timestamp']] for entry in data1]

# Load the JSON data for Banorte Portal B
with open('coordinates.json') as json_file:
    data2 = json.load(json_file)

# Extract x, y, and timestamp from the JSON data for Banorte Portal B
coordinates2 = [[entry['x'], entry['y'], entry['timestamp']] for entry in data2]

# Define the number of clusters (k) based on the expected number of most visited coordinates
k = 3

# Analyze Banorte Portal A
most_visited_coordinates1, results1, total_time_minutes1 = analyze_heatmap(coordinates1)

# Analyze Banorte Portal B
most_visited_coordinates2, results2, total_time_minutes2 = analyze_heatmap(coordinates2)

# Open a text file for writing
with open('heatmap_comparison_results.otd', 'w') as file:

    # Redirect the standard output to the text file
    import sys
    sys.stdout = file

    # Report the comparisons between the two heatmaps
    print('Comparison of Heatmap Results:')
    print('------------------------------------')
    print('Banorte Portal A:')
    print('Most visited coordinates:')
    for i, coord in enumerate(most_visited_coordinates1):
        average_time, frequency = results1[i]
        print(f'Coordinate {i+1}: X: {coord[0]}, Y: {coord[1]}, Average Time: {average_time:.2f} seconds, Frequency: {frequency}')
    print(f'Total time spent on the webpage: {total_time_minutes1:.2f} minutes')
    print('------------------------------------')
    print('Banorte Portal B:')
    print('Most visited coordinates:')
    for i, coord in enumerate(most_visited_coordinates2):
        average_time, frequency = results2[i]
        print(f'Coordinate {i+1}: X: {coord[0]}, Y: {coord[1]}, Average Time: {average_time:.2f} seconds, Frequency: {frequency}')
    print(f'Total time spent on the webpage: {total_time_minutes2:.2f} minutes')
    print('------------------------------------')

    # Perform comparisons between the heatmaps and report the differences

    # Set the threshold values
    max_time_difference = -2  # Maximum acceptable time difference in minutes

    # Compare the total time spent on the webpage
    time_difference = total_time_minutes2 - total_time_minutes1

    # Example comparison: Total time spent on the webpage
    if time_difference < max_time_difference:
        print(f'Banorte Portal B shows {-time_difference:.2f} minutes less time spent on the webpage compared to Banorte Portal A, indicating it is more efficient.')
    else:
        print(f'Banorte Portal A shows {-time_difference:.2f} minutes less time spent on the webpage compared to Banorte Portal B, indicating it is more efficient.')

# Perform other comparisons as needed
# ...

# Restore the standard output
sys.stdout = sys.__stdout__
