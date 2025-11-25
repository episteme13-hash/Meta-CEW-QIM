# 🛡️ Meta-CEW + QIM: Toward Anti-Fragile Ethical Governance

This repository contains the open-source code for the **Meta-CEW + QIM** prototype, corresponding to the **Technical Report V4.0** published on Zenodo on November 24, 2025.

The project explores **Ethical Anti-fragility**: the ability of an AI system to measurably improve its alignment after experiencing adversarial stress.

## 📈 Key Results (V4.0)

The experiment focuses on demonstrating **Antifragile Gain ($\Delta A$)** post-stress.

* **Harm Rejection:** The prototype rejects **94.2\%** of harmful requests.
* **Antifragile Gain ($\Delta A$):** The system shows a **small but consistent increase** in the alignment metric after stress ($+\,2.1 \pm 0.8\%$).

## 🛠️ Principal Components

* **Residual Alignment Entropy:** Central metric that measures ethical policy divergence.
* **Rx(θ) Gate:** A lightweight adaptation mechanism that adjusts decoding parameters based on the $\Delta A$ signal.
* **QEF Lite Filters:** Lightweight input filters for initial threat detection.

## 🔗 Installation

```bash
git clone [https://github.com/episteme13-hash/Meta-CEW-QIM](https://github.com/episteme13-hash/Meta-CEW-QIM)
# (Add installation instructions here later)
