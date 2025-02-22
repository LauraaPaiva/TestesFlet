# models.py
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONN = 'sqlite:///projetoFlet.db'

engine = create_engine(CONN, echo=True)
SessionFactory = sessionmaker(bind=engine)
Base = declarative_base()

def Cadastro(item):
    session = SessionFactory()
    session.add(item)
    session.commit()
    session.close()

def ListarProdutos():
    session = SessionFactory()
    produtos = session.query(Produto).all()
    session.close()
    return produtos

class Produto(Base):
    __tablename__ = 'Produto'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    preco = Column(Float())

Base.metadata.create_all(engine)