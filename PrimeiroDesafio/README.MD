## 📘 Documentação do App.py

---

# Sistema de Gerenciamento de Tarefas (App.py)

## 1. Visão geral

- Linguagem: Python
- Banco de dados: SQLite (`sqlite3`)
- Arquivo de dados: tarefas.db
- Modo de uso: CLI (linha de comando)
- Objetivo: CRUD simples para tarefas acadêmicas (título, disciplina, prazo, status)

## 2. Estrutura do código

- Classe principal:
  - `BancoDados`  
- Operações:
  - criar tabela
  - inserir tarefa
  - consultar todas as tarefas
  - atualizar status
  - excluir tarefa

- Loop interativo:
  - 1) Adicionar
  - 2) Consultar
  - 3) Atualizar status
  - 4) Excluir
  - 5) Sair

---

## 3. Classe `BancoDados`

```python
class BancoDados:
    def __init__(self, db_path="PrimeiroDesafio/tarefas.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
```

- Construtor:
  - recebe `db_path` (caminho do arquivo SQLite)
  - abre conexão inicial (que não é usada em outros métodos, mas existe)

### 3.1 `criar_tabela()`

```python
def criar_tabela(self):
    conexao = sqlite3.connect(self.db_path)
    cursor = conexao.cursor()
    cursor.execute('''...''')
    conexao.commit()
    conexao.close()
```

- Cria tabela `tarefas`, caso NÃO exista.
- Colunas:
  - `id` (INTEGER, PK, autoincrement)
  - `titulo` (TEXT, NOT NULL)
  - `disciplina` (TEXT, NOT NULL)
  - `prazo` (TEXT, NOT NULL)
  - `status` (TEXT, NOT NULL)

### 3.2 `inserir_dados(titulo, disciplina, prazo, status)`

```python
def inserir_dados(self, titulo, disciplina, prazo, status):
    conexao = sqlite3.connect(self.db_path)
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO tarefas (titulo, disciplina, prazo, status)
        VALUES (?, ?, ?, ?)
    ''', (titulo, disciplina, prazo, status))
    conexao.commit()
    conexao.close()
```

- Insere novo registro na tabela.
- Usa parâmetros com `?` para evitar SQL injection.
- Fecha conexão ao final.

### 3.3 `consultar_dados()`

```python
def consultar_dados(self):
    conexao = sqlite3.connect(self.db_path)
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM tarefas')
    resultados = cursor.fetchall()
    conexao.close()
    return resultados
```

- Lê todos registros.
- Retorna lista de tuplas
  - formato: `(id, titulo, disciplina, prazo, status)`

### 3.4 `atualizar_status(id, novo_status)`

```python
def atualizar_status(self, id, novo_status):
    conexao = sqlite3.connect(self.db_path)
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE tarefas
        SET status = ?
        WHERE id = ?
    ''', (novo_status, id))
    conexao.commit()
    conexao.close()
```

- Atualiza apenas o campo `status`.
- Identifica tarefa por `id`.

### 3.5 `excluir_dados(id)`

```python
def excluir_dados(self, id):
    conexao = sqlite3.connect(self.db_path)
    cursor = conexao.cursor()
    cursor.execute('''
        DELETE FROM tarefas
        WHERE id = ?
    ''', (id,))
    conexao.commit()
    conexao.close()
```

- Exclui tarefa por `id`.

---

## 4. Fluxo do programa (executável)

### 4.1 Inicialização

- `BancoDados().criar_tabela()` garante que a tabela exista antes de qualquer operação.

### 4.2 Tela de boas-vindas

- Exibe menu fixo para usuário escolher.
- Repete em `while True` até opção 5.

### 4.3 Opção 1: Adicionar tarefa

Inputs coletados:
- `titulo`
- `disciplina`
- `prazo` (dd/mm/yyyy) (não validado)
- `status` (Pendente/Concluída) (não validado)

A chamada:
- `BancoDados("PrimeiroDesafio/tarefas.db").inserir_dados(...)`

### 4.4 Opção 2: Listar tarefas

- Chama `consultar_dados()`
- Exibe cada tarefa com `print(f"ID: ...")`

### 4.5 Opção 3: Atualizar status

Inputs:
- `id` (int)
- `novo_status`

Ação:
- `atualizar_status(id, novo_status)`

### 4.6 Opção 4: Excluir tarefa

- Input `id` (int)
- Chama `excluir_dados(id)`

### 4.7 Opção 5: Sair

- Faz `break` no loop
- Exibe mensagem de despedida

### 4.8 Tratamento de opção inválida

- Qualquer outra entrada exibe: `"Opção inválida. Por favor, tente novamente."`

---

## 5. Notas de manutenção e melhorias recomendadas

1. `BancoDados.__init__` abre conexão não utilizada (pode ser removida ou aproveitada).
2. Reutilizar conexão em vez de sempre criar nova em cada método (economia de recursos).
3. Validação de entrada:
   - formato de data
   - título não vazio
   - status fixo (Pendente/Concluída)
   - `id` existente
4. Tratamento de exceções: `try/except` para falhas de DB (arquivo corrompido, bloqueio, etc).
5. Exibir resumo quando não houver tarefas.
6. Inserir opção de busca por `disciplina`/`status`/`prazo`.

---

## 6. Exemplo de uso na prática

1. Executar:
   - `python PrimeiroDesafio\App.py`
2. Selecionar `1` e inserir tarefa
3. Selecionar `2` para ver tabela
4. Selecionar `3` para marcar concluída
5. Selecionar `4` para remover
6. Selecionar `5` para sair

---

## 7. Tabela de campos da entidade `tarefas`

- `id`:
  - tipo: INTEGER
  - papel: identificador único e chave primária
- `titulo`:
  - tipo: TEXT
  - papel: nome/descrição breve
- `disciplina`:
  - tipo: TEXT
  - papel: categoria acadêmica
- `prazo`:
  - tipo: TEXT
  - papel: data limite (string)
- `status`:
  - tipo: TEXT
  - papel: controle do estado (Pendente/Concluída)

---

## 8. Conclusão

- O App.py é um gerenciador simples e funcional de tarefas com SQLite.
- A lógica é linear e adequada para protótipo / estudo.
- A documentação acima torna claro cada artefato (classe, método, fluxo, dados).