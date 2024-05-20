import qiskit
from qiskit import QuantumCircuit, transpile, assemble
from qiskit.visualization import plot_histogram
from qiskit_aer import Aer
import numpy as np
import random


# Step 1: Generate a random initial guess
def generate_random_guess(size=4, colors=2):
    return [random.randint(0, colors-1) for _ in range(size)]

initial_guess = generate_random_guess()
print(f"Initial guess: {initial_guess}")

# Step 2: Create quantum and classical registers
num_bits = 4
qr = qiskit.QuantumRegister(num_bits, 'q')
cr = qiskit.ClassicalRegister(num_bits, 'c')
qc = QuantumCircuit(qr, cr)

# Step 3: Apply Hadamard gates to create superposition
for qubit in qr:
    qc.h(qubit)

# Step 4: Calculate Hamming distance and store in ancilla qubits
def calculate_hamming_distance(qc, initial_guess, num_bits):
    ancilla_qubits = qiskit.QuantumRegister(num_bits, 'a')
    qc.add_register(ancilla_qubits)
    
    for i in range(num_bits):
        qc.cx(qr[i], ancilla_qubits[i])
        if initial_guess[i] == 1:
            qc.x(ancilla_qubits[i])
    
    return qc

# Apply the function to calculate Hamming distance
calculate_hamming_distance(qc, initial_guess, num_bits)

# Step 5: Simulate the quantum circuit
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
# qobj = assemble(compiled_circuit)
results = simulator.run(compiled_circuit, shots=1024).result()
counts = results.get_counts()

print("Counts: ", counts)
plot_histogram(counts)
