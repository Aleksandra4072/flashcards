from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routes.auth import auth_router
app = FastAPI()

origins: list[str] = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router)
# app.include_router(task_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
