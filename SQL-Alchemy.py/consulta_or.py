from sqlalchemy import create_engine, or_
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

x = session.query(Pessoa).filter(or_(Pessoa.nome == 'Caio', Pessoa.nome == 'Marcos')).all()

for i in x:
    print(i.nome)