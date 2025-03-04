from sqlalchemy import Column, DateTime, text
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.sql import func


class CustomBase:
    """
    Abstract base class model.

    Abstract base class model provides self updating ``created`` and
    ``modified`` fields.
    """

    @declared_attr
    def __tablename__(cls):
        """Tablename in lower case."""
        return cls.__name__.lower()

    created = Column(
        DateTime,
        nullable=False,
        default=func.now(),
        server_default=text("NOW()::timestamp"),
    )

    modified = Column(
        DateTime,
        nullable=False,
        default=func.now(),
        server_default=text("NOW()::timestamp"),
        onupdate=func.now()
    )


Base = declarative_base(cls=CustomBase)
