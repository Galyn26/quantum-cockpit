import os
import numpy as np
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
from qiskit.circuit.library import zz_feature_map
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

# 1. Authenticate via env
api_token = os.environ.get("IBM_QUANTUM_TOKEN") or os.environ.get("QISKIT_IBM_TOKEN")
service = QiskitRuntimeService(channel="ibm_quantum_platform", token=api_token)

# 2. Load tabular cellular data
X = np.load("data/cancer_features.npy")
patient_vector = X[0, :4] 

# 3. Build Feature Map and apply parameters
f_map = zz_feature_map(feature_dimension=4, reps=1, entanglement="linear")
parameterized_circuit = f_map.assign_parameters(patient_vector)
parameterized_circuit.measure_all()

# 4. Target Backend and Transpile abstract map to physical hardware gates
backend = service.least_busy(simulator=False, operational=True)
print(f"Targeting Physical QPU Backend: {backend.name}")

pass_manager = generate_preset_pass_manager(optimization_level=1, backend=backend)
isa_circuit = pass_manager.run(parameterized_circuit)

# 5. Submit to queue via SamplerV2 mode syntax
sampler = SamplerV2(mode=backend)
print("Submitting Transpiled Breast Cancer Workload to IBM Cloud...")
job = sampler.run([isa_circuit])
print(f"\n🚀 SUCCESS! Breast Cancer Job ID: {job.job_id}")
