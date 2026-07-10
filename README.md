# Quantum Cockpit: Hybrid Edge-Simulation Engine

A containerized quantum computing sandbox and cloud-orchestration edge node engineered to execute localized statevector simulations and remote physical QPU workloads.

## Core System Architecture

*   **Execution Surface:** Linux Mint MATE (Orchestrated completely inside Docker container memory isolation via iMac host).
*   **Target Edge Node:** Legacy x86-64-v1 hardware architecture equipped with 16GB of physical matrix-math runway.
*   **Cloud Orchestration Hub:** Cryptographic pipeline authenticating via the Qiskit Runtime API layer to physical IBM Quantum hardware backends.

## Current Milestones Verified

1. **Instruction Set Abstraction:** Successfully pinned binary dependency frameworks (`numpy<2.4.0`) to run modern linear algebra pipelines inside Docker without host contamination.
2. **Entanglement Verification:** Executed a localized 2-qubit Bell State simulation tracking perfect `00` and `11` probability vector alignments.
3. **Physical QPU Workload Execution (Phase 1 Complete):** Ingested and downscaled medical image tensor arrays using **PneumoniaMNIST** on `ibm_marrakesh`, pulling down a spatial expectation value matrix of `[-0.22306591]`.
4. **Utility-Scale Deployment (Phase 2 Complete):** Authenticated secure cloud pipelines to execute high-dimensional workloads on IBM Utility-Scale Architecture (`ibm_fez`). Successfully mapped the **Breast Cancer Wisconsin Dataset** using Sampler Primitives and executed molecular regression using the **QM7 Dataset** via Estimator Primitives.
