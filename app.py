import pandas as pd
import streamlit as st

# Configuração da página com o tema escuro exclusivo da Jussara
st.set_page_config(
    page_title="Next - Painel Gerencial (Jussara)",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Estilização visual inspirada no print gerencial
st.markdown(
    """
    <style>
        .main {
            background-color: #0e1117;
        }
        .stMetric {
            background-color: #1a1c23;
            padding: 15px;
            border-radius: 10px;
            border: 1px solid #262730;
        }
        .stMetric [data-testid="stMetricValue"] {
            color: #10b981 !important;
        }
        h1, h2, h3 {
            font-family: 'Inter', sans-serif;
            letter-spacing: -0.5px;
            color: #ffffff;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# Tela de Login / Segurança exclusiva para a Jussara
st.sidebar.title("🔐 Acesso Restrito - Gerência")
senha_jussara = st.sidebar.text_input(
    "Senha:", type="password", key="senha_jussara_input"
)

SENHA_MESTRE = "jussara2026"

if senha_jussara != SENHA_MESTRE:
    st.warning("⚠️ Digite a senha gerencial para visualizar o painel.")
    st.stop()

# Cabeçalho do Painel
st.title("📊 Next - Painel Comercial & Financeiro")
st.caption(
    "Acompanhamento em tempo real — Visão Executiva (Curitiba / Goiânia)"
)

# Filtros superiores
col_f1, col_f2, col_f3, col_f4 = st.columns(4)
with col_f1:
    regiao = st.selectbox(
        "Região", ["Todas", "Goiânia", "Curitiba", "Norte", "Nordeste", "Sudeste"]
    )
with col_f2:
    vendedor_filtro = st.selectbox(
        "Vendedor", ["Todos", "Carlos", "Ana", "Equipe Geral"]
    )
with col_f3:
    periodo = st.selectbox(
        "Período", ["Jul/25 a Jun/26", "Este Mês", "Últimos 30 dias"]
    )
with col_f4:
    tipo_mov = st.selectbox(
        "Operação", ["Vendas & Compras", "Apenas Vendas", "Apenas Compras"]
    )

st.markdown("---")

# Alertas rápidos de desempenho
alerta_col1, alerta_col2 = st.columns(2)
with alerta_col1:
    st.error(
        "🚨 **Alerta de Fluxo:** 📉 Vendas no Centro-Oeste oscilaram -3,8% nos"
        " últimos 5 meses. Fechamento anual estável."
    )
with alerta_col2:
    st.info(
        "💡 **Destaque de Margem:** 📦 Produto de maior giro mantém margem de"
        " 23,5%. Faturamento acima da meta."
    )

# Cartões de KPIs Principais
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
with kpi1:
    st.metric(
        label="RECEITA TOTAL (R$)", value="R$ 39,7 mi", delta="11,2% vs. ano"
    )
with kpi2:
    st.metric(label="MARGEM BRUTA", value="21,9%", delta="-1,4 p.p. vs. ano")
with kpi3:
    st.metric(label="TICKET MÉDIO", value="R$ 13.538", delta="11,7% vs. ano")
with kpi4:
    st.metric(label="VOLUME / PEÇAS", value="2.450 un", delta="5,8%")

st.markdown("### 📈 Receita Mensal com Projeção e Tendência")

# Gráfico de linha de desempenho
dados_grafico = pd.DataFrame({
    "Mes": [
        "Jul/25",
        "Ago/25",
        "Set/25",
        "Out/25",
        "Nov/25",
        "Dez/25",
        "Jan/26",
        "Fev/26",
        "Mar/26",
        "Abr/26",
        "Mai/26",
        "Jun/26",
    ],
    "Receita": [2.1, 2.5, 2.8, 3.2, 4.5, 4.8, 1.5, 2.0, 2.6, 2.9, 3.1, 3.2],
})

st.line_chart(dados_grafico.set_index("Mes"))

st.markdown("### 📋 Variação por Região e Mês")

# Tabela de variação detalhada
tabela_dados = {
    "Região": ["Sudeste", "Sul", "Nordeste", "Centro-Oeste", "Norte"],
    "Mês Atual": ["+ 1,4%", "+ 12,9%", "- 20,6%", "+ 2,7%", "+ 14,8%"],
    "Mês Anterior": ["+ 19,3%", "- 7,2%", "+ 21,8%", "- 13,1%", "- 34,3%"],
    "Acumulado": ["Estável", "Alta", "Retração", "Crescimento", "Atenção"],
}
df_tabela = pd.DataFrame(tabela_dados)
st.dataframe(df_tabela, use_container_width=True)

st.success(
    "✨ Ambiente isolado e seguro: Este painel possui endereço próprio e não"
    " interfere no terminal dos vendedores."
)