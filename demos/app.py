# demos/app.py - QIM Local Demo
from src.qef_lite_scan import qef_lite_scan
from src.phi_proxy import calculate_phi_proxy
import torch

prompt = input("Enter prompt: ")
scan = qef_lite_scan(prompt)
if not scan["approved"]:
    print(scan)
    print("resubmit: true")
else:
    vector = torch.tensor([0.1, 0.8, 0.05, 0.05])
    phi = calculate_phi_proxy(vector)
    print(f"Approved. Phi: {phi:.3f}")
