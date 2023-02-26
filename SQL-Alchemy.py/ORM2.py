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


x  = Pessoa(nome="Marcos", 
            usuario="marcos", 
            senha="123")

y  = Pessoa(usuario="marcos", 
            senha="123")



session.add_all([x,y])

session.commit()



