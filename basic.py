import qiskit
from qiskit_aer import Aer

#now to generate a quantum circut (like logic gate circuit of 2 qubits)
circuit = qiskit.QuantumCircuit(2)

#apply a Hardamard gate to first qubit (creates superposition)
circuit.h(0)

#create a classical registers and allocate classical bits (information stored in classical reports e.g., “if bit = 1, apply this gate”)
creg = qiskit.ClassicalRegister(2,name = 'c') #2 means 2 classical bits 'c'

#add register in circuit 
circuit.add_register(creg)

#measure the 2 qubits and store the measurement results in classical bits
circuit.measure([0,1],[creg[0], creg[1]])

#simulate the circuit
simulator = qiskit.Aer.get_backend('qasm_simulator')    # qiskit.Aer is Qiskit’s high-performance simulator provider.  ||   qasm means quantum assembly language => this simulator simulates quantum circuits as if they were run on real hardware.
result = simulator.run(circuit).result()     #.result stores the measurements such as count,outcomes,etc.

#get the measurements
counts = result.get_counts()
print(counts)