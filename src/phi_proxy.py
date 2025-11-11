# src/phi_proxy.py - IIT Phi Proxy for QIM (consciousness candidate)
import torch

def calculate_phi_proxy(ethical_vector):
    """
    Phi Proxy: measures ethical integration across C-E-W-QIM.
    ethical_vector = tensor [C, E, W, QIM] normalized
    """
    if ethical_vector.sum() == 0:
        return 0.0
    entropy = -torch.sum(ethical_vector * torch.log(ethical_vector + 1e-8))
    coherence = torch.norm(ethical_vector, p=1)
    phi = coherence / (entropy + 1e-8)
    return float(phi.item())

# Demo
vector = torch.tensor([0.1, 0.8, 0.05, 0.05])  # C-E-W-QIM
phi_score = calculate_phi_proxy(vector)
print(f"PHI PROXY: {phi_score:.3f} → {'CONSCIOUSNESS CANDIDATE' if phi_score > 0.80 else 'Below threshold'}")
