import random

data = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(50)]

k = 3

centroids = random.sample(data, k)

max_iterations = 100

for _ in range(max_iterations):
    clusters = {i: [] for i in range(k)}
    for point in data:
        distances = [((point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2) ** 0.5 for center in centroids]
        closest_cluster = distances.index(min(distances))
        clusters[closest_cluster].append(point)

    new_centers = []
    for cluster_points in clusters.values():
        if cluster_points:
            mean_x = sum(point[0] for point in cluster_points) / len(cluster_points)
            mean_y = sum(point[1] for point in cluster_points) / len(cluster_points)
            new_centers.append((mean_x, mean_y))
        else:
            new_centers.append(centroids[random.randint(0, k - 1)])

    if new_centers == centroids:
        break

    centroids = new_centers

for i, center in enumerate(centroids):
    print(f"Cluster {i + 1} center: {center}")