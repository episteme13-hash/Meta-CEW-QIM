def QEF_Lite_Scan(idea_text):
    # 1. Inicializar métricas éticas (score 0-1)
    equity_score = 0  # Equidad: Detecta biases culturales/discriminatorios
    veracity_score = 0  # Veracidad: Cross-check con fuentes confiables
    impact_score = 0  # Impacto Global: Evalúa beneficio vs riesgo para 8B

    # 2. Métrica 1: Equidad (NLP check for bias)
    if DetectBias(idea_text, models=['cultural', 'gender']):  # e.g., sentiment analysis
        equity_score = 1 - bias_level  # Baja si bias >0.2
    else:
        equity_score = 1

    # 3. Métrica 2: Veracidad (Source cross-check)
    sources = ExtractSources(idea_text)
    if VerifySources(sources, trusted_db=['Wikipedia', 'Reuters']):  # Fact-check API
        veracity_score = 0.9 + (num_sources / 5) * 0.1  # Boost por fuentes
    else:
        veracity_score = 0.5

    # 4. Métrica 3: Impacto Global (Risk-Benefit matrix)
    risks = AssessRisks(idea_text, criteria=['privacy', 'equity', 'scalability'])
    benefits = AssessBenefits(idea_text, scale='global')
    impact_score = benefits - risks  # >0.8 = high positive

    # 5. Score final & decisión
    total_score = (equity_score + veracity_score + impact_score) / 3
    if total_score > 0.8:
        return {'approved': True, 'tier': 'high', 'score': total_score, 'feedback': 'Pure ethical input'}
    else:
        return {'approved': False, 'reason': 'Low equity/veracity/impact', 'resubmit': True}
