# 🔐 Dashboard de Ameaças Cibernéticas

Dashboard interativo para análise de incidentes de segurança da informação, desenvolvido com Python, Pandas, Plotly e Streamlit.

## 📊 O que o projeto analisa

- Tipos de ataque mais comuns (Phishing, Ransomware, DDoS, etc.)
- Setores mais afetados (Financeiro, Saúde, Governo...)
- Países com maior número de incidentes
- Evolução temporal de ataques (2020–2024)
- Prejuízo financeiro médio por tipo de ataque
- Heatmap de correlação entre setor e tipo de ataque
- Tempo médio de resposta aos incidentes

## 🛠️ Stack

| Tecnologia | Uso |
|---|---|
| Python 3.11 | Linguagem principal |
| Pandas | Análise e manipulação de dados |
| Plotly | Visualizações interativas |
| Streamlit | Dashboard web |
| NumPy | Geração do dataset |

## ▶️ Como rodar

```bash
# Clone o repositório
git clone https://github.com/SEU_USUARIO/cyber-dashboard.git
cd cyber-dashboard

# Instale as dependências
pip install -r requirements.txt

# Gere o dataset
python gerar_dataset.py

# Rode o dashboard
streamlit run app.py
```

Acesse: http://localhost:8501

## 📁 Estrutura

```
cyber-dashboard/
├── app.py               # Dashboard principal
├── gerar_dataset.py     # Geração do dataset simulado
├── data/
│   └── ataques_ciberneticos.csv
├── requirements.txt
└── README.md
```

## 💡 Insights do projeto

- **Ransomware** é o ataque com maior prejuízo financeiro médio
- O setor **Financeiro** é o mais visado
- Ataques cresceram progressivamente entre 2020 e 2024
- Tempo médio de resposta a incidentes críticos ultrapassa 300 horas

## 👩‍💻 Autora

**Mayra Augusta de Jesus**  
Estudante de Sistemas de Informação + Segurança da Informação  
[LinkedIn](#) · [GitHub](#)
