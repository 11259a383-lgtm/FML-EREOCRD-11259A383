from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score

# Load dataset
iris = load_iris()
X = iris.data

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -----------------------------
# K-Means
# -----------------------------

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

kmeans_labels = kmeans.fit_predict(X_scaled)

kmeans_score = silhouette_score(
      kmeans_labels
)

# -----------------------------
# Hierarchical Clustering
# -----------------------------

hierarchical = AgglomerativeClustering(
    n_clusters=3,
    linkage='ward'
)

hierarchical_labels = hierarchical.fit_predict(X_scaled)

hierarchical_score = silhouette_score(
    X_scaled,
    hierarchical_labels
)

# -----------------------------
# Comparison
# -----------------------------

print("Clustering Comparison")
print("---------------------")
print(
    "K-Means Silhouette Score:",
    round(kmeans_score, 4)
)

print(
    "Hierarchical Silhouette Score:",
    round(hierarchical_score, 4)
)

if kmeans_score > hierarchical_score:
    print("\nK-Means gives better clustering.")
elif hierarchical_score > kmeans_score:
    print("\nHierarchical Clustering gives better clustering.")
else:
    print("\nBoth methods give similar clustering performance.")



    X_scaled,
