import os
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit_ibm_runtime import QiskitRuntimeService

def execute_quantum_helloworld():
    print("\n[⚡] Initializing Quantum Hello World Pipeline...")

    # 1. Construct a 2-qubit entangled Bell State
    circuit = QuantumCircuit(2)
    circuit.h(0)     # Superposition gate on Qubit 0
    circuit.cx(0, 1) # Entanglement gate linking Qubit 0 and 1
    circuit.measure_all()

    # 2. Local Matrix Simulation using Mint's 16GB RAM
    print("[💻] Running local statevector matrix simulation on Host RAM...")
    sampler = StatevectorSampler()
    job = sampler.run([circuit])
    result = job.result()

    # Extract binary measurement statistics
    counts = result[0].data.meas.get_counts()
    print(f"[📊] Local Simulation Output Counts: {counts}")
    print("     (An ideal entanglement yields roughly equal distributions of '00' and '11')")

    # 3. Cloud Server Authentication Check
    token = os.getenv("IBM_QUANTUM_TOKEN")
    if token and token != "your_raw_token_here":
        try:
            print("[☁️] Authenticating with IBM Quantum Cloud Server...")
            # FIXED: Channel string updated to reflect modern Qiskit API specifications
            service = QiskitRuntimeService(channel="ibm_quantum_platform", token=token)
            least_busy = service.least_busy(simulator=False)
            print(f"[🎯] Authentication Success! Ready to scale. Least busy QPU: {least_busy.name}")
        except Exception as e:
            print(f"[❌] IBM Cloud Authentication failed: {e}")
    else:
        print("[⚠️] System running in localized simulation mode. No valid IBM_QUANTUM_TOKEN detected.")

if __name__ == "__main__":
    execute_quantum_helloworld()
