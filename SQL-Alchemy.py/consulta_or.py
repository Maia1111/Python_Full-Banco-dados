from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definindo as informações de autenticação e configuração do banco de dados
USUARIO = "maia"
SENHA ="12149180"
HOST = "localhost"
BANCO = "aulaPythonFull"
PORT = "3306"

# Criando a string de conexão com o banco de dados
CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

# Criando a conexão com o banco de dados MySQL
engine = create_engine(CONN, echo=True)

# Criando uma instância da classe sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# Criando a classe base ORM
Base = declarative_base()

# Criando a classe Pessoa ORM que representa a tabela "Pessoa" do banco de dados
class Pessoa(Base):
    __tablename__ = "Pessoa"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    usuario = Column(String(20))
    senha = Column(String(10))

# Criando todas as tabelas definidas nas classes ORM no banco de dados
Base.metadata.create_all(engine)
