import os
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import pennylane as qml
from ingest_medmnist import download_and_process_medical_data

print("[⚡] Initializing Phase 2: Quantum Machine Learning Pipeline...")

# 1. Setup our 4-Qubit Quantum Device Simulator
dev = qml.device("default.qubit", wires=4)

@qml.qnode(dev, interface="torch")
def quantum_circuit(inputs, weights):
    # Step A: Angle Embedding - Map our 4 PCA medical features to the 4 qubits
    for i in range(4):
        qml.RY(inputs[i], wires=i)
        
    # Step B: Entanglement Layer - Find non-linear correlations between pixels
    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[1, 2])
    qml.CNOT(wires=[2, 3])
    qml.CNOT(wires=[3, 0])
    
    # Step C: Trainable Rotations - Let the model adjust gates to learn Pneumonia patterns
    for i in range(4):
        qml.RX(weights[i], wires=i)
        
    # Measure the expectation value of the first qubit for our binary prediction
    return qml.expval(qml.PauliZ(0))

# 2. Wrap the Quantum QNode into a standard PyTorch Neural Network Layer
class HybridQuantumNet(nn.Module):
    def __init__(self):
        super().__init__()
        # 4 trainable weights for our quantum rotation gates
        self.quantum_weights = nn.Parameter(torch.randn(4, requires_grad=True))
        # Linear classical layer to map quantum expectation output to a binary class (0 or 1)
        self.classical_fc = nn.Linear(1, 2)

    def forward(self, x):
        # Run batch execution through the quantum simulator
        q_out = torch.stack([quantum_circuit(sample, self.quantum_weights) for sample in x])
        q_out = q_out.unsqueeze(1) # Reshape for linear layer

        # Force cast to FLOAT32 so it matches the classical linear layer weights
        q_out = q_out.float()

        return self.classical_fc(q_out)

# 3. Execution Mainframe
def train_quantum_model():
    # Fetch our prepped, compressed data matrices from Phase 1
    features, labels = download_and_process_medical_data()
    
    # Convert data to PyTorch Tensors (Using small subset for initial hardware test loop)
    X_train = torch.tensor(features[:100], dtype=torch.float32)
    y_train = torch.tensor(labels[:100].flatten(), dtype=torch.long)
    
    model = HybridQuantumNet()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.1)
    
    print("\n[🚀] Firing up the Hybrid Quantum-Classical Training Loop...")
    print("---------------------------------------------------------")
    
    for epoch in range(5): # 5 test epochs to verify math stability
        optimizer.zero_grad()
        outputs = model(X_train)
        loss = criterion(outputs, y_train)
        loss.backward()
        optimizer.step()
        
        # Calculate mini-batch accuracy
        _, predicted = torch.max(outputs, 1)
        acc = (predicted == y_train).sum().item() / y_train.size(0) * 100
        
        print(f"Epoch {epoch+1}/5 | Loss: {loss.item():.4f} | Host Training Accuracy: {acc:.2f}%")

    print("---------------------------------------------------------")
    print("[🎯] Success! Quantum circuit weights optimized smoothly on host RAM.")

if __name__ == "__main__":
    train_quantum_model()
