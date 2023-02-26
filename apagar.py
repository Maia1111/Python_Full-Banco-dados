import pymysql

con = pymysql.connect(
    host ="localhost",
    user = "maia", 
    password ="12149180",
    port = 3306,
    charset ="utf8mb4",
    db ="aulaPythonFull",
    cursorclass = pymysql.cursors.DictCursor)


def apagar(nome):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"DELETE FROM Teste WHERE nome = '{nome}' ")
            print("Exclusão realizada com sucesso!")
            con.commit()

    except Exception  as e:
            print(f"Ocorreu o erro {e}")
    
    finally:
         con.close()


apagar('Marcelo')
