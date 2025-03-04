import settings
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from index_router import index_router
from contextlib import asynccontextmanager
from database.db_setup import apply_migrations


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("Server is starting...")
    apply_migrations()
    # await startup()

    yield

    logger.info("Server is shutting down...")
    # await shutdown()


app = FastAPI(lifespan=lifespan)


# Add CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(index_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    logger.info(f"Starting application with FASTAPI_ENVIRONMENT={settings.FASTAPI_ENVIRONMENT}")

    if settings.FASTAPI_ENVIRONMENT == "DEVELOPMENT":
        uvicorn.run("main:app", host=settings.SERVER_IP, port=settings.SERVER_PORT, reload=True, workers=2)
    else:
        uvicorn.run("main:app", host=settings.SERVER_IP, port=settings.SERVER_PORT, workers=2)
