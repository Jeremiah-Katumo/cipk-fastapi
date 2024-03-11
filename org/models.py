from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Org(Base):
    __tablename__ = "orgs"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    org_uuid = Column(String)
    location = Column(String)
    contacts = Column(String)
    welcome_message = Column(String)
    background = Column(String)
    mission = Column(String)
    vision = Column(String)
    core_values = Column(String)
    team_members = Column(String)
    faqs = Column(String)
    created_date = Column(String)
    updated_date = Column(String)
    created_by = Column(String)
    updated_by = Column(String)
    org_status = Column(String)


class ContactMessage(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    org_id = Column(Integer, ForeignKey("orgs.id"))
    email = Column(String)
    subject = Column(String)
    message = Column(String)
    status = Column(String)
    created_date = Column(String)
    updated_date = Column(String)
    created_by = Column(String)
    updated_by = Column(String)

    owner = relationship("Org", back_populates="id")