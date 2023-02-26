from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ORM import Pessoa


def RetornaSession():
    USUARIO = "maia"
    SENHA ="12149180"
    HOST = "localhost"
    BANCO = "aulaPythonFull"
    PORT = "3306"

    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)

    return Session()


session = RetornaSession()

# Passa o parametro nome da tabela
x = session.query(Pessoa)

# Esta colocando os dados de Pessoa persistido na variavel x
x = x.all()


# Trazendo todos os nome do banco de dados. Aqui esta realizando dois filtros
x = session.query(Pessoa).filter(Pessoa.nome == 'Caio').filter(Pessoa.id == "2")
for i in x :
     print(i.nome)
     

# Jeito mais pythonido de passar dois ou mais parametros
x = x.session.query(Pessoa).filter_by(usuario='caio', nome='Caio')
for i in x:
    print(i.nome)


# Imprimindo somente os que tem nome 'Caio'
for i in x :
    if i.nome == 'Caio':
        print(i.nome)