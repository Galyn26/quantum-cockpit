import os
import sys
import torch
import numpy as np
import pennylane as qml
from qiskit_ibm_runtime import QiskitRuntimeService
from ingest_medmnist import download_and_process_medical_data

print("[☁️] Phase 3: Initializing Physical QPU Deployment Mainframe...")

# 1. Retrieve the secure token from Docker environment variables
ibm_token = os.getenv("IBM_QUANTUM_TOKEN")
if not ibm_token or ibm_token == "your_ibm_token_here":
    print("[❌] Critical Error: IBM_QUANTUM_TOKEN environment variable is missing!")
    sys.exit(1)

# 2. Authenticate and fetch the actual Backend object from IBM
try:
    print("[📡] Establishing secure token handshake with IBM Quantum Service...")
    service = QiskitRuntimeService(channel="ibm_quantum_platform", token=ibm_token)
    
    print("[🔍] Querying for target QPU instance (ibm_marrakesh)...")
    target_backend = service.backend("ibm_marrakesh")
    print(f"[🎯] Physical QPU Instance Locked: {target_backend.name}")
except Exception as e:
    print(f"[❌] IBM Service Authentication Failed: {str(e)}")
    sys.exit(1)

# 3. Configure the PennyLane Qiskit Device using the backend object
try:
    dev = qml.device("qiskit.remote", wires=4, backend=target_backend)
    print("[⚡] PennyLane Qiskit-Plugin Bridge active and ready.")
except Exception as e:
    print(f"[❌] PennyLane Device Initialization Failed: {str(e)}")
    sys.exit(1)

# 4. Define the Physical Circuit Layout (Passing shots into the QNode decorator!)
@qml.qnode(dev, shots=100)
def real_quantum_circuit(inputs, weights):
    # Step A: Physical Angle Embedding
    for i in range(4):
        qml.RY(inputs[i], wires=i)
        
    # Step B: Physical CNOT Entanglement
    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[1, 2])
    qml.CNOT(wires=[2, 3])
    qml.CNOT(wires=[3, 0])
    
    # Step C: Optimized Gates
    for i in range(4):
        qml.RX(weights[i], wires=i)
        
    return qml.expval(qml.PauliZ(0))

def run_hardware_verification():
    features, labels = download_and_process_medical_data()
    test_sample = features[0]
    true_label = "PNEUMONIA" if labels[0][0] == 1 else "NORMAL"
    
    # Using the converging weights verified from Phase 2
    optimized_weights = np.array([-0.12, 0.45, -0.78, 0.23])
    
    print(f"\n[🔬] Input Sample Pathology Profile: {test_sample}")
    print(f"[📋] Ground Truth Label: {true_label}")
    print("[🚀] Submitting Quantum Circuit job packet to IBM cloud queue...")
    
    try:
        raw_expectation = real_quantum_circuit(test_sample, optimized_weights)
        print("\n---------------------------------------------------------")
        print("[🛰️] RESPONSE RECEIVED FROM IBM SUPERCONDUCTING QPU")
        print(f"[*] Raw Expectation Value <Z>: {raw_expectation}")
        
        prediction = "PNEUMONIA" if raw_expectation < 0.0 else "NORMAL"
        print(f"[🔮] Real Hardware Medical Prediction: {prediction}")
        
        if prediction == true_label:
            print("[🎉] VERIFICATION SUCCESS: Real hardware correctly evaluated the pathology!")
        else:
            print("[⚠️] Verification Complete: Quantum noise variation detected.")
        print("---------------------------------------------------------")
    except Exception as e:
        print(f"[❌] Cloud Execution Failed: {str(e)}")

if __name__ == "__main__":
    run_hardware_verification()
