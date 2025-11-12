Continuação do Projeto (Atividade) ✨

Objetivo: dar continuidade ao projeto criado em aula. Execute BD para criar o esquema e insert fornecido para popular as tabelas iniciais. Sua tarefa é criar arquivos de insert adicionais para popular as tabelas que ficaram vazias, garantindo integridade e organização.

📁 Estrutura sugerida do repositório
/atividade/
├─ BD.sql                    -- script para criar banco e tabelas (fornecido)
├─ insert.sql                -- inserts iniciais (fornecido)
├─ insert_categorias.sql     -- seu novo arquivo de exemplo
├─ insert_usuarios.sql       -- seu novo arquivo de exemplo
├─ insert_produtos.sql       -- seu novo arquivo de exemplo
├─ verificar.sql             -- consultas rápidas para checar inserções
└─ README.md                 -- este arquivo (bonito e claro)

✨ Guia passo a passo (rápido e direto)

Abra seu SGBD (SQLite / MySQL / PostgreSQL — conforme a aula).

Execute BD.sql → cria estrutura do banco.

Execute insert.sql (script inicial).

Rode SELECT nas tabelas para descobrir quais estão vazias.

Crie arquivos insert_<tabela>.sql para cada tabela sem dados.

Execute os novos insert_*.sql e verifique com SELECT COUNT(*) FROM <tabela>;.

Ajuste a ordem dos inserts para respeitar chaves estrangeiras (FKs).

✅ Boas práticas (sempre)

Use nomes descritivos: insert_produtos.sql, insert_pedidos.sql.

Adicione um cabeçalho em cada arquivo explicando pré-requisitos.

Insira dados realistas (nomes, e-mails, preços, datas).

Agrupe inserts em transações (BEGIN; ... COMMIT;) quando possível.

Evite duplicar registros.

Teste em um banco limpo antes de entregar.

🧩 Exemplo de arquivo: insert_produtos.sql
-- insert_produtos.sql
-- Insere produtos. Pré-requisito: categorias já populadas.

BEGIN;

INSERT INTO produtos (nome, descricao, preco, quantidade, categoria_id)
VALUES ('Caderno Universitário 100F', 'Caderno 100 folhas, capa dura', 18.50, 80, 2);

INSERT INTO produtos (nome, descricao, preco, quantidade, categoria_id)
VALUES ('Caneta Esferográfica Azul', 'Ponta média 0.7mm', 2.75, 200, 1);

COMMIT;

🔁 Ordem recomendada de inserção (quando houver FKs)

Tabelas de referência (ex.: categorias, fornecedores, estados)

Tabelas independentes (ex.: usuarios)

Tabelas com FKs (ex.: produtos → categoria_id)

Tabelas transacionais (ex.: pedidos, itens_pedido)

🛠️ Arquivo de verificação: verificar.sql (exemplos)
-- verificar.sql
SELECT 'categorias' AS tabela, COUNT(*) FROM categorias;
SELECT 'produtos'   AS tabela, COUNT(*) FROM produtos;
SELECT 'usuarios'   AS tabela, COUNT(*) FROM usuarios;

📋 Checklist de entrega

 Criou insert_*.sql para todas as tabelas vazias.

 Scripts executam sem erros em um banco novo.

 Comentários explicando dependências em cada arquivo.

 verificar.sql presente para comprovar inserções.

 Observações (NOTAS.md) sobre suposições, se houver.

🧾 Critérios de avaliação (sugestão)

Funcionalidade (40%) — scripts executam sem erros.

Organização (25%) — nomes claros, cabeçalhos e transações.

Qualidade dos dados (20%) — realismo e variedade.

Documentação (15%) — README, notas e verificação.

💡 Dicas rápidas de depuração

Erro de FK? Verifique se o registro referenciado existe.

Erro de sintaxe? Rode um INSERT por vez para localizar a linha.

SQLite: ative FKs com PRAGMA foreign_keys = ON; antes dos testes.

Use BEGIN; ... ROLLBACK; para testar sem persistir alterações.

✍️ Exemplo de comentário inicial para cada arquivo
-- insert_usuarios.sql
-- Insere usuários de teste (5 registros).
-- Pré-requisito: nenhuma tabela externa.
