import pymysql

con = pymysql.connect(
    host ="localhost",
    user = "maia", 
    password ="12149180",
    port = 3306,
    charset ="utf8mb4",
    db ="aulaPythonFull",
    cursorclass = pymysql.cursors.DictCursor)

def inserir(nome):
    try:
        
        with con.cursor() as cursor:
            cursor.execute(f"INSERT INTO Teste (nome) values ('{nome}')")
            con.commit()  # Confirma a transação
            print(f"Valor inserido com sucesso!")

    except Exception as e:
        print(f'Ocorreu um erro {e}')

    finally:
        con.close()  # Fecha a conexão com o banco de dados

inserir('Rogerio')
