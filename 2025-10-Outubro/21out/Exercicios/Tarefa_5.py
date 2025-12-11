import pandas as pd

# Lê os ficheiros CSV
clientes = pd.read_csv("clientes_T5.csv")
vendas = pd.read_csv("vendas_T5.csv")

print("Clientes:", clientes.shape)
print("Vendas:", vendas.shape)

print("\nValores nulos por coluna:")
print(clientes.isnull().sum())

print("\nDuplicados em clientes:", clientes.duplicated().sum())
print("Duplicados em vendas:", vendas.duplicated().sum())

clientes_invalidos_idade = clientes[(clientes['idade'] < 18) | (clientes['idade'] > 100)]
print("\nClientes com idade inválida:", len(clientes_invalidos_idade))

import re

def email_valido(email):
    padrao = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return bool(re.match(padrao, str(email)))

clientes['email_valido'] = clientes['email'].apply(email_valido)
print("Emails inválidos:", (~clientes['email_valido']).sum())

ids_clientes = set(clientes['id_cliente'])
vendas_invalidas = vendas[~vendas['id_cliente'].isin(ids_clientes)]
print("Vendas sem cliente associado:", len(vendas_invalidas))

clientes = clientes.drop_duplicates(subset='id_cliente', keep='first')
clientes = clientes[(clientes['idade'] >= 18) & (clientes['idade'] <= 100)]
clientes = clientes[clientes['email_valido']]

clientes['email'] = clientes['email'].fillna("sem_email@empresa.pt")
clientes['nome'] = clientes['nome'].fillna("Desconhecido")

vendas = vendas[vendas['id_cliente'].isin(clientes['id_cliente'])]

clientes['nome'] = clientes['nome'].str.title()
clientes['email'] = clientes['email'].str.lower()

clientes = clientes.sort_values(by='id_cliente')

clientes.to_csv("clientes_final.csv", index=False)
vendas.to_csv("vendas_validas.csv", index=False)

print("Ficheiros limpos gerados com sucesso!")

def nome_valido(nome):
    return bool(re.match(r'^[A-Za-zÀ-ÿ\s]+$', str(nome)))

clientes['nome_valido'] = clientes['nome'].apply(nome_valido)
clientes = clientes[clientes['nome_valido']]

