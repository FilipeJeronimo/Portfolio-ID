#1
#Os valores marcados como inválidos serão -5, None e 122

#2
#Os restantes dos dados e verificar se existe algum tipo de consistência entre as 2 contas, ou seja mesmos dados.

#3
# 1º problema - emails repetidos: ana.silva@email.com (Unicidade / Duplicidade)
# 2º problema - emails nulos do ID: 103, 108 (Completude)
# 3º problema - coerência nos dados: Nome - Carlos Gome tem o email maria@email.com (Consistência / Precisão)
# 4º problema - idade nula no ID: 106 (Completude)
# 5º problema - diferença entre escrita do nome da cidade PORTO ou Porto (Padronização / Consistência)
# 6º problema - o cliente João Pereira tem data de nascimento para o ano e tendo 25 anos de idade (Validade / Precisão)

#4
"""
CREATE TABLE Produtos (
    ProdutoID INT PRIMARY KEY NOT NULL,
    NomeProduto VARCHAR(255) NOT NULL,
    Preco DECIMAL(10,2) CHECK (Preco > 0),
    Stock INT CHECK (Stock >= 0),
    DataValidade DATE,
    CHECK (DataValidade IS NULL OR DataValidade > CURRENT_DATE)
);
"""

#5
import pandas as pd
df = pd.read_csv("vendas.csv")
df = df.drop_duplicates()
df["Cliente_Email"] = df["Cliente_Email"].fillna("desconhecido@email.com")
df.loc[df["Quantidade"] <= 0, "Quantidade"] = 1
df["Produto"] = df["Produto"].str.title()
print(df)
df.to_csv("vendas_limpo.csv", index=False)
