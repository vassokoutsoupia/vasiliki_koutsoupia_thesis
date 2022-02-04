from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics.cluster import mutual_info_score
from sklearn.metrics.cluster import adjusted_mutual_info_score
from sklearn.metrics.cluster import rand_score
from sklearn.metrics.cluster import homogeneity_score
from sklearn.metrics.cluster import completeness_score


def print_metrics_cluster(method_name, ground_truth_labels, labels):
    mi_score_method = mutual_info_score(ground_truth_labels, labels)
    nmi_score_method = normalized_mutual_info_score(ground_truth_labels, labels)
    ami_score_method = adjusted_mutual_info_score(ground_truth_labels, labels)
    rand_score_method = rand_score(ground_truth_labels, labels)
    hom_score_method = homogeneity_score(ground_truth_labels, labels)
    com_score_method = completeness_score(ground_truth_labels, labels)
    metrics = {'mi_score': mi_score_method,
               'nmi_score': nmi_score_method,
               'ami_score': ami_score_method,
               'rand_score': rand_score_method,
               'how_score': hom_score_method,
               'com_score': com_score_method}

    print('---------')
    print(f'Metrics for clustering with {method_name}')
    print(f'Mutual Information (MI) score ({method_name}): {mi_score_method}')
    print(f'Normalized Mutual Information (NMI) score ({method_name}): {nmi_score_method}')
    print(f'Adjusted Mutual Information (AMI) score ({method_name}): {ami_score_method}')
    print(f'Rand score ({method_name}): {rand_score_method}')
    print(f'Homogeneity score ({method_name}): {hom_score_method}')
    print(f'Completeness score ({method_name}): {com_score_method}')
    return metrics


def clusters_to_labels(clusters):
    num_of_clusters = len(clusters)
    num_of_nodes = sum([len(c) for c in clusters])
    labels = [None] * num_of_nodes

    for i, c in enumerate(clusters):
        for node in c:
            labels[node] = i

    return labels


def labels_to_clusters(labels):
    num_of_nodes = len(labels)
    num_of_clusters = len(set(labels))

    clusters = []

    for i in range(num_of_clusters):
        clusters.append(list())

    for i in range(num_of_nodes):
        cluster_id = labels[i]
        clusters[cluster_id].append(i)

    return clusters

