"""Module initialize a database session."""
from core.config import settings
from db.engine import create_engine
from db.session import Session


def get_db() -> Session:
    """Get database conenction, in this case is fake DB since it's been used file.

    Returns:
        _type_: Database Session.
    """
    engine = create_engine(settings.DATABASE_FILE)
    return Session(engine)
