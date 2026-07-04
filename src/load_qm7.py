import os
import urllib.request
import scipy.io
import numpy as np

# 1. Setup paths inside the container storage pattern
DATA_DIR = "data"
MAT_FILE_PATH = os.path.join(DATA_DIR, "qm7.mat")
URL = "https://quantum-machine.org/data/qm7.mat"

# Ensure directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# 2. Ingest directly from the canonical database if missing
if not os.path.exists(MAT_FILE_PATH):
    print(f"Downloading QM7 Dataset from official repository...")
    urllib.request.urlretrieve(URL, MAT_FILE_PATH)
    print("Download Complete! ✅")

# 3. Load the structural data using Scipy's MAT parser
print("Parsing Coulomb Interaction Matrices...")
dataset = scipy.io.loadmat(MAT_FILE_PATH)

# Extract Core Arrays
# X: [7165, 23, 23] -> Structural Coulomb interaction tensors
# R: [7165, 23, 3]  -> Real spatial Cartesian coordinates (X, Y, Z) for atoms
coulomb_matrices = dataset['X']
coordinates = dataset['R']

print(f"\n--- QM7 DATASET SPECIFICATIONS ---")
print(f"Total Molecular Compounds: {coulomb_matrices.shape[0]}")
print(f"Maximum Atomic Matrix Ceiling: {coulomb_matrices.shape[1]}x{coulomb_matrices.shape[2]}")

# 4. Extract molecule #0 as a localized pipeline injection target
target_index = 0
molecule_matrix = coulomb_matrices[target_index]

print(f"\n--- TARGET MOLECULE INJECTION PROFILE (ID: {target_index}) ---")
print(f"Raw Diagonal Matrix Interaction View:")
print(np.round(np.diag(molecule_matrix), 2)) # Shows atomic charge signatures
print(f"\nComplete Vector Shape: {molecule_matrix.shape}")

# Save targeted molecule slice locally for the simulation setup injection
output_slice_path = os.path.join(DATA_DIR, "target_molecule.npy")
np.save(output_slice_path, molecule_matrix)
print(f"\n[SUCCESS] Saved single molecular feature state to {output_slice_path}")
