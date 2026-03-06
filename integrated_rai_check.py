# Holistic check for RAI principles
def run_rai_audit(model_metrics):
    checks = {
        "Robustness": model_metrics['accuracy_stability'] > 0.9,
        "Fairness": model_metrics['demographic_parity'] > 0.8,
        "Privacy": model_metrics['data_anonymized'] == True,
        "Explainability": model_metrics['has_feature_importance'] == True
    }
    
    passed = all(checks.values())
    return passed, checks

metrics = {
    'accuracy_stability': 0.95,
    'demographic_parity': 0.85,
    'data_anonymized': True,
    'has_feature_importance': True
}

success, results = run_rai_audit(metrics)
print(f"Overall RAI Compliance: {'PASSED' if success else 'FAILED'}")
print(results)
