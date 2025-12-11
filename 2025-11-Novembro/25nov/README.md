# Aula 12 – Desenvolvimento do Projeto Final

## 📌 Objetivos da Aula

- Consolidar os conteúdos teóricos antes da fase final de desenvolvimento.  
- Iniciar formalmente a construção do Projeto Final de Avaliação.  
- Interpretar requisitos, dividir o trabalho em fases e estruturar o pipeline completo.  
- Explorar o cenário empresarial, as fontes de dados e a arquitetura esperada.  
- Criar a base conceptual e prática para avançar autonomamente nas 5 fases do projeto.  

---

## 📚 Revisão dos Conteúdos Essenciais

- Fundamentos de Integração de Dados.  
- Arquiteturas de Integração e Contextos Empresariais.  
- Processos ETL (Extract, Transform, Load).  
- Qualidade e Consistência de Dados.  
- Ferramentas de Integração (ETL, ELT, Streaming, MDM).  
- Integração de Dados em Contextos Avançados.  

---

# 🧩 Projeto Final – Integração de Dados (5 Módulos)

## 🎯 Título  
**Implementação de um Sistema Híbrido de Integração e Governança de Dados para uma Visão 360º do Cliente**

## 🎯 Objetivo  
Demonstrar proficiência total em Integração de Dados:  
- fundamentos teóricos  
- processos ETL  
- qualidade dos dados  
- ferramentas  
- integração avançada  
- governança e visão 360º  

---

## 🏢 Cenário de Negócio

Uma empresa de serviços financeiros está a modernizar o sistema de gestão de clientes. A meta:  
**criar uma visão 360º do cliente**, integrando três fontes distintas:

1. **Sistema Legado (Batch)** – Base de dados histórica (estruturados).  
2. **Sistema de Suporte (API/Web Service)** – Contactos e moradas (semi-estruturados).  
3. **Sistema de Transações (Streaming)** – Eventos financeiros em tempo real.  

O projeto deve unificar estes fluxos num Data Mart e assegurar qualidade, consistência e governança.

---

# 📦 Estrutura do Projeto (5 Fases)

## 🔵 Fase 1 – Análise e Design Conceptual  
*(Módulo 1: Fundamentos de Integração de Dados)*

Tarefas:  
1. Definir requisitos e desafios (latência, diversidade, consistência, etc.).  
2. Propor a arquitetura conceptual e justificar.  
3. Criar glossário com 5 termos essenciais.  

---

## 🟠 Fase 2 – Mapeamento e Processo ETL  
*(Módulo 2: Processos ETL)*

Tarefas:  
4. Selecionar 5 campos do Sistema Legado e criar tabela de mapeamento → Data Mart.  
5. Produzir pseudocódigo para transformação complexa.  
6. Definir estratégia de carga (Full Load / CDC incremental).  

---

## 🟡 Fase 3 – Qualidade e Consistência de Dados  
*(Módulo 3: Data Quality)*

Tarefas:  
7. Descrever o Data Profiling aplicado às moradas da API.  
8. Criar 3 regras de Data Cleansing para o campo Nome.  
9. Definir regra de resolução de conflitos para o NIF e identificar a Golden Source.  

---

## 🟣 Fase 4 – Seleção e Justificação de Ferramentas  
*(Módulo 4: Ferramentas de Integração)*

Tarefas:  
10. Escolher uma ferramenta ETL comercial e outra open source, com justificação técnica.  
11. Definir a plataforma de streaming (Kafka + Spark/Flink, etc.).  
12. Escolher ferramenta de MDM e explicar integração com ETL e Streaming.  

---

## 🟢 Fase 5 – Integração Avançada e Governança  
*(Módulo 5: Integração Avançada)*

Tarefas:  
13. Descrever o pipeline de streaming para transações financeiras + CDC + Kappa/Lambda.  
14. Explicar parsing e normalização de transações em XML para o Data Mart relacional.  
15. Definir papéis de Data Owner e Data Steward e políticas de governança conformes ao RGPD.  

---

# 📎 Anexos Disponibilizados

- `clientes_master_data.csv` – Base estruturada de clientes.  
- `interacoes_web_stream.json` – Stream de interações web.  
- `mock_data_description.md` – Documentação das falhas intencionais (NIF inválido, valores fora de domínio, registos órfãos).  

Estes ficheiros servem para testes de integração, qualidade e validação.

---

# 📄 Entregáveis

O aluno deve entregar **um único Relatório Técnico em PDF**, contendo:

- Capa e índice.  
- Introdução + enquadramento.  
- Desenvolvimento das 5 Fases (com tabelas, diagramas e justificações).  
- Conclusão.  
- Anexos (código e ficheiros utilizados).  

---

# 🧮 Critérios de Avaliação

| Critério | Módulo | Peso | Descrição |
|---------|--------|------|-----------|
| Design Conceptual | Módulo 1 | 15% | Requisitos e adequação da arquitetura. |
| Processo ETL | Módulo 2 | 20% | Mapeamento e pseudocódigo. |
| Qualidade de Dados | Módulo 3 | 20% | Cleansing, profiling e consistência. |
| Seleção de Ferramentas | Módulo 4 | 15% | Justificação de ETL, Streaming e MDM. |
| Integração Avançada | Módulo 5 | 20% | CDC, streaming, governança. |
| Relatório Geral | – | 10% | Clareza, rigor técnico e formatação. |

**Nota mínima para aprovação: 50% no Projeto Final.**

---

# 📅 Data de Entrega

**16 de dezembro de 2025**

---

## 💬 Comentários / Observações

- A aula foi inteiramente dedicada ao início do projeto.  
- O foco agora desloca-se para design, rigor e execução de cada fase.  
- Este documento enquadra tudo o que será exigido até à entrega final.

