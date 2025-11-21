#this is for modern updated code 

import qiskit
from qiskit_aer import Aer

# Create circuit with 2 qubits and 2 classical bits
circuit = qiskit.QuantumCircuit(2,2)

# Apply a Hadamard gate to the first qubit
circuit.h(0)

#you dont need to manually add classical register already added in (2,2)

# Measure qubits into classical bits
circuit.measure([0,1], [0,1])

# Use Aer simulator
simulator = Aer.get_backend('qasm_simulator')
result = simulator.run(circuit).result()

# Get measurement results
counts = result.get_counts()
print(counts)
