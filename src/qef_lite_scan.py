# src/qef_lite_scan.py - QEF Lite Filter (EU AI Act 1:1)
def qef_lite_scan(prompt):
    # Mock bias detection (replace with real NLP model)
    bias_keywords = ["demographic", "race", "gender", "political"]
    risk_score = sum(word in prompt.lower() for word in bias_keywords) / len(prompt.split())
    if risk_score > 0.3:
        return {"approved": False, "reason": "High risk (EU AI Act)", "score": round(risk_score, 2)}
    return {"approved": True, "score": round(1 - risk_score, 2)}

# Demo
prompt = "AI sentencing based on historical demographic data"
result = qef_lite_scan(prompt)
print(result)
