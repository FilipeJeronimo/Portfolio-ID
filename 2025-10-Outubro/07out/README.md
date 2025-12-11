# Aula 05 – Revisão e Consolidação de ETL com Exercícios Práticos

## 📌 Objetivos da Aula

- Revisar os conteúdos essenciais de ETL abordados nas aulas anteriores.  
- Aplicar técnicas de Extração, Transformação e Carga em contexto real.  
- Consolidar competências através da resolução guiada de exercícios práticos.  
- Reforçar boas práticas de manipulação e validação de dados com Python.  

## 📚 Conteúdos Abordados

- Revisão dos conceitos fundamentais de ETL  
- Manipulação de dados com **pandas**  
- Limpeza e validação de datasets  
- Integridade referencial entre tabelas  
- Preparação de dados para processos analíticos  
- Escrita e leitura de ficheiros CSV  
- Consolidação de técnicas de ETL em Python  

## 🛠 Exercícios e Projetos

### Ficha Prática – ETL Completo com Python  
**Tarefa resolvida durante a aula**

1. **Leitura dos ficheiros:**  
   - `clientes.csv`  
   - `vendas.csv`  

2. **Deteção e correção de problemas nos clientes:**  
   - Remoção de **duplicados** (com base no nome e email)  
   - Tratamento de **valores nulos**, especialmente no campo email  
   - Correção de **idades inválidas** (menores de 18, negativas ou acima de 120 → substituídas por `None`)  
   - Validação de **emails mal formatados** (ausência de `@`)  

3. **Validação da integridade referencial:**  
   - Apenas manter clientes cujo `id_cliente` esteja presente na tabela de vendas  

4. **Guardar o resultado:**  
   - Ficheiro gerado: `clientes_final.csv`  

5. **Nova leitura dos ficheiros:**  
   - `clientes_final.csv`  
   - `vendas.csv`  

6. **Validação de integridade referencial em vendas:**  
   - Manter apenas vendas com `id_cliente` existente em `clientes_final`  

7. **Cálculo do total de vendas válidas**  

8. **Guardar o ficheiro final:**  
   - `vendas_validas.csv`  

### Estado da tarefa
✅ Exercícios concluídos com sucesso.

## 💡 Observações / Comentários

- Os exercícios reforçaram os passos essenciais de limpeza e verificação de datasets.  
- A abordagem seguida será reutilizada em futuros projetos de integração de dados.  
- Comentário interno: garantir que as funções criadas para validação e limpeza sejam reaproveitadas nas próximas aulas.
