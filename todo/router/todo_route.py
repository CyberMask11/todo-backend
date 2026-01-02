from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Body
from todo.db.schema.todo import CreateTodo, TodoOutput, DeleteTodo
from todo.service.userService import UserService
from todo.core.database import get_db

route = APIRouter()

@route.post('/todo', status_code=201, response_model=TodoOutput)
def create_todo(details: CreateTodo, session: Session = Depends(get_db)) -> CreateTodo:
    return UserService(session=session).create_todo(Details=details)

@route.delete('/todo')
def delete_todo(title: DeleteTodo = Body(...), session: Session = Depends(get_db)):
    return UserService(session=session).delete_todo(todo_title=title.title)

@route.get('/todo/{Todo_id}', status_code=200, response_model=TodoOutput)
def get_todo(Todo_id: int, session: Session = Depends(get_db)):
    return UserService(session=session).get_todo(todo_id=Todo_id)

@route.get('/todo', status_code=200, response_model=list[TodoOutput])
def get_all(session: Session = Depends(get_db)):
    return UserService(session=session).get_all_todos()
    