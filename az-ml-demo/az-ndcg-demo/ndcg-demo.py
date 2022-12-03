from sklearn.metrics import ndcg_score

y_truth = [0,1,2,3]
y_predict = [0,1,2,3]
ndcg = ndcg_score([y_truth], [y_predict])
print(f'ndcg = {ndcg}')