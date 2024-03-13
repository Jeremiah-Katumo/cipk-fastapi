from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
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
    name = Column(String, unique=True)
    org_uuid = Column(String, unique=True, nullable=False, default=uuid.uuid4)
    about = Column(String, nullable=True, default=None)
    location = Column(String, nullable=True, default=None)
    contacts = Column(ListType, nullable=True, default=None)
    welcome_message = Column(String, nullable=True, default=None)
    background = Column(String, nullable=True, default=None)
    mission = Column(String, nullable=True, default=None)
    vision = Column(String, nullable=True, default=None)
    core_values = Column(ListType, nullable=True, default=None)
    # created_date = Column(Date, default=date.today)
    created_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_date = Column(Date, nullable=True, default=None)
    created_by = Column(String, nullable=True, default=None)
    updated_by = Column(String, nullable=True, default=None)
    org_status = Column(String, default='active')

    messages = relationship("ContactMessage", back_populates="org")

class ContactMessage(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    org_id = Column(Integer, ForeignKey("orgs.id"))
    email = Column(String)
    subject = Column(String)
    message = Column(String)
    status = Column(String, default='new')
    # created_date = Column(String)
    created_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_date = Column(String)
    created_by = Column(String)
    updated_by = Column(String)

    org = relationship("Org", back_populates="messages")