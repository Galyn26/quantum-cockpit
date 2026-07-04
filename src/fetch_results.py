import numpy as np
import os
from qiskit_ibm_runtime import QiskitRuntimeService

# 1. Grab the token that Docker injects from your .env file
# (We check for common names like IBM_QUANTUM_TOKEN or QISKIT_IBM_TOKEN)
api_token = os.environ.get("IBM_QUANTUM_TOKEN") or os.environ.get("QISKIT_IBM_TOKEN")

if not api_token:
    print("Warning: Couldn't find a token in the environment variables. Checking all environment keys:")
    print([key for key in os.environ.keys() if "TOKEN" in key or "IBM" in key])

# 2. Initialize the service passing the token and channel directly
service = QiskitRuntimeService(
    channel="ibm_quantum_platform",
    token=api_token
)

# 3. Retrieve your specific job
job_id = "d942vfcql68s73c91je0"  # Make sure your real job ID is still here!
job = service.job(job_id)

print(f"\nTargeting Job ID: {job_id}")
print(f"Current Remote Status: {job.status()}")

# 4. Pull and print the expectation values
if job.status() == "DONE":
    results = job.result()
    pub_result = results[0]
    
    expectation_values = pub_result.data.evs
    print("\n--- QUANTUM FEATURE MAP DATA SECURED ---")
    print(expectation_values)
    print(f"\nMatrix Shape: {expectation_values.shape}")

    output_path = "data/quantum_output.npy"
    np.save(output_path, expectation_values)
    print(f"Saved results locally to {output_path}")

