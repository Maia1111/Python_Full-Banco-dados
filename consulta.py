import pymysql


con = pymysql.connect(
    host ="localhost",
    user = "maia", 
    password ="12149180",
    port = 3306,
    charset ="utf8mb4",
    db ="aulaPythonFull",
    cursorclass = pymysql.cursors.DictCursor)


def consultar():
    try:
        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM Teste")
            resultado = cursor.fetchall()           

            for i in resultado:
                print(i)            
    except Exception as e:
        print(f'Ocorreu o erro {e}')



consultar()