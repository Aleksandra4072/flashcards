import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware

from app.routes.auth import auth_router
from app.routes.bundle import bundle_router
from app.routes.flashcard import flashcard_router
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
app.include_router(bundle_router)
app.include_router(flashcard_router)


@app.get("/download_file/{filename}")
async def download_file(filename: str):
    file_path = f"app/data/{filename}"
    if os.path.exists(file_path):
        return FileResponse(path=file_path, filename=filename)
    else:
        return {"error": "File not found"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
