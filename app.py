import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ── Configuração da página ────────────────────────────────────────────────────
st.set_page_config(
    page_title="Cyber Threat Dashboard",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── CSS customizado ───────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #0d1117; }
    .stApp { background-color: #0d1117; color: #e6edf3; }
    .metric-card {
        background: linear-gradient(135deg, #161b22, #21262d);
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
    }
    .metric-value { font-size: 2rem; font-weight: bold; color: #58a6ff; }
    .metric-label { font-size: 0.85rem; color: #8b949e; margin-top: 4px; }
    h1, h2, h3 { color: #e6edf3 !important; }
    .sidebar .sidebar-content { background-color: #161b22; }
</style>
""", unsafe_allow_html=True)

# ── Carregar dados ────────────────────────────────────────────────────────────
@st.cache_data
def carregar_dados():
    df = pd.read_csv("data/ataques_ciberneticos.csv", parse_dates=["data"])
    return df

df = carregar_dados()

# ── Sidebar — filtros ─────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🔐 Filtros")
    st.markdown("---")

    anos = sorted(df["ano"].unique())
    ano_sel = st.multiselect("📅 Ano", anos, default=anos)

    tipos = sorted(df["tipo_ataque"].unique())
    tipo_sel = st.multiselect("⚔️ Tipo de Ataque", tipos, default=tipos)

    setores = sorted(df["setor"].unique())
    setor_sel = st.multiselect("🏢 Setor", setores, default=setores)

    severidades = sorted(df["severidade"].unique())
    sev_sel = st.multiselect("🚨 Severidade", severidades, default=severidades)

    st.markdown("---")
    st.markdown("**Mayra Augusta de Jesus**")
    st.markdown("*Sistemas de Informação + Segurança*")

# ── Aplicar filtros ───────────────────────────────────────────────────────────
df_f = df[
    df["ano"].isin(ano_sel) &
    df["tipo_ataque"].isin(tipo_sel) &
    df["setor"].isin(setor_sel) &
    df["severidade"].isin(sev_sel)
]

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("# 🔐 Dashboard de Ameaças Cibernéticas")
st.markdown("Análise de incidentes de segurança — 2020 a 2024")
st.markdown("---")

# ── KPIs ──────────────────────────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{len(df_f):,}</div>
        <div class="metric-label">Total de Incidentes</div>
    </div>""", unsafe_allow_html=True)

with col2:
    prejuizo_total = df_f["prejuizo_usd"].sum()
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">$ {prejuizo_total/1_000_000:.1f}M</div>
        <div class="metric-label">Prejuízo Total (USD)</div>
    </div>""", unsafe_allow_html=True)

with col3:
    criticos = len(df_f[df_f["severidade"] == "Crítica"])
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value" style="color:#f85149">{criticos}</div>
        <div class="metric-label">Ataques Críticos</div>
    </div>""", unsafe_allow_html=True)

with col4:
    tempo_medio = df_f["tempo_resposta_horas"].mean()
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value" style="color:#3fb950">{tempo_medio:.0f}h</div>
        <div class="metric-label">Tempo Médio de Resposta</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Linha 1: Ataques por tipo + Evolução temporal ─────────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.markdown("### ⚔️ Tipos de Ataque")
    contagem = df_f["tipo_ataque"].value_counts().reset_index()
    contagem.columns = ["tipo_ataque", "quantidade"]
    fig = px.bar(
        contagem, x="quantidade", y="tipo_ataque",
        orientation="h", color="quantidade",
        color_continuous_scale="Blues",
        template="plotly_dark"
    )
    fig.update_layout(
        paper_bgcolor="#161b22", plot_bgcolor="#161b22",
        showlegend=False, coloraxis_showscale=False,
        margin=dict(l=0, r=0, t=10, b=0), height=320
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("### 📈 Evolução de Ataques por Ano")
    evolucao = df_f.groupby("ano").size().reset_index(name="quantidade")
    fig2 = px.line(
        evolucao, x="ano", y="quantidade",
        markers=True, template="plotly_dark",
        color_discrete_sequence=["#58a6ff"]
    )
    fig2.update_traces(line=dict(width=3), marker=dict(size=8))
    fig2.update_layout(
        paper_bgcolor="#161b22", plot_bgcolor="#161b22",
        margin=dict(l=0, r=0, t=10, b=0), height=320
    )
    st.plotly_chart(fig2, use_container_width=True)

# ── Linha 2: Setores + Mapa de severidade ─────────────────────────────────────
col3, col4 = st.columns(2)

with col3:
    st.markdown("### 🏢 Setores Mais Afetados")
    setores_count = df_f["setor"].value_counts().reset_index()
    setores_count.columns = ["setor", "quantidade"]
    fig3 = px.pie(
        setores_count, values="quantidade", names="setor",
        hole=0.45, template="plotly_dark",
        color_discrete_sequence=px.colors.sequential.Blues_r
    )
    fig3.update_layout(
        paper_bgcolor="#161b22",
        margin=dict(l=0, r=0, t=10, b=0), height=320
    )
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.markdown("### 🌍 Países com Mais Incidentes")
    paises_count = df_f["pais"].value_counts().reset_index()
    paises_count.columns = ["pais", "quantidade"]
    fig4 = px.bar(
        paises_count, x="pais", y="quantidade",
        color="quantidade", color_continuous_scale="Reds",
        template="plotly_dark"
    )
    fig4.update_layout(
        paper_bgcolor="#161b22", plot_bgcolor="#161b22",
        showlegend=False, coloraxis_showscale=False,
        margin=dict(l=0, r=0, t=10, b=0), height=320,
        xaxis_tickangle=-30
    )
    st.plotly_chart(fig4, use_container_width=True)

# ── Linha 3: Prejuízo por tipo + Heatmap ──────────────────────────────────────
col5, col6 = st.columns(2)

with col5:
    st.markdown("### 💸 Prejuízo Médio por Tipo de Ataque (USD)")
    prejuizo_tipo = df_f.groupby("tipo_ataque")["prejuizo_usd"].mean().sort_values(ascending=True).reset_index()
    fig5 = px.bar(
        prejuizo_tipo, x="prejuizo_usd", y="tipo_ataque",
        orientation="h", color="prejuizo_usd",
        color_continuous_scale="Oranges",
        template="plotly_dark"
    )
    fig5.update_layout(
        paper_bgcolor="#161b22", plot_bgcolor="#161b22",
        coloraxis_showscale=False,
        margin=dict(l=0, r=0, t=10, b=0), height=320
    )
    st.plotly_chart(fig5, use_container_width=True)

with col6:
    st.markdown("### 🔥 Heatmap: Setor × Tipo de Ataque")
    heat = df_f.groupby(["setor", "tipo_ataque"]).size().unstack(fill_value=0)
    fig6 = px.imshow(
        heat, color_continuous_scale="Blues",
        template="plotly_dark", aspect="auto"
    )
    fig6.update_layout(
        paper_bgcolor="#161b22",
        margin=dict(l=0, r=0, t=10, b=0), height=320
    )
    st.plotly_chart(fig6, use_container_width=True)

# ── Tabela de dados ───────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("### 📋 Registros de Incidentes")
colunas = ["data", "tipo_ataque", "setor", "pais", "severidade", "status", "prejuizo_usd", "sistemas_afetados"]
st.dataframe(
    df_f[colunas].sort_values("data", ascending=False).head(50),
    use_container_width=True,
    hide_index=True
)

st.markdown("---")
st.markdown("<center style='color:#8b949e'>Mayra Augusta de Jesus · Sistemas de Informação + Segurança da Informação · 2025</center>", unsafe_allow_html=True)
