import pandas as pd
import json
import numpy as np

# ================================================================
# Exercício 1: Extração e Visualização de Dados CSV
# ================================================================

dados_vendas = """Data,Produto,Quantidade,Preco_Unitario
2024-05-01,Teclado,10,25.00
2024-05-01,Rato,5,15.50
2024-05-02,Monitor,2,150.00
2024-05-02,Webcam,8,30.00
2024-05-03,Teclado,12,25.00
"""
with open("vendas_diarias.csv", "w", encoding="utf-8") as f:
    f.write(dados_vendas)

df_vendas = pd.read_csv("vendas_diarias.csv")

print("=== Primeiras 3 Linhas ===")
print(df_vendas.head(3))
print("\n=== Tipos de Dados ===")
print(df_vendas.dtypes)

# ================================================================
# Exercício 2: Extração de Dados JSON e Carregamento para CSV
# ================================================================

dados_stock = [
    {"id": "P001", "nome": "Teclado", "stock": 150, "localizacao": "A1"},
    {"id": "P002", "nome": "Rato", "stock": 200, "localizacao": "A2"},
    {"id": "P003", "nome": "Monitor", "stock": 50, "localizacao": "B1"},
    {"id": "P004", "nome": "Webcam", "stock": 80, "localizacao": "B2"}
]

with open("stock_produtos.json", "w", encoding="utf-8") as f:
    json.dump(dados_stock, f, indent=4, ensure_ascii=False)

df_stock = pd.read_json("stock_produtos.json")

df_stock.to_csv("stock_limpo.csv", index=False, encoding="utf-8")

print("\n=== Dados de Stock ===")
print(df_stock)

# ================================================================
# Exercício 3: ETL Completo com Limpeza e Agregação
# ================================================================

dados_brutos = """ID_Venda,Produto,Cliente_ID,Valor_Unitario,Quantidade
1,Teclado,101,25.00,2
2,Rato,102,15.50,1
3,Monitor,101,150.00,NaN
4,Webcam,103,30.00,5
5,Teclado,102,25.00,3
6,Rato,101,15.50,NaN
7,Monitor,103,150.00,1
"""
with open("vendas_brutas.csv", "w", encoding="utf-8") as f:
    f.write(dados_brutos)

df_brutas = pd.read_csv("vendas_brutas.csv")

df_brutas["Valor_Unitario"] = pd.to_numeric(df_brutas["Valor_Unitario"], errors="coerce")

media_quantidade = df_brutas["Quantidade"].mean()
df_brutas["Quantidade"] = df_brutas["Quantidade"].fillna(media_quantidade)

df_brutas["Valor_Total"] = df_brutas["Valor_Unitario"] * df_brutas["Quantidade"]

df_total_gasto = (
    df_brutas.groupby("Cliente_ID", as_index=False)["Valor_Total"]
    .sum()
    .rename(columns={"Valor_Total": "Total_Gasto"})
)

df_total_gasto.to_csv("total_gasto_clientes.csv", index=False, encoding="utf-8")

print("\n=== Total Gasto por Cliente ===")
print(df_total_gasto)