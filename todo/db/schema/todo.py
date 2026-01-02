from pydantic import BaseModel
from typing import Union

class CreateTodo(BaseModel):
    title: str
    content: str

class DeleteTodo(BaseModel):
    title: str

class TodoOutput(BaseModel):
    id: int
    title: str
    content: str

class UpdateTodo(BaseModel):
    int: int
    title: Union[str, None] = None
    content: Union[str, None] = None