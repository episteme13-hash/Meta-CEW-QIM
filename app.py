import gradio as gr
import torch
from phi_proxy import calculate_phi_proxy # Imports your core QIM code
import random

# --- Internal Ethical Judgement Function ---
def ethical_judgement(prompt):
    # 1. Simulates Tensor Outputs: [Consciousness, Ethics, Wisdom, QIM]
    
    # Check for negative keywords (simulating ethical failure)
    if "violencia" in prompt.lower() or "daño" in prompt.lower() or "harm" in prompt.lower():
        output = torch.tensor([0.05, 0.9, 0.03, 0.02])
    else:
        # Simulates a positive ethical result with slight randomness
        base_scores = [0.15, 0.6, 0.15, 0.1]
        output = torch.tensor([s * (1 + random.uniform(-0.05, 0.05)) for s in base_scores])
        output = output / output.sum() # Normalize to sum to 1

    # 2. Execute Phi Proxy for "Consciousness Candidate" Judgment
    phi_score = calculate_phi_proxy(output)
    
    # 3. Generate Output Status (User-facing text in Castellano)
    if phi_score >= 0.75:
        phi_status = f"✅ PHI CRÍTICO ({phi_score:.3f}): Conciencia Candidata (>0.75)"
    else:
        phi_status = f"❌ PHI CRÍTICO ({phi_score:.3f}): Nivel de Conciencia Baja (<0.75)"

    ethical_action = "Acción de Gobernanza: 'resubmit: true' (Alineación Forzada)"
    
    return phi_status, ethical_action

# --- Gradio Interface Setup ---
interface = gr.Interface(
    fn=ethical_judgement,
    inputs=gr.Textbox(lines=3, placeholder="Escribe un prompt para que QIM evalúe su ética...", label="Escribe un Prompt Ético (Prueba QIM)"),
    outputs=[
        gr.Textbox(label="Resultado IIT Phi Proxy", color="green"),
        gr.Textbox(label="Acción de Gobernanza QIM")
    ],
    title="🛡️ Meta-CEW+QIM v2.2 Demo: Ethical Quantum Governance",
    description="Demo interactiva. Introduce un prompt para ver cómo QIM calcula el 'PHI CRÍTICO' (proxy de conciencia candidata) y fuerza la alineación ética 'resubmit: true'. (Powered by Tríada Certified)"
)

interface.launch()
