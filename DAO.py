import mysql.connector

def consultaNV(categoria):
    conexao = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password ='',
    database = 'LaBellaVita'
    )
    cursor = conexao.cursor()

    comando = "SELECT nome, preco FROM serviços WHERE categoria = %s"
    cursor.execute(comando, (categoria))
    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()
    return resultado

def consultaLogin(email, senha):
    conexao = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password ='',
    database = 'LaBellaVita'
    )
    cursor = conexao.cursor()

    comando = "SELECT email, senha FROM clientes WHERE email= %s and senha = %s"
    cursor.execute(comando, (email, senha))
    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()
    return resultado

def consultaCadastro(email):
    conexao = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password ='',
    database = 'LaBellaVita'
    )
    cursor = conexao.cursor()

    cursor.execute(f"SELECT email FROM clientes WHERE email= '{email}'")   
    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()
    return resultado

def ConsultaAgenda(categoria, data, time):
    conexao = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password ='',
    database = 'LaBellaVita'
    )
    cursor = conexao.cursor()

    comando = "SELECT agenda.dia, agenda.hora FROM agenda INNER JOIN serviços on (serviços.id = agenda.id_service) WHERE categoria = %s AND agenda.dia = %s AND agenda.hora = %s"
    cursor.execute(comando, (categoria, data, time))
    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()
    return resultado

def AdiconarData(data, time , email, nomeS):
    conexao = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password ='',
    database = 'LaBellaVita'
    )
    cursor = conexao.cursor()

    cursor.execute(f"SELECT id FROM clientes WHERE email = '{email}';")
    id_cliente = cursor.fetchall()
    

    cursor.execute(f"SELECT id FROM serviços WHERE nome = '{nomeS}';")
    id_service = cursor.fetchall()

    cursor.execute(f"INSERT INTO agenda (id_cliente, id_service, dia, hora) VALUES ({id_cliente[0][0]},{id_service[0][0]},'{data}','{time}');")
    resultado = cursor.fetchall()
    conexao.commit()

    cursor.close()
    conexao.close()
    return resultado

def AdiconarCadastro(nome, email, senha):
    conexao = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password ='',
    database = 'LaBellaVita'
    )
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO clientes (nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senha))
    resultado = cursor.fetchall()
    conexao.commit()

    cursor.close()
    conexao.close()

    return resultado


