# Aqui vou declarar que o banco de dados e a tabela Eventos existe
from src.model.configs.base import Base
from sqlalchemy import Column, String, Integer

class Eventos(Base):
    __tablename__ = "Eventos"
    
# Declarar o que possui de campos na tabela

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)