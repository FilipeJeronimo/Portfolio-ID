# Aula 09 – Integração de Dados com APIs e ETL Avançado

## 📌 Objetivos da Aula

- Revisão geral dos conteúdos nucleares da UC.  
- Consolidar Fundamentos de Integração de Dados.  
- Reforçar processos ETL completos em contexto real.  
- Avaliar qualidade e consistência de dados provenientes da Web.  
- Explorar ferramentas e métodos de integração moderna com APIs.  
- Aplicar técnicas ETL em cenários avançados com Python.  

---

## 📚 Conteúdos Abordados

- Fundamentos da Integração de Dados  
- Processos ETL (Extract, Transform, Load)  
- Qualidade e consistência de dados  
- Ferramentas de integração (ETL/ELT, Open Source, Cloud, Código)  
- Integração em contextos avançados (APIs, JSON, BD, dashboards)  
- Python como motor ETL para extração web  
- Revisão e síntese dos módulos anteriores  

---

## 🛠 Exercícios e Projetos

### 📄 Tarefa – ETL com APIs Públicas  
**Exercícios completos desenvolvidos integralmente durante a aula.**

---

### **Exercício 1 – Extração de Utilizadores (API JSONPlaceholder)**
**Objetivo:** Fazer extração simples + seleção de campos + carregamento.

**Passos realizados:**
1. Pedido HTTP GET à API de utilizadores.  
2. Extração dos campos:  
   - `name`  
   - `email`  
   - `address.city`  
3. Criação do ficheiro `utilizadores.csv`.  

---

### **Exercício 2 – Extração e Limpeza de Comentários**
**Objetivo:** ETL com validação e limpeza de emails.

**Passos realizados:**
1. Extração de comentários via API.  
2. Seleção dos campos `name`, `email`, `body`.  
3. Remoção de registos sem `@` no email.  
4. Carregamento para `comentarios_limpos.csv`.  

---

### **Exercício 3 – Integração entre Utilizadores e Tarefas**
**Objetivo:** Combinar duas APIs e agregar resultados.

**Passos realizados:**
1. Extração de utilizadores.  
2. Extração de tarefas (todos).  
3. Junção das tabelas via `userId`.  
4. Contagem de tarefas concluídas por utilizador.  
5. Exportação para `tarefas_por_utilizador.csv`.  

---

### **Exercício 4 – ETL Completo para Produtos (FakeStore API)**
**Objetivo:** Pipeline completo API → Limpeza → Cálculo → BD.

**Passos realizados:**
1. Extração dos produtos da API FakeStore.  
2. Criação do ficheiro `produtos_novos.csv`.  
3. Limpeza:  
   - Remoção de produtos com preço 0.  
   - Criação da coluna `preco_com_iva = preco * 1.23`.  
4. Inserção dos dados limpos numa BD SQLite (tabela `produtos`).  

---

### **Exercício 5 – API da NASA + Visualização**
**Objetivo:** Extração, estruturação e análise visual.

**Passos realizados:**
1. Extração de 10 imagens APOD da NASA.  
2. Construção da tabela com:  
   - `date`  
   - `title`  
   - `url`  
3. Criação de um gráfico (matplotlib) do número de fotos por mês.  

---

## 📘 Estado da Tarefa  
✅ Todos os exercícios foram concluídos com sucesso.  
💻 A aula foi totalmente orientada para prática de ETL com APIs reais.

---

## 💡 Observações / Comentários

- Excelente consolidação de processos ETL reais com dados externos.  
- APIs introduzem desafios adicionais de qualidade, formatos e validação.  
- Comentário interno: integrar dashboards (Power BI / Python) numa aula futura para encerrar o ciclo ETL.
