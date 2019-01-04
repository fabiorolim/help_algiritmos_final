import sqlite3

BD = 'financeiro.db'
conexao = sqlite3.connect(BD)
cursor = conexao.cursor()


def cadastrar(matricula, nome):
    '''Cadastra um aluno'''
    sql = ("INSERT INTO alunos (matricula, nome) VALUES ('%d', '%s')" 
        % (matricula, nome))
    cursor.execute(sql)
    if cursor.rowcount == 1:
        conexao.commit()
    else:
        print('Erro')


def mostrar_todos():
    '''Printa todos os registros da tabela Alunos'''
    sql = "SELECT * FROM alunos"
    cursor.execute(sql)
    alunos = cursor.fetchall()
    if alunos:
        for aluno in alunos:
            print(aluno[0], aluno[1])
    else:
        print('Nada encontrado')

def fechar_conexao():
    conexao.close()
