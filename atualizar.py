import pymysql

con = pymysql.connect(
    host ="localhost",
    user = "maia", 
    password ="12149180",
    port = 3306,
    charset ="utf8mb4",
    db ="aulaPythonFull",
    cursorclass = pymysql.cursors.DictCursor)


def alterar(nomeAlterar, nomeAlterado):
    try:       
        with con.cursor() as cursor:

            cursor.execute(f"UPDATE  Teste set nome ='{nomeAlterado}' where nome = '{nomeAlterar}' ")
            con.commit()
            print("Alteração realizada com sucesso!")
    except Exception as e:
        print(f'Ocorreu o erro {e}')
    
   
    
alterar('Joaquim', 'Felisberto')
