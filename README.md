# Quantum Cockpit: Hybrid Edge-Simulation Engine

A containerized quantum computing sandbox and cloud-orchestration edge node engineered to execute localized statevector simulations and remote physical QPU workloads.

## 🚀 Quickstart: Setup & Physical QPU Execution

Because this engine runs entirely within containerized memory isolation via Docker, you do not need to manage complex local Python environments or worry about conflicting dependency versions. 

### 📋 Prerequisites
* **Docker & Docker Compose** installed on your host system.
* An **IBM Quantum Platform Account** (with a valid API Token from [quantum.ibm.com](https://quantum.ibm.com/)).

---

### 1. Clone & Environment Configuration

Clone the engine to your local node and navigate to the project root:
```bash
git clone https://github.com/Galyn26/quantum-cockpit.git
cd quantum-cockpit
```

To authenticate your jobs securely with IBM's superconducting backends without hardcoding credentials, initialize your environment variable configuration. Create a .env file in the root directory (or pass it directly to the container runtime):
```
IBM_QUANTUM_TOKEN="your_actual_ibm_quantum_token_here"
```
### 2. Build the Isolated Container Stack

Spin up the edge engine orchestration layer. This step automatically installs the pinned linear algebra frameworks and Qiskit runtimes inside an isolated environment:

```bash
docker-compose up -d --build
```

### 3. Executing Datasets & Processing Real Workloads

Once the container runtime is live, you can enter the container surface or trigger execution commands directly to stream datasets, construct feature maps, and queue jobs on physical hardware backends.

🩻 Run Medical Image Mapping (PneumoniaMNIST)

To ingest classical chest X-ray tensors, normalize the array boundaries, and execute the quantum feature map ansatz:
```
docker-compose exec quantum-engine python src/ingest_medmnist.py
docker-compose exec quantum-engine python src/main.py
```
🧬 Submit Breast Cancer Classification Workloads

To map high-dimensional clinical diagnostic data profiles onto physical qubits and submit Sampler Primitives to an active utility-scale bus:
```
docker-compose exec quantum-engine python src/submit_cancer.py
```
🧪 Submit QM7 Molecular Regression Models

To map Coulomb matrices onto physical hardware instances to estimate electronic ground-state energy configurations via Estimator Primitives:
```
docker-compose exec quantum-engine python src/submit_qm7.py
```

### 4. Fetching Async Hardware Results

Physical hardware executions are handled via remote cloud queues. Once your Job ID statuses transition to complete on your IBM Quantum Dashboard, run the asynchronous tracking utilities to fetch, parse, and save the finalized quantum probability distribution matrix:

```
docker-compose exec quantum-engine python src/fetch_production_results.py
```

## Core System Architecture

*   **Execution Surface:** Linux Mint MATE (Orchestrated completely inside Docker container memory isolation via iMac host).
*   **Target Edge Node:** Legacy x86-64-v1 hardware architecture equipped with 16GB of physical matrix-math runway.
*   **Cloud Orchestration Hub:** Cryptographic pipeline authenticating via the Qiskit Runtime API layer to physical IBM Quantum hardware backends.

## Current Milestones Verified

1. **Instruction Set Abstraction:** Successfully pinned binary dependency frameworks (`numpy<2.4.0`) to run modern linear algebra pipelines inside Docker without host contamination.
2. **Entanglement Verification:** Executed a localized 2-qubit Bell State simulation tracking perfect `00` and `11` probability vector alignments.
3. **Physical QPU Workload Execution (Phase 1 Complete):** Ingested and downscaled medical image tensor arrays using **PneumoniaMNIST** on `ibm_marrakesh`, pulling down a spatial expectation value matrix of `[-0.22306591]`.
4. **Utility-Scale Deployment (Phase 2 Complete):** Authenticated secure cloud pipelines to execute high-dimensional workloads on IBM Utility-Scale Architecture (`ibm_fez`). Successfully mapped the **Breast Cancer Wisconsin Dataset** using Sampler Primitives and executed molecular regression using the **QM7 Dataset** via Estimator Primitives.
