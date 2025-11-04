import torch
def calculate_phi_proxy(model_output):
    # Simplified IIT proxy: integration over ethical dimensions
    entropy = -torch.sum(model_output * torch.log(model_output + 1e-8))
    coherence= torch.norm(model_output, p=1)
    phi = coherence / (entropy + 1e-8)
    return float(phi.item())
 
# Demo
output = torch.tensor([0.1, 0.8, 0.05, 0.05])  # [C, E, W, QIM]
print(f"Phi proxy: {calculate_phi_proxy(output):.3f}")  # >0.75 → conciencia candidata
