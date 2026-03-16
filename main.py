from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

#Criar a classe base do ORM

Base = declarative_base()

class Usuario(Base):
    #Definir o nome da tabela
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    #Campo nome obrigatório
    nome = Column(String(100), nullable=True)
    #unique=True > não permite email repetido
    email = Column(String(100), nullable=True, unique=True)
    idade = Column(Integer)
    ativo = Column(Boolean, default=True)
    salario = Column(Float)

    def __init__(self, nome, email, idade, salario):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.salario = salario

#Criar a conexão
# Postegre: "postgresql://usuario:senha@localhost/nome_banco"
# MySql: "mysql+pymysql://usuario:senha@localhost/nome_banco"

engine = create_engine("sqlite:///empresa.db")

#Criar as  tabelas
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)

session = Session()
with Session() as session:
    try:
        usuario_existente = session.query(Usuario).filter_by(email="querojogardarksouls@gmail.com").first()
        if usuario_existente == None:
            #Criar um objeto
            usuario1 = Usuario( "Emilly", "querojogardarksouls@gmail.com", 16, 5000)
            session.add(usuario1)
            session.commit()
            print("Usuário cadastrado com sucesso!")
        else:
            print(f"Já existe um cadastro com este e-mail!")
    except Exception as erro:
        session.rollback()
        print(f"Ocorreu um erro: {erro}")