import requests
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import json

# ================================================================
# Exercício 1 – Utilizadores (API JSONPlaceholder)
# ================================================================

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
response.raise_for_status()

dados = response.json()
utilizadores = []

for user in dados:
    utilizadores.append({
        "name": user["name"],
        "email": user["email"],
        "city": user["address"]["city"]
    })

df_utilizadores = pd.DataFrame(utilizadores)

df_utilizadores.to_csv("utilizadores.csv", index=False, encoding="utf-8")

print("=== Primeiros Utilizadores ===")
print(df_utilizadores.head())
print("\nFicheiro 'utilizadores.csv' criado com sucesso!")

# ================================================================
# Exercício 2 – Comentários (API JSONPlaceholder)
# ================================================================

url = "https://jsonplaceholder.typicode.com/comments"
response = requests.get(url)
response.raise_for_status()

comentarios = response.json()

dados_filtrados = [
    {"name": c["name"], "email": c["email"], "body": c["body"]}
    for c in comentarios
]

df_comentarios = pd.DataFrame(dados_filtrados)

df_comentarios_limpos = df_comentarios[df_comentarios["email"].str.contains("@", na=False)]

df_comentarios_limpos.to_csv("comentarios_limpos.csv", index=False, encoding="utf-8")

print("\n=== Comentários Limpos ===")
print(f"Total de comentários válidos: {len(df_comentarios_limpos)}")
print("\nFicheiro 'comentarios_limpos.csv' criado com sucesso!")

# ================================================================
# Exercício 3 – Tarefas por Utilizador
# ================================================================

url_users = "https://jsonplaceholder.typicode.com/users"
response_users = requests.get(url_users)
response_users.raise_for_status()
users = response_users.json()

df_users = pd.DataFrame(users)[["id", "name", "email"]]
df_users.rename(columns={"id": "userId"}, inplace=True)

url_todos = "https://jsonplaceholder.typicode.com/todos"
response_todos = requests.get(url_todos)
response_todos.raise_for_status()
todos = response_todos.json()

df_todos = pd.DataFrame(todos)[["userId", "title", "completed"]]

df_merged = pd.merge(df_users, df_todos, on="userId")

df_tarefas_concluidas = (
    df_merged[df_merged["completed"] == True]
    .groupby(["userId", "name", "email"])
    .size()
    .reset_index(name="tarefas_concluidas")
)

df_tarefas_concluidas.to_csv("tarefas_por_utilizador.csv", index=False, encoding="utf-8")

print("\n=== Tarefas Concluídas por Utilizador ===")
print(df_tarefas_concluidas.head())
print("\nFicheiro 'tarefas_por_utilizador.csv' criado com sucesso!")

# ================================================================
# Exercício 4 – Produtos (FakeStore API)
# ================================================================

url = "https://fakestoreapi.com/products"
response = requests.get(url)
response.raise_for_status()
produtos = response.json()

df_produtos = pd.DataFrame(produtos)

if "rating" in df_produtos.columns:
    df_produtos["rating_rate"] = df_produtos["rating"].apply(lambda x: x.get("rate") if isinstance(x, dict) else None)
    df_produtos["rating_count"] = df_produtos["rating"].apply(lambda x: x.get("count") if isinstance(x, dict) else None)
    df_produtos.drop(columns=["rating"], inplace=True)  # remover o dicionário original

df_produtos.to_csv("produtos_novos.csv", index=False, encoding="utf-8")

print("=== Primeiros Produtos Extraídos ===")
print(df_produtos.head(), "\n")

df_produtos_limpos = df_produtos[df_produtos["price"] > 0].copy()
df_produtos_limpos["preco_com_iva"] = df_produtos_limpos["price"] * 1.23

con = sqlite3.connect("produtos.db")
df_produtos_limpos.to_sql("produtos", con, if_exists="replace", index=False)
con.close()

print("=== Produtos Limpos (com IVA) ===")
print(df_produtos_limpos[["id", "title", "price", "preco_com_iva"]].head())
print("\nFicheiro 'produtos_novos.csv' e base de dados 'produtos.db' criados com sucesso!")

# ================================================================
# Exercício 5 – NASA APOD (Astronomy Picture of the Day)
# ================================================================

with open("nasa_apod.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

df_apod = pd.DataFrame(dados)[["date", "title", "url"]]

df_apod.to_csv("nasa_apod.csv", index=False, encoding="utf-8")

print("=== Imagens NASA APOD ===")
print(df_apod.head())
print("\nFicheiro 'nasa_apod.csv' criado com sucesso!")

df_apod["date"] = pd.to_datetime(df_apod["date"], errors="coerce")

df_apod["mes_ano"] = df_apod["date"].dt.to_period("M")

contagem = df_apod["mes_ano"].value_counts().sort_index()

plt.figure(figsize=(8, 5))
contagem.plot(kind="bar", color="skyblue")
plt.title("Número de Fotos NASA APOD por Mês (dados JSON)")
plt.xlabel("Mês/Ano")
plt.ylabel("Número de Fotos")
plt.tight_layout()
plt.savefig("nasa_apod_grafico.png")
plt.show()

print("\nGráfico 'nasa_apod_grafico.png' criado com sucesso!")