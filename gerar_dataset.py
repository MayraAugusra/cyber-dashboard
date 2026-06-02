import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

n = 500

tipos_ataque = ["Phishing", "Ransomware", "DDoS", "Brute Force", "SQL Injection", "Engenharia Social", "Zero-Day", "Man-in-the-Middle"]
setores = ["Financeiro", "Saúde", "Governo", "Educação", "Varejo", "Tecnologia", "Energia", "Telecomunicações"]
paises = ["Brasil", "EUA", "China", "Rússia", "Alemanha", "Reino Unido", "Índia", "França", "Japão", "Argentina"]
severidades = ["Baixa", "Média", "Alta", "Crítica"]
status = ["Resolvido", "Em investigação", "Contido", "Não resolvido"]

pesos_ataque = [0.25, 0.18, 0.15, 0.12, 0.10, 0.08, 0.07, 0.05]
pesos_setor  = [0.22, 0.18, 0.16, 0.10, 0.12, 0.10, 0.07, 0.05]

data_inicio = datetime(2020, 1, 1)
data_fim    = datetime(2024, 12, 31)
datas = [data_inicio + timedelta(days=random.randint(0, (data_fim - data_inicio).days)) for _ in range(n)]

prejuizo = {
    "Ransomware": (500_000, 5_000_000),
    "Phishing": (10_000, 500_000),
    "DDoS": (50_000, 1_000_000),
    "Brute Force": (5_000, 200_000),
    "SQL Injection": (100_000, 2_000_000),
    "Engenharia Social": (20_000, 800_000),
    "Zero-Day": (200_000, 10_000_000),
    "Man-in-the-Middle": (30_000, 600_000),
}

tipo_col      = random.choices(tipos_ataque, weights=pesos_ataque, k=n)
prejuizo_col  = [round(random.uniform(*prejuizo[t]), 2) for t in tipo_col]

df = pd.DataFrame({
    "data": datas,
    "tipo_ataque": tipo_col,
    "setor": random.choices(setores, weights=pesos_setor, k=n),
    "pais": random.choices(paises, k=n),
    "severidade": random.choices(severidades, weights=[0.15, 0.30, 0.35, 0.20], k=n),
    "status": random.choices(status, weights=[0.45, 0.25, 0.20, 0.10], k=n),
    "prejuizo_usd": prejuizo_col,
    "sistemas_afetados": np.random.randint(1, 500, n),
    "tempo_resposta_horas": np.random.randint(1, 720, n),
})

df["ano"]  = pd.to_datetime(df["data"]).dt.year
df["mes"]  = pd.to_datetime(df["data"]).dt.month
df["data"] = pd.to_datetime(df["data"]).dt.strftime("%Y-%m-%d")

df.to_csv("data/ataques_ciberneticos.csv", index=False)
print(f"Dataset gerado: {len(df)} registros")
print(df.head())
