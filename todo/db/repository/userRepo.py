from .base import BaseRepo
from todo.db.model.todo import TODO
from todo.db.schema.todo import CreateTodo, TodoOutput
from fastapi import HTTPException

class UserRepo(BaseRepo):
    def create_todo(self, todo_details: CreateTodo) -> TodoOutput:
        todo = TODO(**todo_details.model_dump(exclude_none=True))

        self.session.add(todo)
        self.session.commit()
        self.session.refresh(todo)

        return todo
    
    def delete_todo(self, todo_id: int):
        todo = self.session.query(TODO).filter_by(id=todo_id).first()
        if not todo:
            raise HTTPException(status_code=404, detail="Todo does not exist")
        
        self.session.delete(todo)
        self.session.commit()

    def get_todo_by_id(self, todo_id: int) -> TODO:
        todo = self.session.get(TODO, todo_id)
        if todo:
            return todo
        raise HTTPException(status_code=404, detail="Todo does not exist")
    
    def get_all_todo(self) -> list[TODO]:
        return self.session.query(TODO).all()

    
    def get_todo_by_title(self, todo_title: str) -> TODO:
        todo = self.session.query(TODO).filter_by(title=todo_title).first()
        return todo
    
    def todo_exist_by_title(self, todo_title: str) -> bool:
        todo = self.session.query(TODO).filter_by(title=todo_title).first()
        return bool(todo)
