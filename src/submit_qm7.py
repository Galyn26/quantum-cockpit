import os
import numpy as np
from qiskit_ibm_runtime import QiskitRuntimeService, EstimatorV2
from qiskit.circuit.library import real_amplitudes
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

# 1. Authenticate via env
api_token = os.environ.get("IBM_QUANTUM_TOKEN") or os.environ.get("QISKIT_IBM_TOKEN")
service = QiskitRuntimeService(channel="ibm_quantum_platform", token=api_token)

# 2. Load and downscale to 4x4 matrix (which is exactly a 2-qubit space)
molecule_matrix = np.load("data/target_molecule.npy")
hamiltonian_matrix = molecule_matrix[:4, :4]

norm_factor = np.max(np.abs(hamiltonian_matrix))
if norm_factor > 0:
    hamiltonian_matrix /= norm_factor

observable = SparsePauliOp.from_operator(hamiltonian_matrix)

# 3. Build 2-qubit ansatz matching the matrix dimensions
ansatz = real_amplitudes(num_qubits=2, reps=2, entanglement="linear")

# 4. Target Backend and Transpile to ISA gates
backend = service.least_busy(simulator=False, operational=True)
print(f"Targeting Physical QPU Backend: {backend.name}")

pass_manager = generate_preset_pass_manager(optimization_level=1, backend=backend)
isa_circuit = pass_manager.run(ansatz)
isa_observable = observable.apply_layout(isa_circuit.layout)

# 5. Submit to queue via EstimatorV2 mode syntax
estimator = EstimatorV2(mode=backend)
initial_theta = np.random.uniform(0, np.pi, ansatz.num_parameters)

print("Submitting Transpiled QM7 Workload to IBM Cloud...")
job = estimator.run([(isa_circuit, isa_observable, initial_theta)])
print(f"\n🚀 SUCCESS! QM7 Job ID: {job.job_id}")
