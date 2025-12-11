# Aula 07 – Revisão Global e Limpeza de Dados em Python

## 📌 Objetivos da Aula

- Consolidar os conteúdos abordados nas aulas anteriores.  
- Aplicar técnicas de limpeza e validação de dados em Python.  
- Identificar inconsistências em ficheiros reais (CRM).  
- Preparar dados para integração num Data Warehouse.  

---

## 📚 Conteúdos Abordados

- Revisão de qualidade de dados  
- Problemas comuns em sistemas CRM  
- Validação e integridade referencial  
- Técnicas de normalização (nomes, emails, ordenação)  
- Limpeza programática com Python  
- Exportação de datasets limpos para posterior análise  

---

## 🛠 Exercícios e Projetos

### 📄 Tarefa 5 – Limpeza e Normalização de Dados (CRM)  
**Tarefa concluída durante a aula**

Contexto: Sistema CRM com dados acumulados ao longo dos anos, contendo erros e inconsistências.  
Objetivo: Avaliar, corrigir e preparar os dados antes da integração num Data Warehouse.

---

### **1. Leitura dos Dados**
- Leitura dos ficheiros:  
  - `clientes_T5.csv`  
  - `vendas_T5.csv`  

---

### **2. Deteção de Problemas**
Foram verificados:

- Valores nulos  
- Duplicados  
- Idades inválidas (fora de 18–100 anos)  
- Emails mal formatados (sem @ ou sem domínio)  
- Falta de integridade referencial entre clientes e vendas  

---

### **3. Tratamento dos Dados**

- Remoção de duplicados  
- Eliminação de registos inválidos  
- Correção de emails mal formatados  
- Preenchimento de valores nulos  
- Remoção de vendas sem cliente existente  

---

### **4. Normalização dos Dados**

- Formatação dos nomes: `str.title()`  
- Emails convertidos para minúsculas  
- Ordenação dos clientes por `id_cliente`  

---

### **5. Exportação de Resultados**

Foram gerados os ficheiros finais:

- `clientes_final.csv`  
- `vendas_validas.csv`

---

### **⭐ Extra (opcional realizado se aplicável)**  
Validação automática usando **expressões regulares**:

- Emails  
- Nomes (apenas letras e espaços)  

---

## 📘 Estado da Tarefa  
✅ Tarefa 5 completamente resolvida.

---

## 💡 Observações / Comentários

- Este exercício é uma simulação realista de problemas típicos em sistemas CRM.  
- Demonstra a necessidade de validação contínua e regras de qualidade bem definidas.  
- Comentário interno: recomendado integrar no futuro módulos automáticos de data validation.
