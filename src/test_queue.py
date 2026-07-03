from qiskit_ibm_runtime import QiskitRuntimeService

try:
    service = QiskitRuntimeService(channel="ibm_quantum_platform", token="xzqu2Dew72my312-8S8aneBdQPIKNBbRWYqv2sHgVBLU")
    
    # Query the raw job details directly from the service client backend
    raw_job_data = service.backend.job("d942vfcql68s73c91je0")
    
    print("\n================================")
    print(f"Status: {raw_job_data.get('status')}")
    print(f"Info: {raw_job_data.get('queue_info', 'No direct queue metrics matching key')}")
    # Let's inspect the whole dictionary structure to find where they hid it
    print(f"Raw Keys Available: {list(raw_job_data.keys())}")
    print("================================\n")
except Exception as e:
    print(f"Error: {e}")
