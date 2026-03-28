import sqlite3

class BancoDados:
    def __init__(self, db_path="PrimeiroDesafio/tarefas.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        
    def criar_tabela(self):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                disciplina TEXT NOT NULL,
                prazo TEXT NOT NULL,
                status TEXT NOT NULL
            )
        ''')
        
        conexao.commit()
        conexao.close()

    def inserir_dados(self, titulo, disciplina, prazo, status):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()
        
        cursor.execute(f'''
            INSERT INTO tarefas (titulo, disciplina, prazo, status)
            VALUES (?, ?, ?, ?)
        ''', (titulo, disciplina, prazo, status))
        
        conexao.commit()
        conexao.close()

    def consultar_dados(self):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()
        
        cursor.execute(f'SELECT * FROM tarefas')
        resultados = cursor.fetchall()
        
        conexao.close()
        return resultados
    
    def atualizar_status(self, id, novo_status):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()
        
        cursor.execute(f'''
            UPDATE tarefas
            SET status = ?
            WHERE id = ?
        ''', (novo_status, id))
        
        conexao.commit()
        conexao.close()

    def excluir_dados(self, id):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()
        
        cursor.execute(f'''
            DELETE FROM tarefas
            WHERE id = ?
        ''', (id,))
        
        conexao.commit()
        conexao.close()

BancoDados().criar_tabela()

print("""
Bem-vindo ao sistema de gerenciamento de tarefas!
Escolha uma opção:
1. Adicionar nova tarefa
2. Consultar tarefas
3. Atualizar status de uma tarefa
4. Excluir uma tarefa
5. Sair
""")

while True:
    opcao = input("Digite a opção desejada: ")
    
    if opcao == '1':
        titulo = input("Digite o título da tarefa: ")
        disciplina = input("Digite a disciplina: ")
        prazo = input("Digite o prazo (dd/mm/yyyy): ")
        status = input("Digite o status (Pendente/Concluída): ")
        BancoDados("PrimeiroDesafio/tarefas.db").inserir_dados(titulo, disciplina, prazo, status)
        print("Tarefa adicionada com sucesso!")
    
    elif opcao == '2':
        tarefas = BancoDados("PrimeiroDesafio/tarefas.db").consultar_dados()
        for tarefa in tarefas:
            print(f"ID: {tarefa[0]}, Título: {tarefa[1]}, Disciplina: {tarefa[2]}, Prazo: {tarefa[3]}, Status: {tarefa[4]}")
    
    elif opcao == '3':
        id = int(input("Digite o ID da tarefa que deseja atualizar: "))
        novo_status = input("Digite o novo status (Pendente/Concluída): ")
        BancoDados("PrimeiroDesafio/tarefas.db").atualizar_status(id, novo_status)
        print("Status atualizado com sucesso!")
    
    elif opcao == '4':
        id = int(input("Digite o ID da tarefa que deseja excluir: "))
        BancoDados("PrimeiroDesafio/tarefas.db").excluir_dados(id)
        print("Tarefa excluída com sucesso!")
    
    elif opcao == '5':
        print("Saindo do sistema. Até mais!")
        break
    
    else:
        print("Opção inválida. Por favor, tente novamente.")