from app.db.session import db_session


class BaseService:
    def __init__(self, session: db_session) -> None:
        self.session = session
