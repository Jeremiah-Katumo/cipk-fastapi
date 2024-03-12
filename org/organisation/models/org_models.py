from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ...database import Base


class Org(Base):
    __tablename__ = "orgs"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    org_uuid = Column(String, nullable=True, default=None)
    about = Column(String, nullable=True, default=None)
    location = Column(String, nullable=True, default=None)
    contacts = Column(String, nullable=True, default=None)
    welcome_message = Column(String, nullable=True, default=None)
    background = Column(String, nullable=True, default=None)
    mission = Column(String, nullable=True, default=None)
    vision = Column(String, nullable=True, default=None)
    core_values = Column(String, nullable=True, default=None)
    created_date = Column(String, nullable=True, default=None)
    updated_date = Column(String, nullable=True, default=None)
    created_by = Column(String, nullable=True, default=None)
    updated_by = Column(String, nullable=True, default=None)
    org_status = Column(String, nullable=True, default=None)


class ContactMessage(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    # org_id = Column(Integer, ForeignKey("orgs.id"))
    email = Column(String)
    subject = Column(String)
    message = Column(String)
    status = Column(String)
    created_date = Column(String)
    updated_date = Column(String)
    created_by = Column(String)
    updated_by = Column(String)

    # owner = relationship("Org", back_populates="id")