from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database import Base

class TranslationHistory(Base):
    __tablename__ = "translation_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    source_text = Column(String(1000), nullable=False)
    translated_text = Column(String(1000), nullable=False)
    direction = Column(String(10), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())