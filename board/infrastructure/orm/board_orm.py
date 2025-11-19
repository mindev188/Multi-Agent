from datetime import datetime

from sqlalchemy import Integer, String, DateTime, Column

from config.database.session import Base


class BoardORM(Base):
    __tablename__ = "board"

    id = Column(Integer, primary_key=True, index=True)
    owner = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
