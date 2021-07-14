import os
import pyphi
import numpy as np

pyphi.config.load_file(
    os.path.dirname(__file__) + '../config/pyphi_config_emd_tri.yml')

tpm = np.array([
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 0],
    [1, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 1, 1],
    [1, 0, 1, 0],
])

cm = np.array([
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0],
])
labels = ('A', 'B', 'C', 'D')
network = pyphi.Network(tpm, cm=cm, node_labels=labels)
state = (1, 0, 1, 0)
node_indices = (0, 1, 2, 3)
subsystem = pyphi.Subsystem(network, state, node_indices)
sia = pyphi.compute.sia(subsystem)
print("MIP: \n", sia.cut)
print("Phi: \n Φ = ", sia.phi)
print("Tiempo: \n", sia.time, "s")
