from sklearn.metrics import ndcg_score
import numpy as np

# list to rank 1
y_truth = [0, 1, 2, 3]
y_predict = [0, 1, 2, 3]
ndcg1 = ndcg_score([y_truth], [y_predict])
print(f'ndcg1 = {ndcg1}')


# list to rank 2
y_truth2 = [0, 1, 2, 3]
y_predict2 = [0.3, 0.1, 0.2, 0.0]
ndcg2 = ndcg_score([y_truth2], [y_predict2])
print(f'ndcg2 = {ndcg2}')


y_truth3 = [0, 1, 2, 3]
y_predict3 = [0.2, 0.1, 0.3, 0.4]
ndcg3 = ndcg_score([y_truth3], [y_predict3])
print(f'ndcg3 = {ndcg3}')

print(f'ndcg_mean = {np.mean([ndcg1, ndcg2, ndcg3])}')

# can do 3 list's NDCG togeter, compute mean 
ndcg = ndcg_score([y_truth, y_truth2, y_truth3], [y_predict, y_predict2, y_predict3])
print(f'ndcg = {ndcg}')
