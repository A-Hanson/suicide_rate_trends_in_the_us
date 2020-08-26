import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

from grouping_functions import aggregate_county, aggregate_county_males

plt.style.use('fivethirtyeight')

def silhouette_calc(df, n):
    range_n_clusters = list(range(2, n))
    print("Cluster Numbers: \n", range_n_clusters)
    scores = []
    for n_clusters in range_n_clusters:
        k_means = KMeans(n_clusters = n_clusters, init='k-means++')
        predictions = k_means.fit_predict(df)
        centers = k_means.cluster_centers_
        scores.append(silhouette_score(df, predictions))
    zips = list(zip(range_n_clusters, scores))
    #df = pd.DataFrame(zips, columns = ['n_clusters', 'score'])
    return zips


if __name__ == "__main__":
    agg_county_sil_scores = silhouette_calc(aggregate_county_males, 10)
    # for n_clusters, score in agg_county_sil_scores:
    #     print("For n_clusters = {}, silhouette score is {:.2f}".format(n_clusters, score))
    fig, ax = plt.subplot(1,1, figsize = (10,10))

    for n_clusters, score in agg_county_sil_scores:
        ax = plt.plot(n_clusters, score)

    



