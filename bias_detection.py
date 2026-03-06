import pandas as pd

# Checking for Disparate Impact (Bias detection)
def check_disparate_impact(data, group_col, outcome_col):
    group_a = data[data[group_col] == 'Group A'][outcome_col].mean()
    group_b = data[data[group_col] == 'Group B'][outcome_col].mean()
    disparate_impact = group_a / group_b if group_b != 0 else 0
    return disparate_impact

data = pd.DataFrame({
    'Group': ['Group A', 'Group A', 'Group B', 'Group B'],
    'Hired': [1, 0, 1, 1]
})

di_ratio = check_disparate_impact(data, 'Group', 'Hired')
print(f"Disparate Impact Ratio: {di_ratio:.2f}")
if di_ratio < 0.8:
    print("Potential Bias Detected (below 80% rule)")
