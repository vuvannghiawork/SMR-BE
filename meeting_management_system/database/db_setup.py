from loguru import logger
from alembic import command, config


def apply_migrations():
    logger.info("Applying migrations")
    alembic_cfg = config.Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
    logger.info("Done applying migrations")
