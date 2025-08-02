from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.chat import router as chat_router
from api.routes.history import router as history_router
from api.routes.uploads import router as uploads_router

app = FastAPI(title="InsurePal HackRx API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/chat", tags=["Chat"])
app.include_router(history_router, prefix="/history", tags=["History"])
app.include_router(uploads_router, prefix="/hackrx", tags=["HackRx"])
