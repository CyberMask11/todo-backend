from todo.core.database import engine, Base
from todo.db.model.todo import TODO

def create_tables():
    Base.metadata.create_all(engine)