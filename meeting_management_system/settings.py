from loguru import logger
from environs import Env


log_file_format = "{time:YYYY-MM-DD}.log"
logger.add(f"logging/{log_file_format}", rotation="00:00", retention="7 days", enqueue=True)


env = Env()
logger.info(f"Loading environment variables...")


FASTAPI_ENVIRONMENT = env.str("FASTAPI_ENVIRONMENT", default="PRODUCTION")
SERVER_IP = env.str("SERVER_IP", default="0.0.0.0")
SERVER_PORT = env.int("SERVER_PORT", default=8314)


POSTGRES_HOST = env.str("POSTGRES_HOST", default="localhost")
POSTGRES_PORT = env.int("POSTGRES_PORT", default=5432)
POSTGRES_USER = env.str("POSTGRES_USER", default="postgres")
POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD", default="postgres")
POSTGRES_DB = env.str("POSTGRES_DB", default="postgres")
SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
