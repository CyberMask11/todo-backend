from sqlalchemy import Column, String, Integer
from todo.core.database import Base

class TODO(Base):
    __tablename__ = "Todo"
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    content = Column(String(120))