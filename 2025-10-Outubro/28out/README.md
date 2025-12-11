# Aula 08 – Ferramentas de Integração e ETL/ELT Moderno

## 📌 Objetivos da Aula

- Compreender o papel das ferramentas de integração no processo ETL.  
- Identificar diferentes tipos de ferramentas (Open Source, Comerciais, Cloud, ELT).  
- Aprender critérios objetivos para seleção de ferramentas ETL/ELT.  
- Explorar ferramentas baseadas em código, SQL e APIs.  
- Aplicar exercícios práticos de extração, transformação e carregamento com Python.  

---

## 📚 Conteúdos Abordados

- Evolução das ferramentas de integração de dados  
- Papel das ferramentas no processo ETL  
- Classificação das ferramentas de integração  
- Critérios de seleção de uma ferramenta ETL  
- Ferramentas Open Source: Pentaho, Talend, Apache Nifi…  
- Ferramentas Comerciais e Cloud: Informatica, SSIS, Azure Data Factory, AWS Glue  
- Ferramentas ELT modernas (dbt, Snowflake pipelines)  
- Integração com linguagens de programação (Python, SQL)  
- Transformações SQL: Stored Procedures e Views  
- Extração de Dados via APIs com Python  
- Exercícios práticos de ETL  

---

## 🛠 Exercícios e Projetos

### 📄 Tarefa 6 – Processos ETL Práticos em Python  
**Realizada integralmente durante a aula**

---

### **Exercício 1 – Extração e Visualização de Dados CSV**
**Objetivo:** Criar, extrair e inspecionar dados de um ficheiro CSV.

**Passos realizados:**
1. Criação do ficheiro `vendas_diarias.csv` com os dados fornecidos.  
2. Extração para um DataFrame Pandas.  
3. Exibição das 3 primeiras linhas (`.head(3)`) e `df.dtypes`.  

---

### **Exercício 2 – Extração de Dados JSON e Carregamento para CSV**
**Objetivo:** Processar dados de stock fornecidos em JSON.

**Passos realizados:**
1. Criação do ficheiro `stock_produtos.json`.  
2. Leitura do JSON para um DataFrame.  
3. Exportação para o ficheiro `stock_limpo.csv`.  

---

### **Exercício 3 – ETL Completo com Limpeza e Agregação**
**Objetivo:** Extrair, transformar e carregar dados de vendas.

**Passos realizados:**

#### 🟦 Extração
- Leitura do ficheiro `vendas_brutas.csv`.

#### 🟧 Transformação – Limpeza
- Substituição de valores `NaN` na coluna **Quantidade** pela média.  
- Conversão dos valores unitários (se necessário).  

#### 🟨 Transformação – Cálculos
- Criação da coluna **Valor_Total** = `Valor_Unitario * Quantidade`.

#### 🟩 Transformação – Agregação
- Cálculo do **Total_Gasto** por `Cliente_ID`.

#### 🟪 Carga
- Exportação para `total_gasto_clientes.csv`.

---

## 📘 Estado da Tarefa  
✅ Tarefa 6 concluída com todos os passos implementados em Python.

---

## 💡 Observações / Comentários

- Os exercícios desta aula simulam fluxos ETL reais em escala reduzida.  
- Demonstração clara da diferença entre extração simples (CSV/JSON) e pipelines completos com transformação.  
- Comentário interno: incluir num futuro próximo ligação a APIs reais (ex.: OpenWeather, CoinGecko) para treino avançado.
