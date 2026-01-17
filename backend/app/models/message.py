from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import ForeignKey, String, Text
from app.db.base import Base
import uuid

class Message(Base):
    __tablename__ = "messages"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("chat_sessions.id"))
    sender_type: Mapped[str] = mapped_column(String(10))
    sender_id: Mapped[uuid.UUID | None]
    content: Mapped[str] = mapped_column(Text)
