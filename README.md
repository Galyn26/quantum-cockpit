# Quantum Cockpit: Hybrid Edge-Simulation Engine

A containerized quantum computing sandbox and cloud-orchestration edge node engineered to execute localized statevector simulations and scale execution workloads directly to remote quantum processing units (QPUs).

## Core System Architecture

*   **Execution Surface:** Linux Mint MATE (Orchestrated completely inside Docker container memory isolation).
*   **Target Edge Node:** Legacy x86-64-v1 hardware architecture equipped with 16GB of physical matrix-math runway.
*   **Cloud Orchestration Hub:** Cryptographic pipeline authenticating via the Qiskit Runtime API layer to physical IBM Quantum hardware processors.

## Current Milestones Verified

1.  **Instruction Set Abstraction:** Successfully pinned binary dependency frameworks (`numpy<2.4.0`) to run modern linear algebra pipelines without requiring `x86-64-v2` hardware instructions.
2.  **Entanglement Verification:** Executed a localized 2-qubit Bell State simulation tracking perfect `00` and `11` probability vector distributions within host memory bounds.
3.  **Active Cloud Link:** Successfully established an authenticated, secure connection over the internet, verifying real-time tracking metrics from active QPUs (e.g., `ibm_marrakesh`).

## Next Execution Phases

*   **Phase 1:** Ingest and downscale medical image tensor data arrays Utilizing **MedMNIST** to establish localized quantum-classifier pipelines.
*   **Phase 2:** Integrate molecular property datasets using **QM7** to test quantum chemical atomization tracking models.
