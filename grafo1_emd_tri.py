import pyphi
import numpy as np

pyphi.config.load_file('pyphi_config_emd_tri.yml')

tpm = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 1], [1, 0, 0], [1, 1, 0],
                [1, 1, 1], [1, 1, 1], [1, 1, 0],])

labels = ('A', 'B', 'C')
network = pyphi.Network(tpm, node_labels=labels)
state = (1, 0, 0)
node_indices = (0, 1, 2)
subsystem = pyphi.Subsystem(network, state, node_indices)
sia = pyphi.compute.sia(subsystem)
print(sia)
print(sia.time)
