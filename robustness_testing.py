import numpy as np

# Simulating model robustness by adding noise to input data
def test_model_robustness(model_output, noise_level=0.1):
    noise = np.random.normal(0, noise_level, model_output.shape)
    perturbed_output = model_output + noise
    stability_score = 1 - np.mean(np.abs(perturbed_output - model_output))
    return stability_score

original_predictions = np.array([0.9, 0.1, 0.85, 0.2])
score = test_model_robustness(original_predictions)
print(f"Model Stability Score: {score:.2f}")
