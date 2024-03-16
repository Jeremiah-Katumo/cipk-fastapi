from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON
from sqlalchemy.orm import relationship

from ...database import Base

 
class Org(Base):
    __tablename__ = "orgs"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    org_uuid = Column(String(36), nullable=True, default=None)
    about = Column(String(1000), nullable=True, default=None)
    location = Column(String(50), nullable=True, default=None)
    contacts = Column(JSON, nullable=True, default=None)
    welcome_message = Column(String(100), nullable=True, default=None)
    background = Column(String(100), nullable=True, default=None)
    mission = Column(String(50), nullable=True, default=None)
    vision = Column(String(100), nullable=True, default=None)
    core_values = Column(String(50), nullable=True, default=None)
    created_date = Column(String(10), nullable=True, default=None)
    updated_date = Column(String(10), nullable=True, default=None)
    created_by = Column(String(10), nullable=True, default=None)
    updated_by = Column(String(10), nullable=True, default=None)
    org_status = Column(String(10), nullable=True, default=None)


class ContactMessage(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True)
    # org_id = Column(Integer, ForeignKey("orgs.id"))
    email = Column(String(20))
    subject = Column(String(20))
    message = Column(String(100))
    status = Column(String(2))
    created_date = Column(String(10))
    updated_date = Column(String(10))
    created_by = Column(String(50))
    updated_by = Column(String(50))

    # owner = relationship("Org", back_populates="id")