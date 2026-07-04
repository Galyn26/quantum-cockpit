import os
import numpy as np
from sklearn.datasets import load_breast_cancer

# 1. Setup path alignment inside the container filesystem
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

# 2. Ingest the dataset natively via sklearn
print("Ingesting Breast Cancer Wisconsin Dataset...")
cancer_data = load_breast_cancer()

# X = Feature matrix (30 cellular characteristics)
# y = Target array (0 = Malignant, 1 = Benign)
X = cancer_data.data
y = cancer_data.target
feature_names = cancer_data.feature_names

print(f"\n--- DATASET SPECIFICATIONS ---")
print(f"Total Patient Cases: {X.shape[0]}")
print(f"Extracted Cellular Features per Case: {X.shape[1]}")
print(f"Target Diagnostic Categories: {np.unique(y)} (0: Malignant, 1: Benign)")

# 3. Target Case #0 as our localized pipeline injection profile
target_index = 0
patient_features = X[target_index]
patient_diagnosis = "Malignant" if y[target_index] == 0 else "Benign"

print(f"\n--- TARGET PATIENT PROFILE (ID: {target_index}) ---")
print(f"Clinical Diagnosis: {patient_diagnosis}")
print(f"Sample Continuous Metrics:")
for i in range(5):
    print(f"  - {feature_names[i]}: {patient_features[i]:.2f}")

# 4. Save features and labels locally for the QSVM template
np.save(os.path.join(DATA_DIR, "cancer_features.npy"), X)
np.save(os.path.join(DATA_DIR, "cancer_labels.npy"), y)
print(f"\n[SUCCESS] Staged tabular cellular arrays inside '{DATA_DIR}/'")
