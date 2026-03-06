# Simple feature importance demonstration for explainability
def get_feature_importance(weights, feature_names):
    importance = sorted(zip(feature_names, weights), key=lambda x: x[1], reverse=True)
    return importance

features = ["Income", "Credit Score", "Age", "Loan Amount"]
weights = [0.45, 0.35, 0.10, 0.10]
importance_list = get_feature_importance(weights, features)

print("Explainability - Feature Importance:")
for feature, weight in importance_list:
    print(f"{feature}: {weight*100}% influence")
