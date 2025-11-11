# src/qim_quantum_v0.1.py - Quantum Veto Gate
from qiskit import QuantumCircuit, Aer, execute

def quantum_veto(risk_level):
    qc = QuantumCircuit(1)
    theta = risk_level * 3.14  # calibrate
    qc.rx(theta, 0)
    qc.measure_all()
    sim = Aer.get_backend('qasm_simulator')
    result = execute(qc, sim, shots=1).result()
    outcome = list(result.get_counts().keys())[0]
    return "veto" if outcome == '1' else "pass"

# Demo
print(quantum_veto(0.64))  # from JSON
