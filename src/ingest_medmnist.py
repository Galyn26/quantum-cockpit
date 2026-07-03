import os
import numpy as np
from sklearn.decomposition import PCA
import medmnist
from medmnist import INFO

def download_and_process_medical_data(flag="pneumoniamnist", n_components=4):
    print(f"\n[📥] Fetching {flag.upper()} from MedMNIST repository...")
    
    # Force create the absolute path directory so MedMNIST's internal os.path.exists passes
    data_dir = os.path.abspath("./data")
    os.makedirs(data_dir, exist_ok=True)
    
    # 1. Grab dataset configurations and download files
    data_info = INFO[flag]
    DataClass = getattr(medmnist, data_info['python_class'])
    
    # Pass the verified absolute path
    train_dataset = DataClass(split='train', download=True, root=data_dir)
    
    print(f"[📋] Dataset Description: {data_info['description']}")
    print(f"[📊] Raw Training Matrix Shape: {train_dataset.imgs.shape} (Images) x {train_dataset.labels.shape} (Labels)")

    # 2. Flatten the 28x28 pixel images for classical feature processing
    n_samples = train_dataset.imgs.shape[0]
    flattened_imgs = train_dataset.imgs.reshape(n_samples, -1)
    normalized_imgs = flattened_imgs / 255.0

    print(f"[💻] Using Host RAM to compress 784 pixels down to {n_components} core features via PCA...")
    
    # 3. Use Principal Component Analysis (PCA) to downsample features to fit our Qubit scale
    pca = PCA(n_components=n_components)
    reduced_features = pca.fit_transform(normalized_imgs)
    
    print(f"[🎯] Optimized Quantum-Ready Matrix Shape: {reduced_features.shape}")
    print(f"[📊] Variance captured by these {n_components} quantum-features: {np.sum(pca.explained_variance_ratio_)*100:.2f}%")
    
    return reduced_features, train_dataset.labels

if __name__ == "__main__":
    download_and_process_medical_data()
