import pandas as pd
from numpy.testing.print_coercion_tables import print_coercion_table

# 1. Ler ficheiro clientes.csv
clientes = pd.read_csv("clientes.csv")

# 2. Detetar e corrigir problemas

# Remover duplicados (com base em nome e email)
clientes = clientes.drop_duplicates(subset=["nome", "email"], keep="first")

# Substituir emails nulos ou vazios por "email_desconhecido"
clientes["email"] = clientes["email"].fillna("email_desconhecido")
clientes["email"] = clientes["email"].replace("", "email_desconhecido")

# Corrigir emails mal formatados (sem '@')
clientes.loc[~clientes["email"].str.contains("@", na=False), "email"] = "email_desconhecido"

# Corrigir idades inválidas (<0, >120 ou ausentes → None)
clientes["idade"] = clientes["idade"].apply(lambda x: x if pd.notnull(x) and 0 <= x <= 120 else None)

# 3. Validar integridade referencial com vendas.csv
vendas = pd.read_csv("vendas.csv")

# Apenas clientes com id_cliente presente nas vendas
clientes_validos = clientes[clientes["id_cliente"].isin(vendas["id_cliente"])]

# 4. Guardar resultado
clientes_validos.to_csv("clientes_final.csv", index=False)

print("clientes_final.csv criado com sucesso!")
