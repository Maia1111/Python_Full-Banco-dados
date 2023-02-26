import pymysql


con = pymysql.connect(
    host ="localhost",
    user = "maia", 
    password ="12149180",
    port = 3306,
    charset ="utf8mb4",
    db ="aulaPythonFull",
    cursorclass = pymysql.cursors.DictCursor)


def cria_tabela(nome_tabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"create table {nome_tabela}(nome varchar(50))")
            print('Tabela criada com sucesso!')
            con.close()

    except Exception as e:
        print(f'Ocorreu um erro {e}')


def remove_tabela(nome_tabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"drop table {nome_tabela}")
            print('Tabela removida com sucesso!')
            con.close()

    except Exception as e:
        print(f'Ocorreu um erro {e}')







cria_tabela('Teste')


