import pandas as pd

# 5. Ler ficheiros
clientes_final = pd.read_csv("clientes_final.csv")
vendas = pd.read_csv("vendas.csv")

# 6. Validar integridade referencial
vendas_validas = vendas[vendas["id_cliente"].isin(clientes_final["id_cliente"])]

# 7. Procurar automaticamente uma coluna de valor
possiveis_colunas = ["valor_venda", "valor", "preco", "montante", "total"]
coluna_valor = next((col for col in possiveis_colunas if col in vendas_validas.columns), None)

if coluna_valor:
    total_vendas = vendas_validas[coluna_valor].sum()
    print(f"Total de vendas válidas ({coluna_valor}): {total_vendas:.2f}")
else:
    print("Não foi encontrada nenhuma coluna de valor nas vendas!")

# 8. Guardar resultado final
vendas_validas.to_csv("vendas_validas.csv", index=False)

print("vendas_validas.csv criado com sucesso!")

