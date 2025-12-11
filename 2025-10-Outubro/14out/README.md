# Aula 06 – Qualidade e Consistência de Dados

## 📌 Objetivos da Aula

- Compreender a importância da qualidade e consistência dos dados em processos ETL.  
- Identificar problemas comuns que comprometem análises, relatórios e pipelines.  
- Explorar dimensões da qualidade de dados e estratégias de Data Quality Management (DQM).  
- Aplicar estes conceitos em exercícios práticos.  

## 📚 Conteúdos Abordados

- Qualidade e consistência de dados  
- Impacto de dados de fraca qualidade nas organizações  
- Dimensões da qualidade de dados  
- Problemas recorrentes em bases de dados  
- Estratégias de Data Quality Management (DQM)  
- Aplicação prática de deteção e correção de erros  
- Revisão e prática orientada  

---

## 🛠 Exercícios e Projetos

### 📄 Tarefa 4 – Resoluções Práticas  
**Tarefa concluída durante a aula**

#### **Exercício 1**  
Lista de idades:  
`[28, 45, -5, None, 32, 122, 98]`  
Identificação dos valores inválidos (idade negativa, nula ou fora dos limites aceitáveis).

#### **Exercício 2**  
Duplicidade de NIF com nomes semelhantes:  
- Análise de possíveis erros de input.  
- Verificação da identidade real do cliente.  
- Procura de inconsistências noutros atributos.  

#### **Exercício 3**  
Deteção de **pelo menos cinco problemas de qualidade** na tabela de clientes, incluindo:  
- Dados em falta  
- Idades inválidas  
- Datas impossíveis  
- Emails incorretos  
- Duplicados  
- Formatos inconsistentes  
- Cidades com escrita desigual  
*(Cada problema associado à dimensão de qualidade correspondente.)*

#### **Exercício 4**  
Criação de tabela SQL `Produtos` com regras:  
- Chave primária  
- Campos obrigatórios  
- Preço positivo  
- Stock não negativo  
- Data de validade futura  

#### **Exercício 5**  
Script em Python (Pandas) para limpeza de `vendas.csv`:  
- Remoção de duplicados  
- Preenchimento de emails em falta com valor padrão  
- Correção de quantidades inválidas (≤ 0 → 1)  
- Padronização de nomes de produtos (capitalização correta)  

---

## 📘 Estado da Tarefa  
✅ Tarefa 4 totalmente resolvida.

---

## 💡 Observações / Comentários

- A aula consolidou a importância de aplicar validações robustas antes de qualquer pipeline ETL.  
- A deteção precoce de inconsistências evita custos elevados em fases posteriores.  
- Comentário interno: boas oportunidades futuras para introdução de ferramentas automatizadas de Data Quality.
