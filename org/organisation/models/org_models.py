from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, JSON, Text
from sqlalchemy.orm import relationship
from ...utils import ListType
from ...database import Base
from datetime import date
import uuid
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class Org(Base):
    __tablename__ = "orgs"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    org_uuid = Column(String(255), unique=True, nullable=False, default=uuid.uuid4)
    about = Column(Text, nullable=True, default=None)
    location = Column(Text, nullable=True, default=None)
    contacts = Column(ListType, nullable=True, default=None)
    welcome_message = Column(Text, nullable=True, default=None)
    background = Column(Text, nullable=True, default=None)
    mission = Column(Text, nullable=True, default=None)
    vision = Column(Text, nullable=True, default=None)
    core_values = Column(ListType, nullable=True, default=None)
    created_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_date = Column(Date, nullable=True, default=None)
    created_by = Column(Integer, nullable=True, default=None)
    updated_by = Column(Integer, nullable=True, default=None)
    org_status = Column(String(10), default='active')

    messages = relationship("ContactMessage", back_populates="org")

class ContactMessage(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    org_id = Column(Integer, ForeignKey("orgs.id"))
    email = Column(String(100), index=True)
    subject = Column(String(200))
    message = Column(Text)
    status = Column(String(10), default='new')
    # created_date = Column(String)
    created_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_date = Column(Date, nullable=True, default=None)
    created_by = Column(Integer, nullable=True, default=None)
    updated_by = Column(Integer, nullable=True, default=None)

    org = relationship("Org", back_populates="messages")