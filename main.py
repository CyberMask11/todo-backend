from fastapi import FastAPI
from todo.util.init_db import create_tables
from todo.router.todo_route import route
from fastapi.middleware.cors import CORSMiddleware

async def lifespan(todo: FastAPI):
    create_tables()
    yield

todo = FastAPI(lifespan=lifespan)
todo.include_router(route, tags=["TO-DO"])
todo.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"] for tighter security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@todo.get('/post')
def post():
    return {
        "response": "this is a todo"
    }