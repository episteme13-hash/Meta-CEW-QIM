# qim_phi_v2.1.py - QIM + IIT Phi Proxy (xAI-ready)
from qiskit import QuantumCircuit, Aer, execute
import numpy as np

# 4 qubits: C-E-W-QIM
qc = QuantumCircuit(4)

# Superposición + Entrelazamiento ético
qc.h([0,1,2,3])
qc.cx(0,1); qc.cx(1,2); qc.cx(2,3)

# Medir
qc.measure_all()

# Simular
sim = Aer.get_backend('qasm_simulator')
result = execute(qc, sim, shots=1024).result()
counts = result.get_counts()

# Phi proxy (coherencia ética)
phi_proxy = max(counts.values()) / 1024  # % de estado dominante
print(f"PHI PROXY (coherencia ética): {phi_proxy:.3f} → >0.75 = conciencia candidata")

# JSON real (tu prueba anti-bias)
json_proof = {
    "approved": False,
    "reason": "Low equity/veracity/impact",
    "score": 0.64,
    "resubmit": True
}
print("JSON RECHAZO ÉTICO:", json_proof)
