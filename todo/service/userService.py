from sqlalchemy.orm import Session
from todo.db.schema.todo import CreateTodo
from todo.db.repository.userRepo import UserRepo, TodoOutput
from fastapi import HTTPException

class UserService:
    def __init__(self, session: Session):
        self.__userRepository = UserRepo(session=session)
    
    def create_todo(self, Details: CreateTodo) -> TodoOutput:
        if self.__userRepository.todo_exist_by_title(todo_title=Details.title):
            raise HTTPException(status_code=400, detail="This todo exist")
        
        todo_create = self.__userRepository.create_todo(todo_details=Details)
        return todo_create
    
    def get_todo(self, todo_id: int) -> TodoOutput:
        try:
            todo = self.__userRepository.get_todo_by_id(todo_id=todo_id)
            return todo
        except Exception as e:
            raise e
        
    def get_all_todos(self) -> list[TodoOutput]:
        return self.__userRepository.get_all_todo()
    
    def delete_todo(self, todo_title: str):
        todo = self.__userRepository.get_todo_by_title(todo_title=todo_title)
        try:
            return self.__userRepository.delete_todo(todo_id=todo.id)
        except Exception as e:
            raise e